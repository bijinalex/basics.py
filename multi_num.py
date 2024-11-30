'''
author-bijin
date-30\11\2024
description-Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''

def mul_of_list(list):
    mul=1
    for i in list:
        mul=mul*i
    print(mul)
list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    b=int(input("Enter the element: "))
    list.append(b)
mul_of_list(list)