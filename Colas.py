class Cola:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()
    
    def tamano(self):
        return len(self.items)
 
c=Cola()
c.agregar(4)
c.agregar('perro')
c.agregar(True)
c.tamano()


#Creamos una lista vacía
cola = []
SEPARA = ("-" * 20) + "\n" #Se crea variable para separar cada menú, \n es salto de línea

#Creamos un menú con 4 opciones
def main():
    print("1 Insertar cola")
    print("2 Borrar en cola")
    print("3 Listar cola")
    print("4 Salir")
    print(SEPARA * 1)# Imprime la variable para separar los menús
    option = input("Elija una opcion: ")
    
#Esta opcion permite encolar el numero en la lista

    if str(option)=="1":
        elemento = input(" Introduzca el numero a encolar: ")
        cola.append(elemento)
        print(" numero encolado con exito ")
        main()
        
 #Esta opcion saca de la lista el numero en orden de ingreso

    elif str(option)=="2":
        if len(cola)>0:
            print("El numero: ",cola.pop(0),"fue desencolado")
            main()
    
        else:
            print("Cola vacia")
            main()
        
 #Esta opcion imprime en pantalla la cola
    elif str(option)=="3":
        for i in cola:
            print("cola: ",i)
            main()
            
 #Esta opcion permite salir de la ejecucion del codigo

    elif str(option)=="4":
        exit()
    
    else:
        print("Seleccione una opcion valida.")
        main()
        
main()
