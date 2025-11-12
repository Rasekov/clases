# S09_Ejemplos_Otras_Estructuras.py

# --- TEMA: TUPLAS ---
# Son como listas, pero INMUTABLES (no se pueden cambiar una vez creadas).
# Se usan para datos que no deben ser modificados, como coordenadas.

# Creación de una tupla (con paréntesis)
coordenada = (10.5, -4.3)
print(f"Tupla de coordenadas: {coordenada}")

# Se puede acceder a sus elementos como en una lista
print(f"Coordenada X: {coordenada[0]}")

# PERO, si intentas modificarla, dará un error.
# La siguiente línea está comentada porque si no, el programa se detendría.
# coordenada[0] = 5.0  # --> Esto generaría un TypeError

print("-" * 20)

# --- TEMA: CONJUNTOS (SETS) ---
# Son colecciones DESORDENADAS de elementos ÚNICOS.
# Muy útiles para eliminar duplicados o para comprobar pertenencia rápidamente.

lista_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
print(f"Lista original con duplicados: {lista_con_duplicados}")

# Crear un conjunto a partir de la lista elimina los duplicados
conjunto_unico = set(lista_con_duplicados)
print(f"Conjunto creado a partir de la lista: {conjunto_unico}") # El orden no está garantizado

# Operaciones comunes
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Unión (|): Todos los elementos de ambos, sin duplicados
union = conjunto_a | conjunto_b
print(f"Unión de A y B: {union}")

# Intersección (&): Solo los elementos que están en AMBOS conjuntos
interseccion = conjunto_a & conjunto_b
print(f"Intersección de A y B: {interseccion}")

# Diferencia (-): Elementos que están en A, pero NO en B
diferencia = conjunto_a - conjunto_b
print(f"Diferencia (A - B): {diferencia}")

print("-" * 20)

# --- TEMA: DICCIONARIOS ---
# Implementan el concepto de "Registro" o "Estructura".
# Son colecciones de pares clave:valor. Son el tipo de dato más versátil de Python.

# Creación de un diccionario para representar a un estudiante
estudiante = {
    "nombre": "Ana",
    "id": 12345,
    "asignaturas": ["Matemáticas", "Física"],
    "esta_activo": True
}
print(f"Diccionario que representa a un estudiante:\n{estudiante}")

# Acceder a un valor a través de su clave
nombre_estudiante = estudiante["nombre"]
print(f"\nEl nombre del estudiante es: {nombre_estudiante}")

# Añadir un nuevo par clave:valor
estudiante["nota_media"] = 8.9
print(f"Diccionario actualizado con la nota media: {estudiante}")

# Recorrer un diccionario
print("\nRecorriendo las claves y valores del diccionario:")
for clave, valor in estudiante.items():
    print(f"  - Clave: '{clave}', Valor: {valor}")