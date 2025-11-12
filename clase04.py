# S04_E02_Conversion_Temperatura.py

# --- NORMA 1: IDENTIFICACIÓN ---
# Programa: S04_E02_Conversion_Temperatura.py
# Descripción: Convierte una temperatura de grados Celsius a Kelvin.
# Autor: [Nombre del Estudiante]
# Fecha: [Fecha Actual]

"""
ANÁLISIS E-P-S

1.  Entrada:
    -   Temperatura en grados Celsius.
        -   Identificador: temp_celsius
        -   Tipo: Real (float)

2.  Proceso:
    -   La fórmula es: TK = TC + 273.15
    -   Usaremos una constante para el valor de la conversión.

3.  Salida:
    -   Temperatura en grados Kelvin.
        -   Identificador: temp_kelvin
        -   Tipo: Real (float)
"""

# --- NORMA 2: DECLARACIONES ---
# Constante
VALOR_CONVERSION = 273.15 # Por convención, las constantes se escriben en mayúsculas.

# --- NORMA 3: INICIO ---
# Inicio

print("--- Conversor de Celsius a Kelvin ---")
temp_celsius_str = input("Introduce la temperatura en grados Celsius: ")
temp_celsius = float(temp_celsius_str)

temp_kelvin = temp_celsius + VALOR_CONVERSION

print(f"{temp_celsius}°C equivale a {temp_kelvin} K.")

# Fin
# --- NORMA 3: FIN ---

# -------------------------------------------------------------------

# S04_E01a_Trigonometria.py
# Ejemplo del uso de la biblioteca 'math'

# --- NORMA 1 ---
# Descripción: Calcula la posición final de un punto usando trigonometría.

# --- NORMA 2 ---
import math # Importamos la "caja de herramientas" matemática.

"""
ANÁLISIS E-P-S

1.  Entrada:
    -   Distancia del movimiento (d).
    -   Ángulo del movimiento en grados (angulo_grados).

2.  Proceso:
    -   Las funciones trigonométricas en Python (math.cos, math.sin) usan RADIANES, no grados.
    -   Paso 1: Convertir el ángulo de grados a radianes. Fórmula: rad = grados * (pi / 180)
    -   Paso 2: Calcular el desplazamiento en x: dx = d * cos(rad)
    -   Paso 3: Calcular el desplazamiento en y: dy = d * sen(rad)

3.  Salida:
    -   Las nuevas coordenadas (dx, dy).
"""

# --- NORMA 3: INICIO ---
# Inicio

distancia = 10
angulo_grados = 90

# Proceso
# Paso 1: Convertir grados a radianes. Podemos usar la función de la librería math.
angulo_radianes = math.radians(angulo_grados)
print(f"{angulo_grados} grados son aproximadamente {angulo_radianes:.4f} radianes.")

# Paso 2 y 3: Calcular los desplazamientos
desplazamiento_x = distancia * math.cos(angulo_radianes)
desplazamiento_y = distancia * math.sin(angulo_radianes)

# Salida
# Nota: El resultado para x es un número muy pequeño, cercano a cero (notación científica),
# debido a la precisión de los flotantes. Lo redondeamos para que sea más legible.
print(f"Un movimiento de {distancia}m en un ángulo de {angulo_grados}° resulta en una posición final de ({desplazamiento_x:.2f}, {desplazamiento_y:.2f}).")

# Fin
# --- NORMA 3: FIN ---