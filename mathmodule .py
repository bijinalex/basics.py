'''
Authour:bijin
date:18-10-2024
description:a Python program that uses functions from the math module to perform the following operations on a number provided by the user:

    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.

Expected Output:

Enter a number: 5

Square root of 5: 2.23606797749979

Factorial of 5: 120

5 raised to power 2: 25.0
                          '''

import math
number=int(input("Enter the number:"))
square_root=math.sqrt(number)
print("square root of ",number,":",square_root)
factorial=math.factorial(number)
print("factorial",number,":",factorial)
power=math.pow(5,2)
print("power",number,":",power)







