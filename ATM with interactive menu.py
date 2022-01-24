#-------------------------------------------------------------------------------
# Name:        módulo5
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
# Cajero Automático con menú interactivo

from random import randrange

saldo = randrange(0,5000000)

print("*** Bienvenido al Cajero Automático ***")
while True:
    print("\nOperaciones disponibles")
    print("\n1. Saldo")
    print("2. Retiro")
    print("3. Depósito")
    print("0. Salir")

    opcion = int(input("Elija operación a realizar entre 0..3: "))
    if opcion in range(4):
        if opcion == 1:
            print("Su saldo es: ", saldo)
        elif opcion == 2:
            monto = int(input("Indique el monto a retirar: "))
            if monto > saldo:
                print("Operación invalida, saldo insuficiente")
            else:
                saldo = saldo - monto
                print("Operación exitosa")
                print("Su saldo actual es: ", saldo)
        elif opcion == 3:
            monto = int(input("Indique el monto a depositar"))
            saldo = saldo + monto
            print("Su saldo actual es: ", saldo)
        else:
            print("Hasta luego...")
            break
    else:
        print("La opción seleccionada no esta disponible")
