# S02_Ejemplo_Representacion.py

# --- TEMA: SISTEMAS DE NUMERACIÓN ---
# Python tiene funciones integradas para convertir entre bases numéricas.

numero_decimal = 170

# La función bin() convierte a binario (prefijo '0b')
binary_representation = bin(numero_decimal)
print(f"El número decimal {numero_decimal} es {binary_representation} en binario.") # Salida: 0b10101010

# La función oct() convierte a octal (prefijo '0o')
octal_representation = oct(numero_decimal)
print(f"El número decimal {numero_decimal} es {octal_representation} en octal.") # Salida: 0o252

# La función hex() convierte a hexadecimal (prefijo '0x')
hex_representation = hex(numero_decimal)
print(f"El número decimal {numero_decimal} es {hex_representation} en hexadecimal.") # Salida: 0xaa

# Para convertir de vuelta, usamos int(numero_como_string, base_original)
print(f"El binario 10101010 es {int('10101010', 2)} en decimal.")

print("-" * 20)

# --- TEMA: VALOR, VARIABLE E IDENTIFICADOR ---

# Identificador: El nombre que le damos a nuestra "caja" de memoria. Aquí es 'edad'.
# Variable: La "caja" o espacio en memoria que almacena algo.
# Valor: El dato que guardamos dentro de la "caja". Aquí es 25.
edad = 25
print(f"El identificador 'edad' hace referencia a una variable que contiene el valor {edad}.")

# El valor de una variable puede cambiar con el tiempo.
edad = 26
print(f"Ahora, la misma variable 'edad' contiene un nuevo valor: {edad}.")

print("-" * 20)

# --- TEMA: METODOLOGÍA E-P-S (Entrada-Proceso-Salida) ---
# Usamos un bloque de comentarios para el análisis antes de escribir el código.

"""
ANÁLISIS E-P-S PARA CALCULAR EL ÁREA DE UN RECTÁNGULO

1.  Entrada (Input):
    -   Necesitamos el valor de la base del rectángulo.
        -   Identificador: base
        -   Tipo de dato: Real (float en Python)
    -   Necesitamos el valor de la altura del rectángulo.
        -   Identificador: altura
        -   Tipo de dato: Real (float en Python)

2.  Proceso (Process):
    -   La fórmula para el área es: area = base * altura.

3.  Salida (Output):
    -   El valor calculado del área.
        -   Identificador: area
        -   Tipo de dato: Real (float en Python)
"""
# AHORA IMPLEMENTAMOS EL ANÁLISIS EN CÓDIGO
print("Implementación del Análisis E-P-S:")
# No hay entradas fijas, se piden al usuario.
base_rectangulo = 10.0
altura_rectangulo = 5.0

# Proceso
area_rectangulo = base_rectangulo * altura_rectangulo

# Salida
print(f"El área de un rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es {area_rectangulo}.")
