'''
Authour:bijin
Date:19-10-2024
Description:Write a Python program that performs the following tasks:

   User Input:
        Ask the user to enter two numbers, num1 and num2.
        Ask the user to enter a third number, num3.

   1. Addition:
        Add the first two numbers (num1 and num2).
        Print the sum in the format: "The sum of num1 and num2 is: result"

   2.Subtraction:
        Subtract num2 from num1.
        Print the difference in the format: "The difference when num2 is subtracted from num1 is: result"

   3.Multiplication:
        Multiply num1 by num2.
        Print the product in the format: "The product of num1 and num2 is: result"

   4. Division:
        Divide num1 by num2.
        Print the quotient in the format: "The quotient when num1 is divided by num2 is: result"

   5. Modulus:
        Find the remainder when num1 is divided by num2.
        Print the remainder in the format: "The remainder when num1 is divided by num2 is: result"

   6.Combined Arithmetic Operation:
        Perform the following combined operation:
        result = (num1 + num2) * num3 / 2
        Print the result in the format: "The result of (num1 + num2) * num3 / 2 is: result"    '''





num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
sum=(num1+num2)
print("The sum of num1 and num2 is:",sum)
sub=(num2-num1)
print("The difference when num2 is subtracted from num1 is:",sub)
print("The product of num1 and num2 is:",num1*num2)
print("The quotient when num1 is divided by num2 is:",num1/num2)
print("The remainder when num1 is divided by num2 is:",num1%num2)
print("The result of (num1 + num2)* num3/2 is:",(num1 + num2)*num3/2)
