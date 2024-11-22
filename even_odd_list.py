'''
Authour=bijin
date=22/11/2024
description=Input two lists from the user.
 Merge these lists into a third list such that in the merged list, all even numbers occur first followed by odd numbers.
 Both the even numbers and odd numbers should be in sorted order.
'''
from types import new_class

list1=(22,34,54,12,52,5)
list2=(30,98,29,11,50,2)
print("list1:",list1)
print("list2:",list2)
even_number=[]
odd_number=[]
combined_list=list1+list2
for i in combined_list:
    if i %2 == 0 :
        even_number.append(i)
    else:
        odd_number.append(i)
even_number.sort()
odd_number.sort()
new_list=even_number+odd_number
print("new_list:",new_list)
