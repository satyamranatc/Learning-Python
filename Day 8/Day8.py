# Data Structures In Python:
# 1. List
# 2. Tuple
# 3. Dictionary
# 4. Set
# -----------------------------------

#List -> Collection Of Elements of any type....

nums = [4,2,3,2,4,5,6,7,5,4,3]
print(len(nums)) # Total number of elements In List


print(nums[0])      # The First Element Of List...
print(nums[-1])     # The Last Element Of List...
print(nums[1:5])    # The Second Element To The 4th Element...
print(nums[3:])     # The Second Element To The Last Element...
print(nums[:4])     # The 0th Element To The 4th Element...
print(nums[0:7:2])  # The 0th Element To The 7th Element with Gap Of 2...
print(nums[-1::-1]) # Reverse

print("-------------------------------")

# Len = len(nums)
# for i in range(Len):
#     print(nums[i], end= " | ")

# In This Loop We Will Get Directly The Element Insted Of Index...
# for i in nums:
#     print(i, end= " | ")


# Using List Function....

# l = list([1,2,3,4])
# print(l) 

# l = list(range(5,501,25))
# print(l)



# Using List Methods....

l = [1,2,3,4]
print(l)

#1. Appemd-> Will add a new element to the list in last position

l.append(5)
print(l)

#2. Insert-> Will add a new element to the list at given position
l.insert(3,500)
print(l)


#Remove -> Will Romove a Specific Element...
l.remove(500)
print(l)

#Pop -> Will Romove a Specific Element by Index, By Default The Last...
RemovedElement = l.pop(3)
print(l)



#Clear -> Will Clear The List...
# l.clear()
# print(l)


#Copy -> Will Copy The List...
x = l.copy()
print(x)

#Reverse -> Will Reverse The List...
l.reverse()
print(l)

#Sort -> Will sort The Elements in a Order
a = [3,3,5,3,2,2,1]
a.sort()
# a.sort(reverse=True)
print(a)



















