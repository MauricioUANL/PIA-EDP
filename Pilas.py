class Stack: # Creamos la clase Stack
    def __init__(self): # __init__ método que inicializa los atributos del objeto que creamos
        self.items = [] # instancia de la clase para acceder a los atributos y métodos
    
    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
 
    def push(self, item): # # Metodo para insertar elementos a la pila, inicialización en 0
        self.items.insert(0, item)
 
    def pop(self): # Metodo para eliminar el ultimo elemento apilado.
        return self.items.pop(0) # recuerda que un array inicializa en 0
 
    def print_stack(self): # Metodo para mostrar los elementos de la pila
        print(self.items)
pila = Stack() # Creamos una instancia de la pila 
# ingresamos algunos elementos a la pila
pila.push('a')
pila.push('b')
pila.push('c') 
pila.push('d') 
pila.push('e') 
pila.print_stack() # Mostramos los elementos de la pila
pila.pop() # Utilizamos el metodo pop, para eliminar el elemento
pila.print_stack() # Mostramos nuevamente los elementos de la pila
pila.pop() # Utilizamos el metodo pop, para eliminar el elemento
pila.print_stack() # Mostramos nuevamente los elementos de la pila


class Pila: # Creamos la clase
    def __init__(self):# __init__ método que inicializa los atributos del objeto que creamos
        self.items = []
 
    def estaVacia(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
 
    def extraer(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop()
 
    def incluir(self, item): # Metodo para insertar elementos a la pila
        self.items.append(item)
 
s = Pila() # Creamos una instancia de la pila 
s.incluir('hola')
s.incluir('verdadero')
s.incluir(1)
s.incluir('falso')
print(s.extraer())


stack = [] #Creamos una lista vacía, llamada stack
SEPARA = ("-" * 20) + "\n" #Se crea variable para separar cada menú, \n es salto de línea

#Creamos un Menú con 4 opciones
    
def main():
    print("1 Aplilar elemento (entero)")
    print("2 Desapilar elemento")
    print("3 Mostrar pila")
    print("4 Salir")
    print(SEPARA * 1)# Imprime la variable para separar los menús 
    option = input("Elija una opción: ")
    
 #Esta opción permite apilar el numero en la lista
    if str(option)=="1":
        elemento = input(" Introduzca el numero a apilar: ")
        stack.append(elemento)
        print("**- Elemento apilado -**")
        main()
        
 #Esta opción saca desapila a partir del último número ingresado
    elif str(option)=="2":
        if len(stack) == 0:
            print(" No hay elementos para desapilar ")
            main()
        else:
            print("**-El numero: ",stack.pop()," fue desapilado-**")
            main()
        
 #Esta opción imprime en pantalla la pila 
    elif str(option)=="3":
        for i in reversed(range(len(stack))):
            print("Pila: ",stack[i])
            main()
            
 #Esta opción permite salir de la ejecución del Código
    elif str(option)=="4":
        exit()
    else:
        print("\Opción incorrecta.\n")
        main()
        
main()
