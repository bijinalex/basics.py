'''
authour=bijin
date=22/11/2024
description=Program to construct patterns of stars (*), using a nested for loop.
'''

#Increasing Triangle
row=int(input("Enter the number of rows:"))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end=" ")
    print(' ')

#Decreasing triangle
row1=int(input("Enter the number of rows:"))
for k in range(row1,0,-1):
    for l in range(k,0,-1):
        print("*", end=" ")
    print('')

#Hill pattern
row2=int(input("Enter the number of rows:"))
for i in range (1,row2+1):
    for m in range(row2-i):
        print(" ", end=" ")
    for n in range(2 * i-1):
        print("*",end=" ")
    print('')

# Reverse Hill Pattern
row3=int(input("Enter the number of rows:"))
for i in range(row3,0,-1):
    for o in range(row3-i,0,-1):
        print(" ", end=" ")
    for p in range(2* i-1):
        print("*", end=" ")
    print('')
