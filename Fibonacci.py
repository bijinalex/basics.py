'''
authour:Bijin
date:6\12\2024
description:Program to define a module to find Fibonacci Numbers and import the module to another program.
'''
def fibonacci(num):
    lst=[0]
    num1=0
    num2=1
    for i in range(num-1):
        lst.append(num2)
        num1,num2=num2,num2+num1
    return lst
