#1. Max & Min In List 
# l = [10,12,63,4,57,46,72,8,9,10]
# Max = l[0]
# Min = l[0]
# for i in l:
#     if i > Max:
#         Max = i
#     if i < Min:
#         Min = i

# print(Max,Min)


#2. Find a Element Present in List Or Not

# l = [10,12,63,4,57,46,72,8,9,33,4,57,46,72,8,9]
# Search = 4

# found = -1


# for i in range(len(l)):
#     if l[i] == Search:
#         found = i
#         break

# if found == -1:
#     print("Element Not Found")

# else:
#     print("Element Found at Index", found)
    


#3. Find the factors of a Element in List...

# l = [10,12,63,4,57,46,1,2,72,5]
# Elemet = 34

# found = -1
# for i in range(len(l)):
#     if l[i] == Elemet:
#         found = i
#         break

# if found == -1:
#     print("Element Not Found")

# else:
#     print("Element Found at Index", found)
#     for i in l:
#         if Elemet % i == 0 and Elemet != i:
#             print(i,end=", ")

#Unpacking Tuple
t,y = (3,4)
print(t)    
print(y)  


L = [(1,2,3),(4,5,6),(55)]
L = ([1,2,3],[],[])



