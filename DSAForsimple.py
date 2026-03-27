"""

This the start of the dsa journey



"""

# print("Cheking Github")



"""
q. Is the number is odd or even.

"""

# n = int(input("Enter your Number : "))

# if (n%2==0):
#     print("even")

# else:
#     print("odd")



"""
q. Sum of numbers from 1 to N

"""

# n = int (input("Enter your number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i

# print(sum)



"""

q. Is number prime or not.

"""
# n = int(input("Enter your number: "))

is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Its a prime number")
else:
    print("Its not a prime number")

"""
how to use arry.

"""

marks = []

for i in range (3):
    m = int(input("Enter your Marks: "))
    marks.append(m)


print (marks)

"""
position of arry

"""

marks =[12,13,14,15,22,55,33,66]

print(marks[4])
marks[4]=59
print(marks)


"""
N-th Tribonacci Number

"""

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


n = int(input("Enter n: "))
print(tribonacci(n))


"""
Power of 2

"""
n = int(input("Enter your number: "))

if n<= 0:
    print("This is not power of 2")

else:
    while n%2 == 0:
        n = n//2

    if n==1:
        print("Its power of 2")

    else:
        print("Its not power of 2")


# //// recursion///

def poweroftwo(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n % 2 != 0:
        return False
    return poweroftwo(n//2)

n = int(input("Enter number: "))
print(poweroftwo(n))


"""
the power of 3

"""

def thepowerofthree(n):
    if n<= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    
    return thepowerofthree(n // 3)

n = int(input("Enter number: "))
print(thepowerofthree(n))


