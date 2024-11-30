'''
authour-bijin
date-30\11\2024
description-Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''
def sum(list):
    sum=0
    for i in list:
        sum +=i
    print(sum)
list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    b=int(input("Enter the element: "))
    list.append(b)
sum(list)