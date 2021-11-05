##Tarea 2 Forulario"
## Función donde ingreso el formulario


def datos_personales():
    lista = []
    informacion_personal= input("Ingresa nombre: ")
    lista += [informacion_personal]
    informacion_personal=input("Ingreso Apellido: ")
    lista += [informacion_personal]
    informacion_personal= input("Ingreso Edad: ")
    lista += [informacion_personal]
    informacion_personal=input("Ingreso Dirección: ")
    lista += [informacion_personal]
    informacion_personal=input("Ingreso email: ")
    lista += [informacion_personal]
    return lista
##LLamo la función  y luego imprimo los datos

m = datos_personales()
print('\n')
print(m)

# 4 operciones de aritmética
# las validaciones de ingreso 
# y despues las operaciones


#Valida si es el primer un número es entero
def lee_entero():
   while True:
       numero1 = input("\nEscriba primer número entero: ")
       try:
           numero1 = int(numero1)
           return numero1
       except ValueError:
           print ("La entrada es incorrecta: escribe un número entero")


#Valida si el segundo número es entero
def lee_entero2():
   while True:
       numero2 = input("\nEscriba segundo número entero: ")
       try:
           # Valida que sea != de 0
           if numero2 == "0":
               print ('Debe ser un número distinto a 0')
           else:
               numero2 = int(numero2)
               return numero2
       except ValueError:
           print ("La entrada es incorrecta: escribe un número entero distinto a 0")
#Se llama a las funciones donde se piden los números
numero_a = lee_entero()
numero_b = lee_entero2()
#Se hacen las 4 operaciones matemáticas con los números ingresados y se imprimen

print(f'\n\nLa multiplicación de {numero_a} * {numero_b} es', numero_a * numero_b)
print(f'La división de {numero_a} / {numero_b} es', numero_a / numero_b)
print(f'La suma de {numero_a} + {numero_b} es', numero_a + numero_b)
print(f'La resta de {numero_a} - {numero_b} es', numero_a - numero_b,end='\n')