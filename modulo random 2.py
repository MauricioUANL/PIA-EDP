import random

#Demostracion de choice() y shuffle()
listaDePrueba = [10, 20, 30, 40, 15, 25, 35, 45]
print(f"La lista de prueba es {listaDePrueba}")

print(f"El valor seleccionado aleatoriamente de la lista anterior es {random.choice(listaDePrueba)}")

random.shuffle(listaDePrueba)
print(f"La lista ya 'peturbada/barajada' es {listaDePrueba}")