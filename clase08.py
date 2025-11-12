# S08_Ejemplos_Listas_y_Cadenas.py

# --- TEMA: ARREGLOS UNIDIMENSIONALES (LISTAS en Python) ---
# Una lista es una colección ordenada y modificable de elementos.

# Creación de una lista de calificaciones
calificaciones = [8.5, 7.0, 9.8, 5.5, 6.2]
print(f"Lista original de calificaciones: {calificaciones}")

# Acceder a un elemento por su índice (la primera posición es 0)
primera_calificacion = calificaciones[0]
print(f"La primera calificación es: {primera_calificacion}")

# Modificar un elemento
calificaciones[3] = 6.0 # Cambiamos el 5.5 por un 6.0
print(f"Lista con el cuarto elemento modificado: {calificaciones}")

# --- Operaciones comunes sobre listas ---
# 1. Añadir un elemento al final (append)
calificaciones.append(10.0)
print(f"Lista tras añadir un 10.0: {calificaciones}")

# 2. Longitud de la lista (len)
num_calificaciones = len(calificaciones)
print(f"Ahora hay {num_calificaciones} calificaciones en la lista.")

# 3. Recorrer la lista con un bucle 'for'
print("Recorriendo e imprimiendo cada calificación:")
for nota in calificaciones:
    print(f"  - Calificación: {nota}")

# 4. Sumar, encontrar el máximo y el mínimo
suma_total = sum(calificaciones)
nota_maxima = max(calificaciones)
nota_minima = min(calificaciones)
print(f"La suma es {suma_total:.2f}, la máxima es {nota_maxima} y la mínima es {nota_minima}.")

# 5. Ordenar la lista (sort)
calificaciones.sort() # Ordena la lista de menor a mayor
print(f"Lista ordenada: {calificaciones}")

print("-" * 20)

# --- TEMA: ARREGLOS BIDIMENSIONALES (MATRICES) ---
# Se implementan como una lista de listas.

# Matriz de 3x3
matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]
print("Matriz 3x3:")
print(matriz)

# Acceder a un elemento: matriz[fila][columna]
elemento_central = matriz[1][1]
print(f"El elemento en la fila 1, columna 1 es: {elemento_central}")

# Recorrer una matriz con bucles anidados
print("Recorriendo la matriz:")
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(f"  Elemento en ({fila}, {columna}): {matriz[fila][columna]}")
        
print("-" * 20)

# --- TEMA: CADENAS Y FORMATEO con f-strings ---
# Las f-strings son la forma moderna y recomendada de dar formato a cadenas.

nombre = "Guillermo"
asignatura = "Ciencias de la Computación"
nota_media = 8.756

# La 'f' antes de las comillas activa el formateo.
# Las variables van entre llaves {}.
texto_formateado = f"El profesor {nombre} imparte la asignatura de {asignatura}."
print(texto_formateado)

# Se puede controlar el formato de los números.
# {variable:.2f} significa "formatea como un flotante con 2 decimales".
texto_con_nota = f"La nota media del alumno es {nota_media:.2f}."
print(texto_con_nota)

# Incluso se pueden realizar operaciones dentro de las llaves.
cantidad = 5
precio = 10.5
print(f"El total a pagar es: {cantidad * precio}€")