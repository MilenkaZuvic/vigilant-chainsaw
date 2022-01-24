
# Modify elments of a list
List = [30,50,21,-39,0]
i = 0
for x in List:
    List[i] = x + 1
    i = i + 1
print(List)

#Now we will do the same thing but with a list composed of chains

ListC = ['abc', 'def', 'ghi', 'jkl']
i = 0
for x in ListC:
    ListC[i] = x + '-p'
    i = i + 1
print(ListaC)

#We modify de position of the list 2 by 2
for i in range(0, len(ListC), 2):
    ListC[i] = "python"
print(ListC)
