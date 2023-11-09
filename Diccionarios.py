peliculas={
    10:"The godfather",
    20: "JUrassic Park",
    30: "Ex-Machine",
    40: "The Notebook"
}

print(len(peliculas))
print(peliculas.keys())
print(peliculas.values())


print(peliculas[40])
print(peliculas.get(40))

print(peliculas.items())


print(peliculas)

#Agregar elemento por asignacion
peliculas[50] = "Star Wars"

#Agregar elemento usando update()
peliculas.update({60: "Unknown"})

print(peliculas)

#Actualizar el valor de un elemento
peliculas[60] = "Casino Royal"

print(peliculas)

#Por omisión, se muestran las llaves.
for llave in peliculas:
    print(llave)
    
#Si se desea recuperar los valores, se usa la llave como referencia.
for llave in peliculas:
    print(peliculas[llave])
    

#Se pueden explorar únicamente las llaves
#Leer peliculas.keys(), es lo mismo que
#Leer peliculas
for llave in peliculas.keys():
    print(llave)
    
    
#Se pueden explorar únicamente los valores
for valor in peliculas.values():
    print(valor)
    

#Se pueden explorar las llaves y los valores al mismo tiempo.
for llave, valor in peliculas.items():
    print(f"A la llave {llave} le corresponde el valor {valor}")    


#Demostrando que la simple asignacion no genera una copia.
print(peliculas)
lo_mismo = peliculas
peliculas[80] = "Fifth Element"
print(lo_mismo)
#Ambos datos de variable permiten llegar a los mismos datos de memoria.


peliculas_1 = peliculas.copy()
peliculas_1[90] = "Toy Story"
print(peliculas)
print(peliculas_1)

peliculas_2 = dict(peliculas)
peliculas_2[90] = "Sharknado"
print(peliculas)
print(peliculas_2)