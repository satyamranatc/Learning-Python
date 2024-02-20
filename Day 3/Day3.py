# Write a Python program using an if-else statement to check if a number is positive,
# negative, or zero


# print("Enter a number: ")
# num = int(input())

# if(num > 0):
#     print("Number Is Positive")

# if (num == 0):
#     print("Number Is Zero")

# else:
#     print("Number Is Negative")




# Write a Python program using an if-else statement to check if a number is divisible by
# 2 and then for 3
# print("Enter a number: ")
# num = int(input())

# if(num % 2 == 0):
#     print("Number divisible by 2")
#     if(num % 3 == 0):
#         print("Number divisible by 3")

# else:
#     print("Number is not divisible by 2")

# try the same program with else if and multiple if



#Check IF A Person id eligible for dirving or not.
    
age = int(input("Enter your age: "))

if age>100 or age < 1:
    print("Invalid age")

elif age >= 18:
    print("You can drive")
    if age>70:
        print("Drive Care Fully")
        
elif age >= 10:
    print("You can ride a cycle")

else:
    print("You can't drive")


