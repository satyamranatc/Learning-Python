l = [1,2,3,4,5,2,2,1,4,5]

Element = l[0]
Count = 1

for i in range(1,len(l)):
    if Element == l[i]:
       Count += 1
    print(Element, Count)
    Element = l[i]
