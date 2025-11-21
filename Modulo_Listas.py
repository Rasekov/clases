# Modulo_Listas.py
# Módulo con funciones básicas para listas de números reales usando índices

def AgregarValores(lista):
    """
    Pide valores al usuario y los agrega hasta que el usuario presiona Enter.
    Se asume entrada válida.
    """
    while True:
        dato = input("Ingrese un número (Enter para terminar): ")
        if dato == "":
            return lista
        lista.append(float(dato))

def MostrarLista(lista):
    """Muestra la lista elemento por elemento."""
    print("Lista =", lista)

def CalcularMinimo(lista):

    if len(lista) == 0:
        return None #Si la lista esta vacia, devolver None

    minimo = lista[0]

    for i in range(1, len(lista)): #El bucle empieza en 1 porque minimo ya es igual a lista[0]
        if lista[i] < minimo:
            minimo = lista[i]

    return minimo

def CalcularMaximo(lista):
 
    if len(lista) == 0:
        return None #Si la lista esta vacia, devolver None

    maximo = lista[0]

    for i in range(1, len(lista)): #El bucle empieza en 1 porque maximo ya es igual a lista[0]
        if lista[i] > maximo:
            maximo = lista[i]

    return maximo

def CalcularPromedio(lista):

    if len(lista) == 0:
        return None #Si la lista esta vacia, devolver None

    suma = 0

    for i in range(0, len(lista)):
        suma += lista[i]

    return suma / len(lista)
