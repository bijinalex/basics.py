'''
authour-bijin
date-29\11\2024
description-Program to find the factorial of a number using Recursion.
'''
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input("Enter the number:"))
factorial(num)
print("The factorial of ",num,"is",factorial(num))
