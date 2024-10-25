'''
Authour:bijin
Description=A Python program to convert temperature values back and forth between Celsius and Fahrenheit.
 The user should be able to input a temperature in Celsius or Fahrenheit,
  and the program should convert it to the other unit using the formula:
c/5=f−32/9

    For Celsius to Fahrenheit conversion:
    f=(9/5×c)+32

    For Fahrenheit to Celsius conversion:
    c=5/9×(f−32)
'''


temp=int(input("Enter temperature:"))
unit=str(input("Is this in (C)elsius or (F)ahrenheit?",))
F=(9/5*temp)+32
if unit=='C':
    print(temp,"Celsius is",F,"(F)ahrenheit")
else:
    g=(5/9*(temp-32))
    print(temp,"Fahrenheit is",g,"(C)elsius")
