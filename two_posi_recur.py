'''
authour-bijin
date-29\11\2024
description-Recursive function to add two positive numbers.
'''
def two_positive_number(num1,num2):
    if num2==0:
        return num1
    else:
        return two_positive_number(num1+1,num2-1)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>0 and num2>0:
    print("sum of the two number is:",two_positive_number(num1,num2))
else:
    print("Enter a positive number")
two_positive_number(num1,num2)
