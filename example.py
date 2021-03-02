#---------------------------------FUNCIONES
#Funcion de resta
def resta(num1, num2):
    return(num1-num2)
print(resta(4, 8))

#---------------------------------LISTAS
#Funcion que recibe como parametro una lista e imprime el nombre "pepe"
def hombre(nombres):
    indice = 0
    esta = False
    for indice in range(len(nombres)):
        if(nombres[indice] == "Pepe"):
            print("En esta lista hay un chico que se llama pepe")
            esta = True
        indice += 1
    if(esta == False):
        print("No hay nadie que se llame pepe")


nombres = ["Pepe", "Maria", "Pepe maria"]
hombre(nombres)

#Lista el ultimo elemento de la lista
print(nombres[-1])

#Listar solo un trozo de la lista (En este caso tiene como intervalo 0,1)
print(nombres[0:1])

#Imprime la lista con su  posicion(Empieza por 1) y el elemento. Ejm 1 pepe
for indice, nombre in enumerate(nombres, start=1):
    print(indice, nombre)

#Anadir un elemento a la lista
nombres.append("Marcos")

#Anadir una lista a otra
nombres.extend(["Marta","David"])

#Indice de un elemento de una lista
print(nombres.index("David"))

#Comprobar si un elemento se encuentra en una lista
print("Pepe" in nombres)

#Borrar un elemnto de una lista
nombres.remove("Pepe")
print(nombres[:])

#Borrar el ultimo elemento de una lista
nombres.pop()
print(nombres[:])

#---------------------------------TUPLAS
#declaracion de una tupla
mitupla=(1,2,"pepe")
print(mitupla)

#Pasar de una tupla a una lista viceversa
milistatupla=list(mitupla)
mituplaaux=tuple(milistatupla)
print(milistatupla)
print(mituplaaux)

#Formas de buscar un elemnto en una tupla
print("pepe" in mitupla)
print(mitupla.count("pepe"))


