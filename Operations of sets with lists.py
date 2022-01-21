
# Sets operations implemented with lists

a = [1,2,4]
b = [1,2,3,5]

# Union -> Set with elements of Set A and Set B, with no repetead elements.

aub = list (a)
for ele in b:
    if not ele in aub:
        aub.append(ele)
print("Union -> ", sorted(aub))

# Intersection -> Sets with common elements in both sets.

ainterb = []
for ele in b:
    if ele in a:
        ainterb.append(ele)
print("Intersection -> ", sorted(ainterb))

# Diference -> A - B, Sets with elements of A that are not in B.

adifb = list(a)
for ele in b:
    if ele in adifb:
        adifb.remove(ele)
print("Diference -> ", sorted(adifb))


# Simetric Diference -> Sets with elements of A that are not in BConjunto con elementos de A que no esten en B and vice-versa

adifSb = list()
for ele in a:
    if not ele in b:
        adifSb.append(ele)
for ele in b:
    if not ele in a:
        adifSb.append(ele)

print("Simetric Diference -> ", sorted(adifSb))

# Super Set -> Check if A contains B
super = True
for ele in b:
    if not ele in a:
        super = False
        break
if super:
    print("Super Set")
else:
    print("NO Super Set")

# Sub-Set -> Check if A is contained in B

sub = True
for ele in a:
    if not ele in b:
        sub = False
        break
if sub:
    print("Sub-Set")
else:
    print("NO Sub-Set")

# Disjoint -> Verified that the elements of the two sets are different

disJ = True
for ele in a:
    if ele in b:
        disJ = False
        break
if disJ:
    print("Disjoint")
else:
    print("NO Disjoint")
