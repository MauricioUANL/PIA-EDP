import math

valorFlotante = float(input("Introduce un valor con fraccion decimal:\n"))

print(f"El siguiente entero hacia abajo de {valorFlotante} es {math.floor(valorFlotante)}")

print(f"El siguiente entero hacia arriba de {valorFlotante} es {math.ceil(valorFlotante)}")

print(f"La parte entera truncada de {valorFlotante} es {math.trunc(valorFlotante)}")
