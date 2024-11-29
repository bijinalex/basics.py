'''
authour-bijin
date-29\11\2024
description-Recursive function to multiply two positive numbers
'''
def positive_multiplication(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+positive_multiplication(num1,num2-1)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
positive_multiplication(num1,num2)
print("multiplication of two numbers is:",positive_multiplication(num1,num2))