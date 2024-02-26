# Cout Of Digits:

# num = 4567
# num2 = num
# digits = 0
# for i in range(num):
#     if num == 0:
#         break
#     num = num // 10
#     digits+=1

# print("Total Digits in", num2,"Is - ", digits)


#..........Same Question With While...........


# num = 456377
# num2 = num

# digits = 0
# while num > 0:
#     num = num // 10
#     digits+=1
# print("Total Digits in", num2,"Is - ", digits)


#..........ArmStrong With While...........

num = 345
num2 = num
digits = 0
while num > 0:
    num = num // 10
    digits+=1

Sum = 0
num = num2

while num2 > 0:
    Remainder = num2 % 10
    Sum += Remainder ** digits
    num2 = num2 // 10


if Sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
