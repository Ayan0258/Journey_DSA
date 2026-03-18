# """

# This the start of the dsa journey



# """

# print("Cheking Github")



# """
# q. Is the number is odd or even.

# """

# n = int(input("Enter your Number : "))

# if (n%2==0):
#     print("even")

# else:
#     print("odd")



# """
# q. Sum of numbers from 1 to N

# """

# n = int (input("Enter your number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i

# print(sum)



"""

q. Is number prime or not.

"""
n = int(input("Enter your number: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Its a prime number")
else:
    print("Its not a prime number")