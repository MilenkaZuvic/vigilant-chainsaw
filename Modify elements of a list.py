#-------------------------------------------------------------------------------
# Name:        módulo2
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

# Modificar elementos de una lista
Lista = [30,50,21,-39,0]
i = 0
for x in Lista:
    Lista[i] = x + 1
    i = i + 1
print(Lista)

ListaC = ['abc', 'def', 'ghi', 'jkl']
i = 0
for x in ListaC:
    ListaC[i] = x + '-p'
    i = i + 1
print(ListaC)

#Modificamos la posicion de la lista de 2 en 2
for i in range(0, len(ListaC), 2):
    ListaC[i] = "python"
print(ListaC)