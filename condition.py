'''
Authour=bijin
Description=find the number is armstrong or not
'''


number=int(input("Enter a number:"))
number1=number
sum_of_digits=0
while (number>0):
    remainder = number%10
    sum_of_digits=sum_of_digits+(remainder**3)
    number=number//10
if number1==sum_of_digits:
    print("it is armstrong number")
else:
    print("it is not armstrong number")