# S05_Ejemplos_Decisiones.py

# --- TEMA: OPERADORES LÓGICOS Y RELACIONALES ---
edad = 20
tiene_carnet = True

# La condición del 'if' debe evaluarse como True o False.
# 'and' requiere que AMBAS condiciones sean True.
if edad >= 18 and tiene_carnet is True:
    print("1. Puedes conducir un coche solo (edad >= 18 y tiene carnet).")

# 'or' requiere que AL MENOS UNA condición sea True.
if edad < 18 or tiene_carnet is False:
    print("2. No puedes conducir un coche solo.")
else:
    print("2. Sí puedes conducir un coche solo.")

# 'not' invierte el valor booleano.
if not tiene_carnet:
    print("3. No tienes carnet, por tanto, no puedes conducir.")

print("-" * 20)

# --- TEMA: ESTRUCTURAS DE DECISIÓN (NORMA 5) ---

# 1. Decisión Simple (if)
# Solo actúa si la condición es verdadera. Si no, no hace nada.
numero = -5
if numero < 0:
    print(f"El número {numero} es negativo.")

# 2. Decisión Compuesta (if-else)
# Ofrece dos caminos: uno para True, otro para False.
numero = 10
if numero % 2 == 0: # El módulo % 2 es 0 si el número es par.
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")

# 3. Decisión Anidada o Múltiple (if-elif-else)
# Permite comprobar varias condiciones en orden.
# Es más limpio y eficiente que usar muchos 'if' separados.
nota = 75

if nota >= 90:
    calificacion = "Sobresaliente (A)"
elif nota >= 80:
    calificacion = "Notable (B)"
elif nota >= 70:
    calificacion = "Bien (C)"
elif nota >= 60:
    calificacion = "Suficiente (D)"
else:
    calificacion = "Suspenso (F)"

print(f"Una nota de {nota} corresponde a una calificación de: {calificacion}.")