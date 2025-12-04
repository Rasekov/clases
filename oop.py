# Instalar UV:
# curl -LsSf https://astral.sh/uv/install.sh | sh
# o
# wget -qO- https://astral.sh/uv/install.sh | sh
#
# Crear virtual environment
# uv venv
#
# Instalar matplotlib
# uv pip install matplotlib

# ==============================================================================
# DIAGRAMA ASCII DE LA JERARQUÍA DE CLASES (PARA REFERENCIA VISUAL)
# ==============================================================================
#
#                             ┌──────────────────────┐
#                             │      Documento       │
#                             │----------------------│
#                             │ nombre               │
#                             │ tipo_documento       │
#                             │ fecha (date)         │
#                             │ etiquetas            │
#                             │----------------------│
#                             │ agregar_etiqueta()   │
#                             │ obtener_edad_dias()  │
#                             │ mostrar_info()       │
#                             └───────────┬──────────┘
#                     ┌───────────────────┴─────────────────┐
#                     │                                     │
#        ┌──────────────────────────┐         ┌────────────────────────────┐
#        │     DocumentoFisico      │         │     DocumentoDigital       │
#        │--------------------------│         │----------------------------│
#        │ ubicacion_almacenamiento │         │ ruta_archivo               │
#        │ prestado                 │         │ version                    │
#        │ prestado_a               │         │----------------------------│
#        │--------------------------│         │ actualizar_version()       │
#        │ prestar()                │         │ obtener_extension_archivo()│
#        │ devolver()               │         │ mostrar_info()             │
#        │ mostrar_info()           │         │                            |
#        └───────────┬──────────────┘         └──────────────┬─────────────┘
#               ┌────┴────┐                            ┌─────┴──────┐
#               │         │                            │            │
#   ┌──────────────────┐┌──────────────────┐┌────────────────────┐┌──────────────────┐
#   │     Contrato     ││      NDA         ││        Email       ││ Archivo          │
#   │------------------││------------------││--------------------││------------------│
#   │ partes           ││ parte_divulgadora││ remitente          ││ datos            │
#   │ valor            ││ parte_receptora  ││ destinatario       ││------------------│
#   │ ejecutado        ││ fecha_expiracion ││ asunto             ││ cargar_csv()     │
#   │------------------││------------------││ leido, destacado   ││ analizar_datos() │
#   │ ejecutar()       ││ esta_expirado()  ││ marcar_leido()     ││ graficar_datos() │
#   │ calcular_valor_..││ dias_hasta_exp...││ alternar_estrella()││ mostrar_info()   │
#   │ mostrar_info()   ││ mostrar_info()   ││ mostrar_info()     │└──────────────────┘
#   └──────────────────┘└──────────────────┘└────────────────────┘
#
# ==============================================================================

# %% [markdown]
# # Sistema de Gestión de Documentos Legales
# Esto demuestra conceptos de POO: herencia, polimorfismo y sobrescritura de métodos

# %% Importaciones y Definiciones de Clases
from datetime import date, datetime

# ==============================================================================
# CLASE BASE - Documento
# ==============================================================================
# Esta es la base. Todos los documentos comparten estas características básicas.
# Al poner la funcionalidad común aquí, evitamos repetir código en las clases hijas.

class Documento:
    def __init__(self, nombre, tipo_documento, fecha):
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.fecha = datetime.strptime(fecha, "%d-%m-%y").date()
        self.etiquetas = []  # Para categorizar documentos
    
    def agregar_etiqueta(self, etiqueta):
        """Agregar una etiqueta para categorización - heredado por TODOS los tipos de documento"""
        if etiqueta not in self.etiquetas:
            self.etiquetas.append(etiqueta)
            return f"Etiqueta '{etiqueta}' agregada a {self.nombre}"
        return f"Etiqueta '{etiqueta}' ya existe"
    
    def obtener_edad_dias(self):
        """Calcular cuántos días tiene el documento - heredado por TODOS los tipos de documento"""
        edad = date.today() - self.fecha
        return edad.days
    
    def mostrar_info(self):
        """Mostrar detalles del documento - ESTO SE SOBRESCRIBE en las clases hijas"""
        info = f"{self.nombre} ({self.tipo_documento}) - {self.fecha.strftime('%d-%m-%y')}"
        if self.etiquetas:
            info += f"\nEtiquetas: {', '.join(self.etiquetas)}"
        return info


# ==============================================================================
# DOCUMENTOS FÍSICOS - Primer nivel de herencia
# ==============================================================================
# DocumentoFisico hereda TODOS los métodos de Documento (agregar_etiqueta, obtener_edad_dias, mostrar_info)
# MÁS agrega nuevos métodos específicos para almacenamiento físico (prestar, devolver)

class DocumentoFisico(Documento):
    tipo_documento = "DocumentoFisico"

    def __init__(self, nombre, tipo_documento, fecha, ubicacion_almacenamiento):
        # Llamar al constructor padre para configurar nombre, tipo_documento, fecha, etiquetas
        super().__init__(nombre, self.tipo_documento, fecha)
        # Agregar nuevo atributo específico para documentos físicos
        self.ubicacion_almacenamiento = ubicacion_almacenamiento
        self.prestado = False
        self.prestado_a = None
    
    def prestar(self, nombre_persona):
        """MÉTODO NUEVO - solo los documentos físicos pueden ser prestados"""
        if self.prestado:
            return f"Ya está prestado a {self.prestado_a}"
        self.prestado = True
        self.prestado_a = nombre_persona
        return f"Prestado a {nombre_persona}"
    
    def devolver(self):
        """MÉTODO NUEVO - devolver un documento físico"""
        if not self.prestado:
            return "El documento no está prestado"
        persona = self.prestado_a
        self.prestado = False
        self.prestado_a = None
        return f"Devuelto por {persona}"
    
    def mostrar_info(self):
        """SOBRESCRIBIR método padre - agregar ubicación de almacenamiento a la visualización"""
        # Llamar primero al mostrar_info del padre usando super()
        info = super().mostrar_info()
        # Luego agregar nuestra propia información
        info += f"\nAlmacenado en: {self.ubicacion_almacenamiento}"
        if self.prestado:
            info += f"\n⚠️  Prestado a: {self.prestado_a}"
        return info


# ==============================================================================
# CONTRATO - Segundo nivel de herencia
# ==============================================================================
# Contrato hereda de DocumentoFisico, lo que significa que obtiene:
# - De Documento: agregar_etiqueta(), obtener_edad_dias(), mostrar_info()
# - De DocumentoFisico: prestar(), devolver(), ubicacion_almacenamiento
# MÁS agrega métodos específicos de contrato (ejecutar, calcular_valor_por_parte)

class Contrato(DocumentoFisico):
    tipo_documento = "Contrato"

    def __init__(self, nombre, fecha, ubicacion_almacenamiento, partes, valor):
        # Llamar al constructor de DocumentoFisico (que llama al constructor de Documento)
        super().__init__(nombre, self.tipo_documento, fecha, ubicacion_almacenamiento)
        # Agregar atributos específicos de contrato
        self.partes = partes  # Lista de empresas/personas en el contrato
        self.valor = valor    # Valor monetario del contrato
        self.ejecutado = False
    
    def ejecutar(self):
        """MÉTODO NUEVO - marcar contrato como legalmente ejecutado"""
        if self.ejecutado:
            return "El contrato ya está ejecutado"
        self.ejecutado = True
        self.agregar_etiqueta("ejecutado")  # ¡Usando método heredado de Documento!
        return "El contrato ha sido ejecutado"
    
    def calcular_valor_por_parte(self):
        """MÉTODO NUEVO - dividir el valor del contrato entre las partes"""
        return self.valor / len(self.partes)
    
    def mostrar_info(self):
        """SOBRESCRIBIR de nuevo - agregar detalles específicos del contrato"""
        # Obtener info del mostrar_info de DocumentoFisico (que incluye la info de Documento)
        info = super().mostrar_info()
        # Agregar información específica del contrato
        info += f"\nPartes: {', '.join(self.partes)}"
        info += f"\nValor: ${self.valor:,.2f} (${self.calcular_valor_por_parte():,.2f} por parte)"
        info += f"\nEstado: {'✓ Ejecutado' if self.ejecutado else '⏳ Pendiente'}"
        return info


# ==============================================================================
# NDA (Acuerdo de Confidencialidad) - Otra herencia de segundo nivel
# ==============================================================================
# NDA también hereda de DocumentoFisico (hermano de Contrato)
# Obtiene los mismos métodos heredados pero agrega métodos DIFERENTES específicos para NDAs

class NDA(DocumentoFisico):
    tipo_documento = "NDA"

    def __init__(self, nombre, fecha, ubicacion_almacenamiento, parte_divulgadora, parte_receptora, fecha_expiracion):
        super().__init__(nombre, self.tipo_documento, fecha, ubicacion_almacenamiento)
        self.parte_divulgadora = parte_divulgadora
        self.parte_receptora = parte_receptora
        self.fecha_expiracion = datetime.strptime(fecha_expiracion, "%d-%m-%y").date()
    
    def esta_expirado(self):
        """MÉTODO NUEVO - verificar si el NDA ha expirado"""
        return date.today() > self.fecha_expiracion
    
    def dias_hasta_expiracion(self):
        """MÉTODO NUEVO - calcular días restantes"""
        delta = self.fecha_expiracion - date.today()
        return delta.days
    
    def mostrar_info(self):
        """SOBRESCRIBIR - agregar detalles específicos del NDA"""
        info = super().mostrar_info()
        info += f"\n{self.parte_divulgadora} → {self.parte_receptora}"
        
        if self.esta_expirado():
            info += f"\n❌ EXPIRADO el {self.fecha_expiracion.strftime('%d-%m-%y')}"
        else:
            info += f"\n✓ Expira: {self.fecha_expiracion.strftime('%d-%m-%y')} ({self.dias_hasta_expiracion()} días restantes)"
        return info

# ==============================================================================
# DOCUMENTOS DIGITALES - Primer nivel de herencia (paralelo a DocumentoFisico)
# ==============================================================================
# DocumentoDigital también hereda de Documento (como lo hace DocumentoFisico)
# Pero agrega métodos DIFERENTES relacionados con archivos digitales en lugar de almacenamiento físico

class DocumentoDigital(Documento):
    tipo_documento = "DocumentoDigital"

    def __init__(self, nombre, tipo_documento, fecha, ruta_archivo):
        super().__init__(nombre, self.tipo_documento, fecha)
        self.ruta_archivo = ruta_archivo
        self.version = 1.0
    
    def actualizar_version(self, notas=""):
        """MÉTODO NUEVO - incrementar número de versión (característica digital)"""
        self.version += 0.1
        self.version = round(self.version, 1)
        return f"Actualizado a versión {self.version}: {notas}"
    
    def obtener_extension_archivo(self):
        """MÉTODO NUEVO - extraer tipo de archivo"""
        return self.ruta_archivo.split('.')[-1] if '.' in self.ruta_archivo else "desconocido"
    
    def mostrar_info(self):
        """SOBRESCRIBIR - agregar detalles del documento digital"""
        info = super().mostrar_info()
        info += f"\nArchivo: {self.ruta_archivo} (v{self.version})"
        return info


# ==============================================================================
# EMAIL (Correo Electrónico) - Segundo nivel de herencia
# ==============================================================================
# Email hereda de DocumentoDigital (obtiene seguimiento de versión, ruta de archivo)
# Más agrega métodos específicos de email (marcar_leido, alternar_estrella)

class Email(DocumentoDigital):
    tipo_documento = "Email"
    def __init__(self, nombre, fecha, remitente, destinatario, asunto):
        super().__init__(nombre, self.tipo_documento, fecha, ruta_archivo="servidor_email")
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.leido = False
        self.destacado = False
    
    def marcar_leido(self):
        """MÉTODO NUEVO - marcar email como leído"""
        self.leido = True
        return "Email marcado como leído"
    
    def alternar_estrella(self):
        """MÉTODO NUEVO - destacar/deshacer destacado de emails importantes"""
        self.destacado = not self.destacado
        return "Destacado" if self.destacado else "Sin destacar"
    
    def mostrar_info(self):
        estado = "✓" if self.leido else "📧"
        estrella = " ⭐" if self.destacado else ""
        info = f"{estado}{estrella} Asunto: {self.asunto}\n"
        info += f"De: {self.remitente} → Para: {self.destinatario}\n"
        info += f"Fecha: {self.fecha.strftime('%d-%m-%y')}"
        if self.etiquetas:
            info += f"\nEtiquetas: {', '.join(self.etiquetas)}"
        return info


# ==============================================================================
# DOCUMENTO DE ARCHIVO - Otra herencia de segundo nivel
# ==============================================================================
# Archivo hereda de DocumentoDigital (hermano de Email)
# Agrega métodos para análisis de datos CSV y visualización

class Archivo(DocumentoDigital):
    tipo_documento = "Archivo"
    def __init__(self, nombre, tipo_documento, fecha, ruta_archivo):
        super().__init__(nombre, self.tipo_documento, fecha, ruta_archivo)
        self.datos = []
    
    def cargar_csv(self, nombre_archivo):
        """MÉTODO NUEVO - cargar datos desde archivo CSV"""
        import csv
        with open(nombre_archivo, 'r') as f:
            lector = csv.reader(f)
            self.datos = list(lector)
        return self.datos
    
    def analizar_datos(self):
        """MÉTODO NUEVO - realizar estadísticas básicas sobre datos numéricos"""
        datos_numericos = []
        for fila in self.datos[1:]:  # Saltar fila de encabezado
            try:
                datos_numericos.append(float(fila[1]))  # Segunda columna
            except (ValueError, IndexError):
                continue
        
        if datos_numericos:
            return {
                'cantidad': len(datos_numericos),
                'suma': sum(datos_numericos),
                'promedio': sum(datos_numericos) / len(datos_numericos),
                'maximo': max(datos_numericos),
                'minimo': min(datos_numericos)
            }
        return None
    
    def graficar_datos(self):
        """MÉTODO NUEVO - crear visualización de gráfico de barras"""
        import matplotlib
        
        matplotlib.use('Agg')  # Usar backend no interactivo

        import matplotlib.pyplot as plt
        
        # Extraer datos para graficar
        etiquetas = [fila[0] for fila in self.datos[1:]]
        valores = [float(fila[1]) for fila in self.datos[1:]]
        
        # Crear gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(etiquetas, valores)
        plt.title(f"Análisis de {self.nombre}")
        plt.xlabel("Categoría")
        plt.ylabel("Valor")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        nombre_archivo = f"{self.nombre.replace(' ', '_')}_grafico.png"
        plt.savefig(nombre_archivo)
        print(f"Gráfico guardado en {nombre_archivo}")
        
        plt.close()

# ==============================================================================
# EMAIL ATTACHMENT - Herencia Múltiple
# ==============================================================================
# EmailAttachment hereda de AMBOS Email Y Archivo
# Esto demuestra que una clase puede heredar de múltiples padres
# Obtiene métodos relacionados con email (marcar_leido, alternar_estrella)
# Y métodos de análisis de archivos (cargar_csv, analizar_datos, graficar_datos)

class EmailAttachment(Email, Archivo):
    tipo_documento = "EmailAttachment"
    
    def __init__(self, nombre, fecha, remitente, destinatario, asunto, ruta_archivo):
        # Inicializar Email (que inicializa DocumentoDigital y Documento)
        Email.__init__(self, nombre, fecha, remitente, destinatario, asunto)
        # Inicializar atributos específicos de Archivo
        self.ruta_archivo = ruta_archivo
        self.datos = []
        self.tipo_documento = "EmailAttachment"
    
    def adjuntar_analisis(self):
        """MÉTODO NUEVO - combinar funcionalidad de email y archivo"""
        if not self.datos:
            return "No hay datos para analizar. Usa cargar_csv() primero."
        
        stats = self.analizar_datos()
        mensaje = f"\n📎 ANÁLISIS DEL ADJUNTO:\n"
        mensaje += f"   Archivo: {self.ruta_archivo}\n"
        mensaje += f"   Total puntos de datos: {stats['cantidad']}\n"
        mensaje += f"   Promedio: {stats['promedio']:.2f}\n"
        return mensaje
    
    def mostrar_info(self):
        """SOBRESCRIBIR - combinar información de email Y archivo"""
        # Obtener info básica del email
        info = Email.mostrar_info(self)
        # Agregar información del adjunto
        info += f"\n📎 Adjunto: {self.ruta_archivo} (v{self.version})"
        if self.datos:
            info += f"\n   Filas de datos: {len(self.datos)}"
        return info


# %% DEMOSTRACIÓN 1: Crear Documentos Físicos
print("=" * 70)
print("PARTE 1: DOCUMENTOS FÍSICOS")
print("=" * 70)

# Crear un contrato
contrato = Contrato(
    nombre="Acuerdo Smith-Jones",
    fecha="15-11-24",
    ubicacion_almacenamiento="Gabinete A, Cajón 3",
    partes=["Smith Corp", "Jones LLC"],
    valor=150000
)

print("\n--- Probando métodos HEREDADOS de la clase base Documento ---")
# ¡Estos métodos se definieron en Documento, pero Contrato puede usarlos!
print(contrato.agregar_etiqueta("urgente"))         # Heredado de Documento
print(contrato.agregar_etiqueta("cliente-smith"))   # Heredado de Documento
print(f"Edad del documento: {contrato.obtener_edad_dias()} días")  # Heredado de Documento

print("\n--- Probando métodos de DocumentoFisico ---")
# Estos métodos se definieron en DocumentoFisico
print(contrato.prestar("Alicia Johnson"))   # Heredado de DocumentoFisico

print("\n--- Probando métodos ESPECÍFICOS de CONTRATO ---")
# Estos métodos son únicos para Contrato
print(contrato.ejecutar())                  # Método propio de Contrato
print(f"Valor por parte: ${contrato.calcular_valor_por_parte():,.2f}")  # Método propio de Contrato

print("\n--- Visualización completa del contrato (usa mostrar_info sobrescrito) ---")
print(contrato.mostrar_info())

print("\n" + "-" * 70)

# Crear un NDA
nda = NDA(
    nombre="NDA Startup Tecnológica",
    fecha="01-12-24",
    ubicacion_almacenamiento="Gabinete B, Cajón 1",
    parte_divulgadora="StartupXYZ Inc",
    parte_receptora="Consultor Juan Pérez",
    fecha_expiracion="01-12-26"
)

print("\n--- NDA también hereda de DocumentoFisico ---")
print(nda.agregar_etiqueta("confidencial"))     # Heredado de Documento
print(nda.prestar("Roberto Smith"))             # Heredado de DocumentoFisico

print("\n--- Probando métodos ESPECÍFICOS de NDA ---")
# Estos métodos son únicos para NDA (¡diferentes de Contrato!)
print(f"¿Está expirado? {nda.esta_expirado()}")  # Método propio de NDA
print(f"Días hasta expiración: {nda.dias_hasta_expiracion()}")  # Método propio de NDA

print("\n--- Visualización completa del NDA ---")
print(nda.mostrar_info())


# %% DEMOSTRACIÓN 2: Documentos Digitales
print("\n\n" + "=" * 70)
print("PARTE 2: DOCUMENTOS DIGITALES")
print("=" * 70)

# Crear un email
email = Email(
    nombre="Comunicación con Cliente",
    fecha="03-12-24",
    remitente="abogado@bufete.com",
    destinatario="cliente@empresa.com",
    asunto="Re: Actualización del Caso"
)

print("\n--- Email hereda de DocumentoDigital Y Documento ---")
print(email.agregar_etiqueta("importante"))         # Heredado de Documento
print(email.actualizar_version("Borrador inicial")) # Heredado de DocumentoDigital

print("\n--- Probando métodos ESPECÍFICOS de EMAIL ---")
print(email.marcar_leido())                         # Método propio de Email
print(email.alternar_estrella())                    # Método propio de Email

print("\n--- Visualización completa del email ---")
print(email.mostrar_info())


# %% DEMOSTRACIÓN 3: Análisis de Archivos
print("\n\n" + "=" * 70)
print("PARTE 3: DOCUMENTO DE ARCHIVO CON ANÁLISIS DE DATOS")
print("=" * 70)

archivo_caso = Archivo(
    nombre="Estadísticas de Casos",
    tipo_documento="CSV",
    fecha="03-12-24",
    ruta_archivo="./horas_facturables.csv"
)

# Crear datos CSV de muestra
import csv
datos = [
    ["Mes", "Horas Facturables"],
    ["Enero", "120"],
    ["Febrero", "135"],
    ["Marzo", "98"],
    ["Abril", "142"],
    ["Mayo", "156"]
]

# Guardar los datos
with open("horas_facturables.csv", 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerows(datos)
print("Creado horas_facturables.csv")

print("\n--- Archivo hereda de DocumentoDigital Y Documento ---")
print(archivo_caso.agregar_etiqueta("analítica"))       # Heredado de Documento
print(archivo_caso.actualizar_version("Agregados datos Q1-Q2"))  # Heredado de DocumentoDigital

print("\n--- Probando métodos ESPECÍFICOS de ARCHIVO ---")
archivo_caso.cargar_csv("horas_facturables.csv")    # Método propio de Archivo
estadisticas = archivo_caso.analizar_datos()        # Método propio de Archivo

print(f"\nResultados del Análisis de Datos:")
print(f"  Total de horas: {estadisticas['suma']}")
print(f"  Promedio: {estadisticas['promedio']:.2f}")
print(f"  Máximo: {estadisticas['maximo']}")
print(f"  Mínimo: {estadisticas['minimo']}")

print("\n--- Creando visualización ---")
archivo_caso.graficar_datos()      # Método propio de Archivo

print("\n--- Visualización completa del documento de archivo ---")
print(archivo_caso.mostrar_info())


# %% DEMOSTRACIÓN 4: Polimorfismo
print("\n\n" + "=" * 70)
print("PARTE 4: POLIMORFISMO - Mismo Nombre de Método, Comportamiento Diferente")
print("=" * 70)

# Poner todos los diferentes tipos de documentos en una lista
todos_documentos = [contrato, nda, email, archivo_caso]

print("\n--- Llamando mostrar_info() en cada tipo de documento ---")
print("¡Observa cómo cada clase muestra información de manera diferente,")
print("pero podemos llamar al mismo método en todos ellos!\n")

for doc in todos_documentos:
    # Mismo nombre de método, pero cada clase proporciona su propia implementación
    print(doc.mostrar_info())
    print("-" * 70)

print("\n--- Llamando agregar_etiqueta() en cada tipo de documento ---")
print("Este método se hereda de la clase base Documento por TODOS los tipos:\n")

for doc in todos_documentos:
    # Mismo método, misma implementación, heredada por todos
    print(doc.agregar_etiqueta("revisado-2025"))

# %% DEMOSTRACIÓN 5: Herencia Múltiple
print("\n\n" + "=" * 70)
print("PARTE 5: HERENCIA MÚLTIPLE - EmailAttachment")
print("=" * 70)

# Crear datos de facturación para el adjunto
datos_facturacion = [
    ["Servicio", "Costo"],
    ["Consulta Legal", "500"],
    ["Redacción Contrato", "1200"],
    ["Revisión Documentos", "300"],
    ["Comparecencia", "800"]
]

with open("facturacion_cliente.csv", 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerows(datos_facturacion)

# Crear email con adjunto de datos
email_con_datos = EmailAttachment(
    nombre="Factura Mensual",
    fecha="04-12-24",
    remitente="contabilidad@bufete.com",
    destinatario="cliente@empresa.com",
    asunto="Factura de Servicios Legales - Diciembre 2024",
    ruta_archivo="./facturacion_cliente.csv"
)

print("\n--- EmailAttachment hereda de AMBOS Email Y Archivo ---")
print("¡Puede usar métodos de ambas clases padre!")

print("\n--- Métodos heredados de Email ---")
print(email_con_datos.marcar_leido())           # De Email
print(email_con_datos.alternar_estrella())      # De Email

print("\n--- Métodos heredados de Archivo ---")
email_con_datos.cargar_csv("facturacion_cliente.csv")  # De Archivo
print("Datos CSV cargados exitosamente")

print("\n--- Método NUEVO que combina ambas funcionalidades ---")
print(email_con_datos.adjuntar_analisis())      # Método propio que usa ambos padres

print("\n--- Generando gráfico del adjunto ---")
email_con_datos.graficar_datos()                # De Archivo

print("\n--- Visualización completa (combina info de ambos padres) ---")
print(email_con_datos.mostrar_info())

print("\n--- Verificando herencia múltiple ---")
print(f"¿Es un Email? {isinstance(email_con_datos, Email)}")
print(f"¿Es un Archivo? {isinstance(email_con_datos, Archivo)}")
print(f"¿Es un DocumentoDigital? {isinstance(email_con_datos, DocumentoDigital)}")
print(f"¿Es un Documento? {isinstance(email_con_datos, Documento)}")