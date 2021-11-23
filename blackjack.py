cartas={ 
    chr(0x1f0a1):11, 
    chr(0x1f0a2):2, 
    chr(0x1f0a3):3, 
    chr(0x1f0a4):4, 
    chr(0x1f0a5):5, 
    chr(0x1f0a6):6, 
    chr(0x1f0a7):7, 
    chr(0x1f0a8):8, 
    chr(0x1f0a9):9, 
    chr(0x1f0aa):10, 
    chr(0x1f0ab):10, 
    chr(0x1f0ad):10, 
    chr(0x1f0ae):10 
} 

import random
def dameCarta(lista):
    carta=random.choice(lista)
    valor=cartas.get(carta)
    return carta, valor

print("valor de cada carta")
print(cartas)

listaCartas=list(cartas.keys())

print("lista entera de cartas")
print(listaCartas)

valorCartasJugador = 0
primeraVez=True
while True:
    jugar = input("Quiere carta S/N: ")
    if (jugar == "S" or jugar == "s"):
        if primeraVez == True:
            carta, valor = dameCarta(listaCartas)
            valorCartasJugador = valorCartasJugador + valor
            print("Ha salido la carta: ", carta, " valor: ", valor, " valorAcumulado: ", valorCartasJugador)
            primeraVez = False
        carta, valor = dameCarta(listaCartas)
        valorCartasJugador = valorCartasJugador + valor
        print("Ha salido la carta: ", carta, " valor: ", valor, " valorAcumulado: ", valorCartasJugador)
    else:
        print("ValorCartasJugador: ", valorCartasJugador)
        break