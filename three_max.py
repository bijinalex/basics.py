'''
author-bijin
date-30\11\2024
description-A Python function to find the maximum of three numbers.
'''
def max_num(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
max_num(x,y,z)
print("The maximum number is",max_num(x,y,z))