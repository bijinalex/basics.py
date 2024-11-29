'''
author-bijin
date-29/10/2024
description- check whether the given number is a valid mobile number or not using functions.
'''
from operator import truediv


def mobile_number(number):
    num_length=len(number)
    if num_length==10 and number[0] in "987":
        print("number is valid")
    else:
        print("number is not valid")
no=input("Enter the number:")
mobile_number(no)