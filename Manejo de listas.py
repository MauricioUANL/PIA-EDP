#Ordenar la lista en si, perdiendo el orden original 

lista_original = [3, 4, 2] 
print(lista_original)

lista_original.sort() 
print(lista_original)

#Obtener una copia ordenada de la lista, conservando la lista original en el orden que ya estaba definida 
lista_original2 = [23, 10, 30, 5] 
lista_ordenada = sorted(lista_original2)

print (f"lista original = {lista_original2}, y la version ordenada es {lista_ordenada}")