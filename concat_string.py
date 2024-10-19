'''
Authour:bijin
date:19-10-2024
Description: Python program that performs the following tasks:

   1.Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

   2. Concatenate the two strings with a space in between and store the result in a new variable.

   3. Print the concatenated string.

   4. From the concatenated string:
                                      '''


first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
name=first_name+" "+last_name
print(name)
first_name_length=len(first_name)
print(first_name_length)
extracted_first_length=name[:first_name_length]
print(extracted_first_length)
