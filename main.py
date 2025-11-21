# Programa MaxMinFloatList
# Ejemplo de uso de Modulo_Listas

import Modulo_Listas as ml

# Variables
lista = []

# Pedir valores
lista = ml.AgregarValores(lista)

# Mostrar la lista
ml.MostrarLista(lista)

# Mostrar mínimo
print("Mínimo =", ml.CalcularMinimo(lista))

# Mostrar máximo
print("Máximo =", ml.CalcularMaximo(lista))

# Mostrar promedio
print("Promedio =", ml.CalcularPromedio(lista))
