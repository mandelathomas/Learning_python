"""
Knowing about range

----- defining a range---
What is a range
In Python, the range() function generates sequences of numbers within a specified range.

"""


asvas_score = range(10)
print(asvas_score)

 #check the function type
type(asvas_score)

 #converting a range to a list
list(asvas_score)

 #slicing a range by using the list() function first
list(asvas_score)[2:5]

#looping over a range
for asvas_score in range(6, 20):
  print(asvas_score)

  #Execise tast

  #Considering the code below, what is the result of a[3] ?

num = range(10, 30, 3)
mylist =list(num)
print(mylist)
mylist[3]
