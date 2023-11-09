#Declara un diccionario vacio, de nombre asistentes.
Asistentes={}

#Agregar los elementos existentes.
Asistentes.update({"1234":["1234","Juan",100.00]})
Asistentes.update({"2345":["2345","María",400.00]})
Asistentes.update({"3456":["3456","Brenda",350.00]})

print(Asistentes)

#Menu general del programa.
print("\nMenu de opciones:")
print("\t[A] Agregar")
print("\t[B] Buscar")
print("\t[E] Eliminar elemento")
print("\t[M] Modificar elemento")
print("\t[V] Ver datos")
print("\t[Q] Quitar todos los elementos de la lista")
print("\t[S] Salir")

while True:
    opcion = input("\n¿Qué deseas hacer?")
    
    #Valida si se capturó una opcion valida.
    if (not opcion.upper() in "ABEMVQS"):
        print("Opcion no valida, intenta de nuevo")
        continue
    
    #Opcion: Salir
    if (opcion.upper() == "S"):
        print("Fin de la ejecución.")
        break
    
    #Opcion: Agregar asistente
    if (opcion.upper() == "A"):
        socio = input("Numero de socio a agregar: ")
        
        if Asistentes.get(socio) == None:
            nombre = input("Nombre del socio: ")
            aportacion = float(input("Aportacion: "))
            Asistentes.update({socio:[socio,nombre,aportacion]})
            print("Asistente agregado.")
        else:
            print("Asistente encontrado. No se puede repetir.")
            
    
    #Opcion: Buscar asistente.
    if (opcion.upper() == "B"):
        socio = input("Numero de socio a buscar: ")
        recuperado = Asistentes.get(socio)
        if recuperado == None:
            print("Asistente no encontrado.")
        else:
            print(f"{recuperado[0],{recuperado[1]},{recuperado[2]}}")
            
    #Opcion: Eliminar asistente
    if (opcion.upper() == "E"):
        socio = input("Numero de socio a eliminar: ")
        if Asistentes.get(socio) == None:
            print("Asistentes no encontrado. No se puede eliminar.")
        else:
            Asistentes.pop(socio)
            print("Asistentes eliminado.")
    
    #Opcion: Modificar asistente
    if (opcion.upper() == "M"):
        socio = input("Numero de socio a modificar: ")
        recuperado = Asistentes.get(socio)
        if recuperado == None:
            print("Asistentes no encontrado. No se puede medificar")
        else:
            print(f"Datos actuales: {recuperado[0],{recuperado[1]},{recuperado[2]}}")
            nombre = input("Nuevo nombre del socio: ")
            aportacion = float(input("Nueva aportacion: "))
            Asistentes.update({socio:[socio,nombre,aportacion]})
            print("Asistentes modificado.")
            
    #Ver diccionario
    if (opcion.upper() == "V"):
        acumulado = 0.0
        print(f"Elementos en la lista: {len(Asistentes)} ")
        for v in Asistentes.values():
            print(f"{v[0]},{v[1]},{v[2]}")
            acumulado += v[2]
        print(f"Acumulado: ${acumulado:,.2f} ")