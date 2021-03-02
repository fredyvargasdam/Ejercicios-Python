import random

primo = []
no_primo = []
ganador = True

#Devuelve "True" si el numero es primo
def es_primo(numero):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    return primo

#Rellena 2 Arrays con numeros primos y no primos calculados de forma aleartoria
while len(primo) < 5 or len(no_primo) < 5:
    rdn = random.randint(10, 10000)
    if es_primo(rdn) and not rdn in primo and len(primo) < 5:
        primo.append(rdn)
    elif not rdn in no_primo and len(no_primo) < 5:
        no_primo.append(rdn)

    if ganador and len(primo) == 5:
        print("Ganan los primos: ")
        ganador = False
    elif ganador and len(no_primo) == 5:
        print("Ganan los no  primos: ")
        ganador = False

print("Lista de numeros primos: " + str(primo))
print("Lista de numeros no primos: " + str(no_primo))
