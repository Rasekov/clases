# S03_E01_Operadores_y_Normas.py

# --- NORMA 1: IDENTIFICACIÓN DEL PROGRAMA ---
# Programa: S03_E01_Operadores_y_Normas.py
# Descripción: Muestra el uso de operadores aritméticos, entrada/salida y la estructura formal del curso.
# Autor: [Nombre del Estudiante]
# Fecha: [Fecha Actual]

# --- NORMA 2: BIBLIOTECAS, DEFINICIONES Y DECLARACIONES ---
# En Python, no declaramos tipos, pero usamos esta sección para describir las variables.
# Variables a utilizar:
#   - nombre_usuario: Almacena el nombre del usuario (tipo string).
#   - anio_nacimiento: Almacena el año de nacimiento (tipo integer).
#   - anio_actual: Almacena el año actual (tipo integer, constante).
#   - edad: Almacena la edad calculada (tipo integer).

# --- NORMA 3: DELIMITACIÓN (Inicio del programa) ---
# Inicio

print("--- Calculadora de Edad Simple ---")

# --- ENTRADA (Input) ---
# La función input() SIEMPRE devuelve un texto (string).
nombre_usuario = input("Por favor, introduce tu nombre: ")
anio_nacimiento_str = input("Introduce tu año de nacimiento: ")

# --- PROCESO ---
# Es CRUCIAL convertir el texto a número antes de operar.
# Esto se llama "Type Casting" (Conversión de tipo).
anio_nacimiento = int(anio_nacimiento_str)
ANHO_ACTUAL = 2025 # Usamos una variable como si fuera una constante

# Aquí se aplican los operadores aritméticos.
edad = ANHO_ACTUAL - anio_nacimiento

# --- SALIDA (Output) ---
# La función print() muestra los resultados en la pantalla.
print(f"Hola, {nombre_usuario}.")
print(f"Si estamos en {ANHO_ACTUAL}, tu edad es o será de {edad} años.")

# Ejemplo de otros operadores:
# // (división entera) y % (módulo/resto)
print(f"Tu edad dividida entre 10 es {edad // 10} con un resto de {edad % 10}.")

# ** (exponenciación)
print(f"Tu edad al cuadrado sería {edad ** 2}.")

# Fin
# --- NORMA 3: DELIMITACIÓN (Fin del programa) ---