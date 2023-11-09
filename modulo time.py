import time

segundos = int(input("Cantidad de segundos esperar:\n"))
time.sleep(segundos)  #Espera por lo menos la cantidad de segundos especificado
print(f"Han transcurrido, por lo menos, {segundos} segundos")

"""Iniciaremos la medicion de un proceso simulado, que esperara 10 veces el tiempo que indicamos en la variable 
segundos de la celda anterior
"""

horaInicial = time.time()

for termino in range(10):
    time.sleep(segundos)

print("proceso simulado concluido!")
duracion = time.time() - horaInicial
print(f"La duracion del proceso simulado fue de {duracion:.4f} segundos")