# Loop --> Used For Repeating The Task:
 # 1. While Loop
 # 2. For Loop

# --------1. For loop--------
# for i in range(10): # From 0 --- 9
#     print(i,end="")


# User Input:
# a = int(input("Enter the number of times to repeat:- "))
# for i in range(a): # From 0 --- a-1
#     print(i,end="")


# Start End Gap:
# for i in range(4,50,4):
#     print(i,end=",")


# Practice of For loop:
#  1. Sum Of All Natural Numbers till n..

# n = int(input("Enter a Number: -"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i 
# print(sum)   




#  2. Multiply Of All Natural Numbers till n...
# n = int(input("Enter a Number: - "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i 
# print(fact)



# 3.Swaing Variable with loop If Nedded..
# start = int (input("Enter a Start: -"))
# end = int (input("Enter a End: -"))

# if start > end:
#     temp = end
#     end = start
#     start = temp

#     #We can do this also for swaping:
#     # start,end = end,start

# for i in range(start,end+1):
#     print(i,end=",")




# 4. Printng The Value in reversed order if needed...
# start = int (input("Enter a Start: -"))
# end = int (input("Enter a End: -"))

# if start > end:
#     for i in range(start,end, -1):
#         print(i,end=",")

# else:
#     for i in range(start,end+1):
#         print(i,end=",")


#5 If Inside For...
        
start = int (input("Enter a Start: -"))
end = int (input("Enter a End: -"))

for i in range(start,end+1):
    if i % 7 == 0:
        print(i,end=",")







