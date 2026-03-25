# ///gcd//HCF///


# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)

# print(gcd(15,125))

# //lcm//

# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)

# def lcm(a,b):
#     return a*b//(gcd(b,a%b))


# print(gcd(15,50))
# print(lcm(15,50))

"""
Power of (x,n)

"""

def thepowerof(x, n):
    if n == 0:
        return 1
    half = thepowerof(x, n //2 )

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
    
x = int(input("Enter base: "))
n = int(input("Enter power: "))

print(thepowerof(x,n))