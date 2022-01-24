#-------------------------------------------------------------------------------
# Name:        módulo4
# Purpose:
#
# Author:      milen
#
# Created:     24-01-2022
# Copyright:   (c) milen 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Jugando a adivinar el número

from random import randint

x = randint(1,25)

intentos = 0

#Necesitamos una estructura repetitiva para controlar el numero de intentos
while intentos < 6:
    número = int(input("Elige un número entre 1 y 25 "))
    intentos = intentos + 1
    if número > x:
        print("Tú número esta por encima")
    elif número < x:
        print("Tú número esta por debajo")
    else:
        break

if número == x:
    print("Felicidades... eres un genio...")
    print("Lo lograste en {} intentos".format(intentos))
else:
    print("uy... has perdido, será en otra oportunidad")
