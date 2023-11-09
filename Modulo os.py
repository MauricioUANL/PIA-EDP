import os
#uso del módulo os
#Tenga presente que la respuesta podrá variar de acuerdo al directorio actual de trabajo. print (f"El directorio actual de trabajo es (os.getcwd()}")

for raiz, dirs, archivos in os.walk(".", topdown=False): 
    for nombre in archivos:
        print(os.path.join(raiz, nombre))

for nombre in dirs:
    print (os.path.join(raiz, nombre))