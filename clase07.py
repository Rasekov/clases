# S07_Ejemplos_Ciclos.py

# --- TEMA: REPETICIÓN INDEXADA (CICLO for) ---
# Se usa cuando sabemos cuántas veces queremos repetir una acción.

# La función range() es la herramienta principal.

# Caso 1: range(stop) -> desde 0 hasta stop-1
print("Contando del 0 al 4 con range(5):")
for i in range(5):
    print(f"  Iteración número {i}")

# Caso 2: range(start, stop) -> desde start hasta stop-1
print("\nContando del 1 al 5 con range(1, 6):")
for i in range(1, 6):
    print(f"  Número {i}")

# Caso 3: range(start, stop, step) -> desde start hasta stop-1, saltando 'step'
print("\nContando los números pares del 2 al 10 con range(2, 11, 2):")
for i in range(2, 11, 2):
    print(f"  Número par: {i}")

print("-" * 20)

# --- TEMA: REPETICIÓN CONDICIONADA (CICLO while) ---
# Se usa cuando la repetición depende de una condición que puede cambiar.

print("Ejemplo de menú interactivo con 'while':")
opcion = ""

# El bucle se ejecutará MIENTRAS la opción no sea '3'.
while opcion != "3":
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola! Gracias por elegir la opción 1.")
    elif opcion == "2":
        print("¡Adiós! Gracias por elegir la opción 2.")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

print("Fin del bucle while.")