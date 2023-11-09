import datetime
import time

#Creacion de una hora especifica.
hora = datetime.time(10, 20, 30)
print(f"El tipo de objeto de la hora es {type(hora)}")
print(f"La hora es {hora}")
print(f"La hora de {hora} es {hora.hour}")
print(f"El minuto de {hora} es {hora.minute}")
print(f"El segundo de {hora} es {hora.second}")
print(f"El microsegundo de {hora} es {hora.microsecond}")