# S01_Ejemplo_Logica.py

# --- TEMA: ESTRUCTURAS ALGORÍTMICAS DEL PENSAMIENTO HUMANO ---
# Objetivo: Describir un proceso del mundo real usando las tres estructuras básicas.
# Problema: ¿Cómo llego a clase por la mañana?

# --- 1. SECUENCIA DE ACCIONES ---
# Una secuencia es una serie de pasos que se ejecutan uno tras otro.

print("Inicio del día.")
print("1. Me despierto.")
print("2. Me ducho y me visto.")
print("3. Desayuno.")
print("4. Salgo de casa y voy a la parada del autobús.")

# --- 2. DECISIÓN DE ACCIÓN ---
# Una decisión es una bifurcación en el camino. Se toma una acción SI (if) se cumple una condición.

esta_lloviendo = False # Cambia a True para ver el otro resultado

print("5. Miro por la ventana.")
if esta_lloviendo is True:
    print("   -> Como está lloviendo, cojo el paraguas.")
else:
    print("   -> Como no está lloviendo, no cojo el paraguas.")

# --- 3. CICLO DE ACCIONES ---
# Un ciclo es una acción o conjunto de acciones que se repiten.

minutos_esperando = 0
autobus_ha_llegado = False

print("6. Espero en la parada.")
# Este bucle 'while' simula la espera repetitiva.
while autobus_ha_llegado is False:
    print(f"   -> Minuto {minutos_esperando}: El autobús no ha llegado. Sigo esperando.")
    minutos_esperando = minutos_esperando + 1
    if minutos_esperando == 5: # Simulación: el autobús llega a los 5 minutos.
        autobus_ha_llegado = True

print("7. ¡El autobús ha llegado! Me subo.")
print("8. Llego a la universidad y voy al aula.")
print("Fin del proceso.")