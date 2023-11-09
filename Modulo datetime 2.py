import datetime
#Determinar la fecha del sistema

fecha_actual = datetime.date.today()

print(f"El tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"La fecha actual es {fecha_actual}")
print(f"El año actual es {fecha_actual.year}")
print(f"El mes actual es {fecha_actual.month}")
print(f"El dia actual es {fecha_actual.day}")


#Si se le proporciona una fecha imposible, o en un formato inválido se producirá un error 
fecha_capturada = input("Dime una fecha (dd/mm/aaaa): \n") 
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date() 
print(type(fecha_capturada)) 
print(type(fecha_procesada)) 
print (f"La fecha capturada se transformó a {fecha_procesada}")


#Aritmética de fechas básica
#cant_dias int(input("Dime la cantidad de días a adelantar: \n"))
cant_dias = ""
cant_dias (input(f"Dime la cantidad de días a adelantar respecto a {fecha_procesada}): \n")) 
nueva_fecha = fecha_procesada + datetime.timedelta(days=+ cant_dias)

print (f"Siendo la fecha base (fecha_procesada) y considerando un adelanto de {cant_dias} dias")

print("La nueva fecha es {nueva_fecha}")