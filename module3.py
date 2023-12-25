#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1a
#Write code using a while loop to look for the highest number in a list of numbers.
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
i = 0
highest_number = mylist[0]
while i < len(mylist):
    if mylist[i] > highest_number:
        highest_number = mylist[i]
    i += 1
print(highest_number)


# In[ ]:


#1b
#Write code using a for loop to look for the lowest number in a list of numbers.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lowest_number = mylist[0]
for element in mylist:
    if element < lowest_number:
        lowest_number = element
print(lowest_number)


# In[ ]:


#2
#Write a simple interactive adding machine.
#This program will continuously ask for input.
#if you enter an integer, it should print a running total of the numbers entered
#if you enter a non-numeric, it should print an error message, but continue running
#if you enter "quit", it should quit out of the loop
#Challenge 1: Can you make it accept negative numbers without causing a ValueError?
#Challenge 2: Can you make it accept floating points as well?

number_sum = 0
    
while True:
    s = input("Enter anything that you like (or enter 'quit' to end):")
    
    if s.lower() == 'quit':
        break
    
    try:  
        number = float(s)
        number_sum += number
        print("The total number is : ", number_sum)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# In[4]:


#3
#Using nested loops (loops within a loop)
#write code to find as many unique pairs of integer numbers whose product is 120(a * b = 120).
#1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120

my_list = [1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120]
for a in my_list:
    for b in my_list:
        if a * b == 120:
            print("Pair:", a, b)


# In[13]:


#4
#Floyd's Triangle is an array of consecutive numbers divided by rows.
#It starts with 1 at the top and each row will have continuing numbers based on their row number.
#Write code to generate the triangle and make it flexible so that it will work with any positive row integer value.
#For example, if you set rows to 5, it should print something like:
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15


row = int(input("Enter the row that you would like to see for Floyd's Triangle"))
curr_row_number = 0
print_value = 0

while curr_row_number < row:
    curr_row_number += 1
    print_count = 0
    
    
    while print_count < curr_row_number:
        print_count += 1
        print_value += 1
        print(print_value , end=' ') 
    
    print()



# In[27]:


#5a
#Filter out strings that contain numbers (use a while or for loop). Example:
#mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]
#Output: ["abc", "def", "ghi"]

mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]

for element in mylist:
    if element.isalpha() :
        print(element)


# In[28]:


#5b
#Write a comprehension version of 5a.

mylist = ["abc", "227b", "99e", "def", "888", "ghi", "JK7"]
result = [element for element in mylist if element.isalpha() ]
print(result)


# In[16]:


#5c
#You are given an arbitrary list of measurements in inches. Write a for loop to convert all numbers to meters.

# 1 inch = 0.00254 meter 

inch_meter = float(0.00254)
list_inch = [3, 7, 10, 17, 50]
for i in list_inch:
    i = i * inch_meter
    print(i)


# In[24]:


#5d
#Write a comprehension version of 5c.

inch_meter = float(0.00254)
list_inch = [3, 7, 10, 17, 50]
inch_convert = [ i * inch_meter for i in list_inch]
print(inch_convert)

