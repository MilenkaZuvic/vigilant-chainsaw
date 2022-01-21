#-------------------------------------------------------------------------------
# Name:        módulo2
# Purpose:
#
# Author:      milen
#
# Created:     21-01-2022
# Copyright:   (c) milen 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# Operaciones de Conjuntos implementadas con Listas

a = [1,2,4]
b = [1,2,3,5]

# Unión -> conjunto con los elementos del Conjunto A y del Conjunto B sin elementos repetidos
aub = list (a)
for ele in b:
    if not ele in aub:
        aub.append(ele)
print("Unión -> ", sorted(aub))

# Intersección -> Conjunto con los elementos comunes en ambos conjuntos
ainterb = []
for ele in b:
    if ele in a:
        ainterb.append(ele)
print("Intersección -> ", sorted(ainterb))

# Diferencia -> A - b, Conjunto con los elementos de A que no esten en B
adifb = list(a)
for ele in b:
    if ele in adifb:
        adifb.remove(ele)
print("Diferencia -> ", sorted(adifb))


# Diferencia Simétrica -> Conjunto con elementos de A que no esten en B y  viceversa
adifSb = list()
for ele in a:
    if not ele in b:
        adifSb.append(ele)
for ele in b:
    if not ele in a:
        adifSb.append(ele)

print("Diferencia Simétrica -> ", sorted(adifSb))

# Super Conjunto -> Se verifica si A esta contenido a B
super = True
for ele in b:
    if not ele in a:
        super = False
        break
if super:
    print("Super Conjunto")
else:
    print("NO Super Conjunto")

# SubConjunto -> Se verifica si A esta contenido en B
sub = True
for ele in a:
    if not ele in b:
        sub = False
        break
if sub:
    print("SubConjunto")
else:
    print("No SubConjunto")

# Disjuntos -> Se verifica que los elementos de ambos conjuntos sean diferentes
disJ = True
for ele in a:
    if ele in b:
        disJ = False
        break
if disJ:
    print("Disjuntos")
else:
    print("NO Disjuntos")
