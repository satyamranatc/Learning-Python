# 1. 
# a = 5 # Gloabal (a)

# def Fun():
#     global a # Now The Global a Will Be Updated
#     a = 100
#     print(a)
   
# Fun()
# print(a)


# 2.
# def Fun(a = 0,b = 0):  # Default Parameters
#     print(a+b)
# Fun()

#3. Multiple Arguments:
# sum = 0
# def add(*a):
#     for i in a:
#         global sum
#         sum += i
#     print(sum)
    

# add(4,5)
# add(4,5,3)
# add(4,5)
# add(7,5)


#4. DocString for a Function
# def Fun():
#     """
#         This is a Dummy Function just For Fun:
#         We Not Accepting any arguments
#     """
#     pass
# print(Fun.__doc__)


# 6.Return :- Used To Fetch Out The Data Outside the Function
def Fun():
    x = 100
    return x/2

x = Fun()
print(x)


