import math # Biblioteca estándar (Unidad II)

# =============================================================================
# SECCIÓN 1: FUNDAMENTOS Y REPRESENTACIÓN DE DATOS
# Temas: Variables, Tipos de Datos, Entrada/Salida, Pirámide DIKW
# =============================================================================

print("--- SECCIÓN 1: FUNDAMENTOS ---")

# 1.1. Variables y Tipado Dinámico
# En Python, no declaramos el tipo explícitamente, se infiere del valor.
nombre_estudiante = "Alex"        # str (Cadena)
edad = 19                         # int (Entero)
promedio = 8.5                    # float (Real/Flotante)
esta_matriculado = True           # bool (Lógico)
numero_complejo = 4 + 3j          # complex (Complejo - Específico de Python)

# Verificamos los tipos (Función type() - Built-in)
print(f"Variable 'promedio' es de tipo: {type(promedio)}")

# 1.2. Entrada y Salida (Input/Output)
# Norma: input() SIEMPRE devuelve un string. Hay que hacer 'casting' (conversión).

# print("Por favor, introduce tus datos:")
# dato_entrada = input("Dime tu altura en metros (ej. 1.75): ") 
# altura = float(dato_entrada) # Conversión explícita

# Salida con formato (f-strings - Moderno y recomendado)
# print(f"Hola {nombre_estudiante}, tu altura es {altura}m.")

# Salida con parámetros especiales (sep y end)
print("Datos", "en", "bruto", sep=" - ", end=" [FIN DE LINEA]\n")

# -----------------------------------------------------------------------------
# RETO 1 (Para el estudiante):
# Escribe un programa que pida al usuario los grados Celsius (input)
# y los convierta a Fahrenheit y Kelvin.
# Fórmulas: K = C + 273.15, F = (C * 9/5) + 32
# Muestra los resultados usando f-strings con 2 decimales.
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 2: OPERADORES Y SISTEMAS NUMÉRICOS
# Temas: Aritmética, Módulo Math, Binario/Hexadecimal
# =============================================================================

print("\n--- SECCIÓN 2: MATEMÁTICAS Y LÓGICA ---")

# 2.1. Operadores Aritméticos
a = 10
b = 3

suma = a + b
division_decimal = a / b   # 3.3333...
division_entera = a // b   # 3 (Descarta decimales)
modulo = a % b             # 1 (El resto de la división - CRUCIAL para par/impar)
potencia = a ** b          # 1000 (10 elevado a 3)

# 2.2. Biblioteca Math
raiz = math.sqrt(25)
seno = math.sin(math.radians(90)) # Ojo: sin/cos usan radianes, no grados.

# 2.3. Sistemas Numéricos (Unidad II)
# Python tiene funciones built-in para esto.
numero = 255
print(f"Decimal: {numero}")
print(f"Binario: {bin(numero)}") # Prefijo 0b
print(f"Hexadecimal: {hex(numero)}") # Prefijo 0x

# -----------------------------------------------------------------------------
# RETO 2 (Para el estudiante):
# Usa el operador módulo (%) para determinar si un número ingresado
# por el usuario es PAR o IMPAR. Imprime True si es Par, False si es Impar.
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 3: ESTRUCTURAS DE CONTROL (DECISIONES)
# Temas: Lógica Proposicional, if, elif, else
# =============================================================================

print("\n--- SECCIÓN 3: CONTROL DE FLUJO (DECISIONES) ---")

# 3.1. Operadores Relacionales y Lógicos
# Relacionales: >, <, >=, <=, == (igualdad), != (diferente)
# Lógicos: and (Y), or (O), not (NO)

nota = 6.5
asistencia = 85

# Estructura condicional (Norma 5)
if nota >= 5.0 and asistencia >= 80:
    estado = "Aprobado"
elif nota >= 4.0 and asistencia >= 90: # Caso especial (ejemplo)
    estado = "Recuperación"
else:
    estado = "Suspenso"

print(f"Estado del alumno: {estado}")

# Anidamiento (Decisiones dentro de decisiones)
if estado == "Aprobado":
    if nota >= 9.0:
        print("¡Matrícula de Honor!")

# -----------------------------------------------------------------------------
# RETO 3 (Para el estudiante):
# "El portero de la discoteca": Pide la edad al usuario.
# Si es menor de 18: "No pasas".
# Si tiene entre 18 y 65: "Pasa".
# Si es mayor de 65: "Pasa VIP".
# EXTRA: Si escribe una edad negativa, decir "Error".
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 4: ESTRUCTURAS DE CONTROL (CICLOS/BUCLES)
# Temas: for (Iteración definida), while (Iteración indefinida), range()
# =============================================================================

print("\n--- SECCIÓN 4: CICLOS (LOOPS) ---")

# 4.1. Ciclo FOR (Norma 6 - Repetición Indexada)
# Usamos range(inicio, fin_sin_incluir, paso)
print("Tabla del 5:")
for i in range(1, 11): # Del 1 al 10
    print(f"5 x {i} = {5*i}")

# 4.2. Ciclo WHILE (Norma 6 - Repetición Condicionada)
# Útil cuando no sabemos cuántas veces se repetirá (ej. validación)
# contador = 5
# while contador > 0:
#     print(f"Despegue en {contador}...")
#     contador -= 1 # Importante: modificar la variable de control para evitar bucles infinitos
# print("¡Despegue!")

# 4.3. Validación de entrada (Patrón común en exámenes)
# numero_valido = -1
# while numero_valido < 0:
#     try:
#         numero_valido = int(input("Introduce un número positivo: "))
#     except ValueError:
#         print("Eso no es un número.")

# -----------------------------------------------------------------------------
# RETO 4 (Para el estudiante):
# Crea un "Acumulador":
# Pide números al usuario continuamente.
# Si introduce un 0, el programa termina.
# Al final, muestra la SUMA total de los números introducidos.
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 5: ESTRUCTURAS DE DATOS (ARREGLOS Y LISTAS)
# Temas: Listas, Índices, Slicing, Métodos de lista
# =============================================================================

print("\n--- SECCIÓN 5: LISTAS (VECTORES) ---")

# 5.1. Creación y Acceso
# En Python las listas funcionan como vectores dinámicos.
notas = [4.5, 6.0, 7.5, 9.0]
nombres = ["Ana", "Beto", "Carla", "Dani"] # Arreglos Paralelos (Concepto de clase)

# Acceso por índice (Empieza en 0)
print(f"Nota de {nombres[0]}: {notas[0]}")

# Índices negativos (Característica de Python)
print(f"Último alumno: {nombres[-1]}")

# 5.2. Slicing (Rebanadas) [inicio : fin : paso]
sub_lista = nombres[1:3] # ['Beto', 'Carla'] (El índice 3 no se incluye)

# 5.3. Métodos Importantes
notas.append(10.0)      # Añadir al final
notas.insert(0, 2.5)    # Insertar en posición específica
notas.pop()             # Eliminar el último
# notas.remove(6.0)     # Eliminar por valor
longitud = len(notas)   # Tamaño del vector

# 5.4. Recorrido de Listas
# Forma A: Por elemento
for nota in notas:
    pass # 'pass' es una instrucción vacía para que no de error este ejemplo

# Forma B: Por índice (Necesario para modificar la lista o usar paralelos)
print("Listado oficial:")
for i in range(len(nombres)):
    print(f"{i+1}. {nombres[i]} tiene un {notas[i]}")

# -----------------------------------------------------------------------------
# RETO 5 (Para el estudiante):
# Dado el vector: numeros = [4, 2, 9, 1, 5, 6]
# 1. Encuentra el número MAYOR sin usar la función max().
# 2. Calcula el PROMEDIO de los valores.
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 6: MATRICES (LISTAS DE LISTAS)
# Temas: Arreglos Bidimensionales (2D)
# =============================================================================

print("\n--- SECCIÓN 6: MATRICES ---")

# Una matriz es una lista donde cada elemento es otra lista (fila).
matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]

# Acceso: matriz[fila][columna]
centro = matriz[1][1] # El 5

# Recorrido anidado (Nested Loops)
# print("Imprimiendo matriz como tabla:")
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end="\t") # \t es tabulador
#     print() # Salto de línea al terminar la fila

# -----------------------------------------------------------------------------
# RETO 6 (Para el estudiante):
# Suma la DIAGONAL PRINCIPAL de la matriz anterior (1 + 5 + 9).
# Pista: En la diagonal, el índice de fila es igual al de columna [i][i].
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 7: CADENAS DE CARACTERES (STRINGS)
# Temas: Métodos de string, Inmutabilidad
# =============================================================================

print("\n--- SECCIÓN 7: STRINGS ---")

texto = "  Python es Genial  "

# Los strings son como listas de caracteres (pero inmutables)
primera_letra = texto[2] # 'P' (por los espacios iniciales)

# Limpieza y formato
texto_limpio = texto.strip()         # Quita espacios inicio/fin
mayusculas = texto_limpio.upper()    # "PYTHON ES GENIAL"
busqueda = texto_limpio.find("es")   # Devuelve el índice donde empieza

# F-Strings con formato numérico (Unidad II/III)
precio = 12.34567
print(f"Precio formateado: {precio:.2f}€") # 12.35€

# -----------------------------------------------------------------------------
# RETO 7 (Para el estudiante):
# Pide una frase al usuario.
# Muestra cuántas vocales (a, e, i, o, u) tiene esa frase.
# Pista: Usa un bucle for sobre el string y un if.
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 8: OTRAS ESTRUCTURAS (TUPLAS, SETS, DICCIONARIOS)
# Temas: Inmutabilidad, Unicidad, Clave-Valor
# =============================================================================

print("\n--- SECCIÓN 8: OTRAS ESTRUCTURAS ---")

# TUPLAS: Como listas, pero NO se pueden modificar (Inmutables). Paréntesis ().
coordenadas = (10, 20)
# coordenadas[0] = 5  # ESTO DARÍA ERROR

# SETS (Conjuntos): Desordenados y SIN DUPLICADOS. Llaves {}.
colores = {"Rojo", "Verde", "Azul", "Rojo"} 
# print(colores) # "Rojo" solo aparece una vez. Útil para eliminar duplicados.

# DICCIONARIOS: Clave -> Valor. Llaves {k:v}. (Como una base de datos pequeña).
alumno = {
    "nombre": "Carlos",
    "edad": 20,
    "asignaturas": ["Programación", "Matemáticas"]
}

# Acceso
# print(f"El alumno se llama {alumno['nombre']}")

# Modificación
alumno["edad"] = 21      # Modificar
alumno["nota_media"] = 7.5 # Añadir nuevo

# Recorrido de diccionario
# for clave, valor in alumno.items():
#     print(f"{clave}: {valor}")

# -----------------------------------------------------------------------------
# RETO 8 (Para el estudiante):
# Crea un diccionario simple inglés-español (ej. "dog":"perro", "cat":"gato").
# Pide al usuario una palabra en inglés y muestra su traducción.
# Si la palabra no existe, di "No conozco esa palabra". (Usa .get() o in).
# -----------------------------------------------------------------------------
# Espacio para solución del alumno:



# =============================================================================
# SECCIÓN 9: PROGRAMACIÓN MODULAR (FUNCIONES)
# Temas: Definición, Parámetros, Retorno, Scope, Diseño Descendente
# =============================================================================

print("\n--- SECCIÓN 9: FUNCIONES ---")

# Definición (Norma 2 - Declaraciones)
# Diseño Descendente: Romper un problema grande en funciones pequeñas.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Parámetros: base (float), altura (float)
    Retorna: float
    """
    area = base * altura
    return area # Devuelve el valor, no lo imprime dentro (normalmente)

# Invocación (Llamada)
b = 5
h = 3
resultado = calcular_area_rectangulo(b, h)
print(f"El área de base {b} y altura {h} es: {resultado}")

# Ámbito (Scope)
variable_global = "Soy global"

def prueba_ambito():
    variable_local = "Soy local"
    print(variable_global) # Puede ver la global
    # print(variable_local) # Funciona aquí

# print(variable_local) # ERROR: No existe fuera de la función

# -----------------------------------------------------------------------------
# RETO FINAL (PROYECTO MINIATURA):
# Crea una función llamada 'es_primo(numero)' que devuelva True o False.
# Luego, usa esa función en un bucle para imprimir todos los primos entre 1 y 20.
# -----------------------------------------------------------------------------
# Espacio para solución del alumno: