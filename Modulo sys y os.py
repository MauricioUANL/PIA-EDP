import os
import sys

#uso del módulo sys

lista = list()
for numero in range(1, 1001):
    lista.append(numero)

consumo_lista = sys.getsizeof(lista)
print (f"La lista tiene {len(lista)} elementos, y tiene un tamaño de {consumo_lista} bytes\n")

tupla = tuple (lista)
consumo_tupla = sys.getsizeof(tupla)
print (f"La tupla tiene (len(tupla)) elementos, y tiene un tamaño de (sys.getsizeof(tupla)) bytes\n")

proporcion = float(consumo_tupla / consumo_lista) * 100

print(f"La versión en tupla de los mismos datos tiene un consumo del {proporcion:.2f}% respecto a la versión en una lista")