'''
Authour:bijin
Date:18-09-2024
Description:Python program that stores a string in a variable. Extract a specific part of the string (substring) and then concatenate it with another string. Finally, display the new string.
Instructions:

    Assign the string "Hello, World!" to a variable.
    Extract the substring "World" from the string.
    Concatenate this substring with the string " Everyone!".
    Print the final concatenated string.'''



str_var="Hello world"
str_pl=str_var[6:13]

res=str_var=" Everyone! "
print(str_pl+res)
