'''
authour=bijin
Description=a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program

Based on the user's choice:

    If they select option 1, prompt them to enter a temperature in Celsius and display the equivalent temperature in Fahrenheit.
    If they select option 2, prompt them to enter a temperature in Fahrenheit and display the equivalent temperature in Celsius.
    If they select option 3, exit the program.

If the user enters an invalid option, display an error message and re-display the menu. The program should continue to display the menu after each conversion until the user chooses to exit.

    fahrenheit = (celsius * 9/5) + 32
    celsius = (fahrenheit - 32) * 5/9

'''






temp=int(input("Enter the temperature:"))
while True:
    print("1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    choice=int(input("Enter the choice :"))
    if choice==1:
        F = (temp * 9 / 5) + 32
        print(F)
    elif choice==2:
        C= (temp - 32) * 5 / 9
        print(C)
    elif choice==3:
        break
    else:
        print("invalid")

