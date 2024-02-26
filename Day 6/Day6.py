#..........Prime Numbers........

# num = 17616765765747326
# isPrime = True

# for i in range(2,num):
#     if num % i == 0:
#         isPrime = False
#         break


# if isPrime == True:
#     print(num, "is a prime number")
# else:
#     print(num, "is Composite number")       

# ----------------------------------------------------------------
# Nested For Loop...

# for a in range(10):
#     for i in range(5):
#         print(a,i)
#     print("\n------------")

# ........Table In a Range......

# for i in range(2,21):
#     for j in range(1,11):
#         print(i, "x",j, "=",i*j)
#     print("---------------")

# ---------------Star Patterns------------------------------------------

"""
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
# n = int(input("Enter a number:- "))

# for i in range(n):
#     for j in range(n):
#         print("* ",end="")
#     print()


# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# n = int(input("Enter a number:- "))

# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()



# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# n = int(input("Enter a number:- "))
# for i in range(n):
#     for j in range(i,n):
#         print("* ",end="")
#     print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# # * 
# n = int(input("Enter a number:- "))
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print()

# for i in range(n):
#     for j in range(i,n-1):
#         print("* ",end="")
#     print()


#           * 
#          * * 
#         * * * 
#        * * * * 
#       * * * * * 

n= int(input("Enter a number:- "))
for i in range(n):

    for j in range(i,n):
        print(" ",end="")

    for k in range(i+1):
        print("* ",end="")

    print()




