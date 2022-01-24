#-------------------------------------------------------------------------------
# Name:        módulo3
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

# Tabla de Multiplicar

print("Tabla de Multiplicar")
for x in range(1,10):
    print("Tabla del ", x)
    for y in range(1,11):
        print(x, "*", y, " = ", x*y)
    print()