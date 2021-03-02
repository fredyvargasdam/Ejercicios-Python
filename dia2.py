#----------------------------------------CONDICIONALES
#Ejercicio con entrada de datos extenso
print("Por favor ingresa tu edad")
edad=input()

def edad_alumno(num):
    if(num>18):
        return "Mayor de edad"
    else:
        return ("el chavon es menor ded edad")

print(edad_alumno(int(edad)))

#Ejercicio con entrada de datos mas facil
print("Ingresa tu nota")
nota=input()

def edad_alumno_version2 (num2):
    return "Aprobado" if num2 > 5 else "Suspenso"

print(edad_alumno_version2(int(nota)))

#Ejercicio con entrada de datos mas facil y ademas con multiple condicion
edad= int(input("Ingresa tu edad "))

def edad_alumno_version3 (num2):
    return "Edad Correcta" if 0<num2<100 else "Edad incorrecta"

print(edad_alumno_version3(edad)) 

#Bucle "for" ejemplo (f es una anotacion especial para concatenar cadenas)
for i in "marquitos":
    print(f"El valor de i es {i}")

#Bucle "While" ejemplo tipo como lo haciamos en clase
edad=int(input("Ingresa tun edad: "))
while(edad<0):
    edad=int(input("Vuelve a ingresar tu edad: "))
print("La edad es correcta, asi que continuaremos con el alta")

#----------------------Contruir objetos iterables
#Esta funcion devolvera una lista de numeros pares utilizando el constructor "yield" ¡incluye el limite!
def numeros_pares(limite):
    
    for indice in range (1,limite+1):
        
            yield indice*2
       
pares=numeros_pares(5)
for numero in pares:
    print(numero)

#Imprimnir un trozo de codigo (GENERADOR)
print(next(pares))
print("Este es el quinto numero")
print(next(pares))

#-------------------------------------EXCEPCIONES
#Esta funcion se encargará de dividir dos datos
while True:
    try:
        dato1=int(input("Primer numero: "))
        dato2=int(input("Segundo numero: "))
        break
    except ValueError:
        print("El dato introducido es incorrecto")

def divide(dato1,dato2):
    try:
        return dato1/dato2
    except ZeroDivisionError:
        print("La division no ha sido resolvida")
        return "Operacion erronea"
print(divide(dato1,dato2))

#Lanzamiento de una excepcion propia. Ejm
nota=int(input("Ingresa la nota del alumno: "))

def nota_alumno(nota):
    if nota<0:
        raise TypeError("Nota fuera de lugar")
    elif nota<5:
        return "Supendido"
    elif nota<10:
        return "Aprobado"

print(nota_alumno(nota))
