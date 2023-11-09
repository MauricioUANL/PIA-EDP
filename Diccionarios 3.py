operaciones_A={
    12922:"Cliente 1",
    27728:"Cliente 2",
    28939:"Cliente 3"
    
}

operaciones_B={
    12922:"Cliente 1",
    73772:"Cliente 4",
    46677:"Cliente 5"
}

#Se tiene operaciones A, y B. Se decide generar un dioccionario C, que contenga la unión de los dos diccionarios.


#De inicio, le proporcionamos todas las entradas de operaciones_A, a operacopnes_C.
operaciones_C = operaciones_A.copy()

#Ahorra barremos operaciones_B, y agregamos en operacipnes_C lo que no esté ahí.
for llave,valor in operaciones_B.items():
    if (not llave in operaciones_C.keys()):
        operaciones_C[llave] = valor
        
print(operaciones_C)
print(len(operaciones_C))
