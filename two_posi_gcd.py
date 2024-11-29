'''
authour-bijin
date-29\11\2024
description-Recursive function to find the greatest common divisor of two positive numbers.
'''
def gcd(num1,num2):
    if num1 % num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
num1=int(input("Enter the positive number:"))
num2=int(input("Enter the positive number:"))
if num1>0 and num2>0:
    print("The greatest common factor is ",gcd(num1,num2))
else:
    print("Enter a positive number")
gcd(num1,num2)
print("The greatest common factor is ",gcd(num1,num2))