# S10_Ejemplos_Funciones.py

# --- TEMA: SUBPROGRAMAS (FUNCIONES) ---
# Una función es un bloque de código reutilizable que realiza una tarea específica.

# --- Definición de una Función ---
# 'def' es la palabra clave para definir una función.
# 'nombre', 'edad' son los PARÁMETROS FORMALES (los nombres que la función usa internamente).
# La anotación de tipo (ej. nombre: str) es opcional pero es una buena práctica.
def generar_saludo(nombre: str, edad: int) -> str:
    """
    Esta es una docstring. Explica lo que hace la función.
    
    Genera un saludo personalizado basado en un nombre y una edad.
    Retorna (returns) una cadena de texto (string).
    """
    # Proceso de la función
    saludo = f"Hola, {nombre}. Tienes {edad} años."
    
    # La palabra clave 'return' envía un valor de vuelta al lugar donde se llamó a la función.
    return saludo

# --- TEMA: DISEÑO DESCENDENTE ---
# Problema: Calcular el área de varios círculos.
# Descomposición:
#   - Tarea 1: Calcular el área de UN círculo (esto será una función).
#   - Tarea 2: Pedir datos y mostrar resultados (esto será el programa principal).

import math

def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    if radio < 0:
        print("Advertencia: El radio no puede ser negativo. Se devolverá 0.")
        return 0 # Devolvemos 0 para radios inválidos
    
    area = math.pi * (radio ** 2)
    return area

# --- Programa Principal ---
# El programa principal se vuelve más simple y legible.
# Solo se encarga de llamar a las funciones.

print("--- Uso de la función 'generar_saludo' ---")
# 'nombre_usuario' y 'edad_usuario' son los PARÁMETROS REALES (los valores que le pasamos).
nombre_usuario = "Carlos"
edad_usuario = 30
saludo_generado = generar_saludo(nombre_usuario, edad_usuario)
print(saludo_generado)

# La podemos reutilizar con otros valores
print(generar_saludo("Laura", 25))

print("\n" + "-" * 20 + "\n")

print("--- Uso de la función 'calcular_area_circulo' (Diseño Descendente) ---")
# Invocamos la función varias veces
radio1 = 5
area1 = calcular_area_circulo(radio1)
print(f"El área de un círculo de radio {radio1} es {area1:.2f}")

radio2 = 10
area2 = calcular_area_circulo(radio2)
print(f"El área de un círculo de radio {radio2} es {area2:.2f}")

# Ejemplo con un valor inválido
radio3 = -4
area3 = calcular_area_circulo(radio3)
print(f"El área de un círculo de radio {radio3} es {area3:.2f}")