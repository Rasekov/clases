### **Sesión 06: Práctica de Decisiones y Lógica Condicional**

*   **Temas Cubiertos:**
    *   Esta sesión no introduce conceptos nuevos. Es una sesión de práctica intensiva para aplicar la **Norma 5 (Decisiones)**.
    *   Resolución de problemas utilizando estructuras `if` (decisión simple), `if-else` (decisión compuesta) y `if-elif-else` (decisión anidada/múltiple).
    *   Refuerzo de la metodología de análisis **E-P-S (Entrada-Proceso-Salida)** como paso previo indispensable antes de programar.
    *   Práctica de validación de datos de entrada (por ejemplo, asegurar que un número sea positivo antes de hacer un cálculo).

*   **Enfoque de Enseñanza:**
    *   El objetivo es que el estudiante gane autonomía y confianza al traducir un enunciado en lenguaje natural a un programa lógico.
    *   Para cada ejercicio de la lista, insiste en que el estudiante complete primero el análisis E-P-S en papel o en un bloque de comentarios. Este paso es el más importante.
    *   Haz hincapié en la traducción de frases clave a operadores lógicos:
        *   "al menos 38°C" se traduce a `temperatura >= 38`.
        *   "un número positivo" se traduce a `numero > 0`.
        *   "entre 1960 y 2021" se traduce a `anio >= 1960 and anio <= 2021`.
    *   Utiliza el ejercicio de las tarifas de autobús (Ejercicio 10) para demostrar por qué `if-elif-else` es la estructura perfecta para manejar múltiples condiciones excluyentes (tramos o categorías).

#### Ejemplos de Código para la Sesión 06

```python
# S06_Ejemplos_Practica_Decisiones.py

# --- EJERCICIO 4: DIAGNÓSTICO DE FIEBRE ---
# Este es un ejemplo perfecto de una decisión compuesta (if-else).

# --- NORMA 1: IDENTIFICACIÓN ---
# Programa: S06_E04_Fiebre.py
# Descripción: Determina si un paciente tiene fiebre según su temperatura corporal.
# Autor: [Nombre del Estudiante]
# Fecha: [Fecha Actual]

"""
ANÁLISIS E-P-S (Ejercicio 4)

1.  Entrada:
    -   Temperatura corporal del paciente en grados Celsius.
        -   Identificador: temperatura
        -   Tipo: Real (float)

2.  Proceso:
    -   La condición para tener fiebre es que la temperatura sea de "al menos 38°C".
    -   Esto se traduce en la expresión lógica: temperatura >= 38.0
    -   Se usará una estructura if-else para mostrar un mensaje u otro.

3.  Salida:
    -   Un mensaje indicando si el paciente tiene o no estado febril.
        -   Tipo: Cadena (string)
"""

# --- NORMA 2: DECLARACIONES Y CONSTANTES ---
TEMPERATURA_FIEBRE = 38.0

# --- NORMA 3: INICIO ---
# Inicio

print("\n--- Sistema de Diagnóstico de Fiebre ---")
temp_str = input("Introduzca la temperatura corporal del paciente (en °C): ")
temperatura = float(temp_str)

# Proceso y Salida combinados en la estructura de decisión
if temperatura >= TEMPERATURA_FIEBRE:
    print("Condición del paciente: Estado Febril.")
else:
    print("Condición del paciente: Sin fiebre.")

# Fin
print("-" * 30)


# --- EJERCICIO 5: CONVERSIÓN DE DISTANCIA CON VALIDACIÓN ---
# Este ejemplo introduce la validación de la entrada antes de realizar el proceso.

# --- NORMA 1: IDENTIFICACIÓN ---
# Programa: S06_E05_Distancia.py
# Descripción: Convierte metros a cm y km, validando que la entrada sea positiva.

"""
ANÁLISIS E-P-S (Ejercicio 5)

1.  Entrada:
    -   Distancia en metros.
        -   Identificador: metros
        -   Tipo: Real (float)

2.  Proceso:
    -   Paso 1 (Validación): Verificar si la distancia es un número positivo (metros >= 0).
    -   Si no es válido, mostrar un mensaje de error y no hacer nada más.
    -   Si es válido:
        -   Calcular centímetros: centimetros = metros * 100
        -   Calcular kilómetros: kilometros = metros / 1000

3.  Salida:
    -   Si la entrada es válida, los valores convertidos a cm y km.
    -   Si la entrada es inválida, un mensaje de error.
"""

# --- NORMA 2: DECLARACIONES ---
# No hay constantes globales, las conversiones son directas.

# --- NORMA 3: INICIO ---
# Inicio
print("\n--- Conversor de Distancias ---")
metros_str = input("Introduce una distancia en metros: ")
metros = float(metros_str)

# Se aplica la estructura de decisión para validar la entrada
if metros < 0:
    # Salida para el caso de error
    print("Error: La distancia introducida es negativa. No se puede realizar el cálculo.")
else:
    # Proceso (solo se ejecuta si la entrada es válida)
    centimetros = metros * 100
    kilometros = metros / 1000
    
    # Salida para el caso de éxito
    print(f"{metros} metros son:")
    print(f"  -> {centimetros} centímetros.")
    print(f"  -> {kilometros} kilómetros.")

# Fin
print("-" * 30)


# --- EJERCICIO 10: CÁLCULO DE TARIFA DE AUTOBÚS ---
# Este es un ejemplo ideal para una decisión anidada/múltiple (if-elif-else).

# --- NORMA 1: IDENTIFICACIÓN ---
# Programa: S06_E10_Tarifas.py
# Descripción: Calcula el coste de un billete de autobús según el kilometraje.

"""
ANÁLISIS E-P-S (Ejercicio 10)

1.  Entrada:
    -   Distancia del viaje en kilómetros.
        -   Identificador: kilometraje
        -   Tipo: Real (float)

2.  Proceso:
    -   Se debe determinar la tarifa aplicable según los tramos:
        -   Tramo 1: Si km <= 500, la tarifa es 0.5 €/km.
        -   Tramo 2: Si 500 < km <= 800, la tarifa es 0.3 €/km.
        -   Tramo 3: Si km > 800, la tarifa es 0.2 €/km.
    -   La estructura if-elif-else es perfecta para esto.
    -   Cálculo final: coste_total = kilometraje * tarifa_aplicada.

3.  Salida:
    -   El coste total del billete.
        -   Identificador: coste_total
        -   Tipo: Real (float)
"""

# --- NORMA 2: DECLARACIONES Y CONSTANTES ---
TARIFA_CORTA = 0.5
TARIFA_MEDIA = 0.3
TARIFA_LARGA = 0.2

# --- NORMA 3: INICIO ---
# Inicio
print("\n--- Calculadora de Coste de Billetes 'Santa Rita' ---")
km_str = input("Introduzca el kilometraje del recorrido: ")
kilometraje = float(km_str)
coste_total = 0.0 # Inicializamos la variable

# Proceso para determinar la tarifa y calcular el coste
if kilometraje <= 0:
    print("Error: El kilometraje debe ser un número positivo.")
elif kilometraje <= 500:
    coste_total = kilometraje * TARIFA_CORTA
    print(f"Se aplica la tarifa de {TARIFA_CORTA} €/km para distancias cortas.")
elif kilometraje <= 800: # Python sabe que ya es > 500 por el 'elif' anterior
    coste_total = kilometraje * TARIFA_MEDIA
    print(f"Se aplica la tarifa de {TARIFA_MEDIA} €/km para distancias medias.")
else: # Si no es <= 500 y no es <= 800, por lógica, tiene que ser > 800
    coste_total = kilometraje * TARIFA_LARGA
    print(f"Se aplica la tarifa de {TARIFA_LARGA} €/km para distancias largas.")

# Salida (solo si el coste es mayor que 0)
if coste_total > 0:
    print(f"El coste total del billete es: {coste_total:.2f} euros.")

# Fin
# --- NORMA 3: FIN ---