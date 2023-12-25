#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 
#Write code to reverse the relationship of a dictionary, so that the keys become the values and the values become the keys. Your code should work for any size of dictionary (i.e., use iteration).  
#For example, given the following dictionary,
#{'a': 1, 'b': 2, 'c': 3, 'd': 4}
#Produce a new dictionary that looks like the following: 
#{1: 'a', 2: 'b', 3: 'c', 4: 'd'} 


result = {}
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for key, val in my_dict.items():
    result[val] = key
   
print(result)


# In[2]:


#2
#Given a string, write code to create a dictionary where:
#the keys are the words
#the values are the count of the words
#Make it so that the keys are case insensitive. You can assume the list contains only strings. 
#For example, given the following string: 
#"A fool thinks himself to be wise, but a wise man knows himself to be a fool" 
#Generate a dictionary that looks like the following (order is not significant) 
#{'a': 3, 'fool': 2, 'thinks': 1, 'himself': 2, 'to': 2,  'be': 2,  'wise': 2,  'but': 1,  'man': 1,  'knows': 1} 

s = "A fool thinks himself to be wise, but a wise man knows himself to be a fool" 
new_s = s.lower()
new_s = new_s.replace(","," ")
new_s = new_s.split()
d = {}
for words in new_s:
    if words not in d:
        d[ words ] = 1 
    else: 
        d[ words ] += 1 
print(d)


# In[3]:


#3
#Write code to combine two dictionaries into one. Assume that the dictionaries have integers as values.
#If a key is found in both dictionaries, add their values together in the new dictionary.
#If a key is found only in one dictionary, keep the value the same. 
#For example, given the following dictionaries: 
#d1 = {'a': 1, 'b': 2, 'c': 3}
#d2 = {'a': 10, 'c': 30, 'f': 50}
#The combined dictionary should look like:
#{'a': 11, 'b': 2, 'c': 33, 'f': 50}

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 10, 'c': 30, 'f': 50}
result = {}
for key in d1:    
    result[key] = d1[key]
    print(result)     

for key in d2:
    if key in d1:
        result[key] = d1[key] + d2[key]
    else:
        result[key] = d2[key]
        
   
    print(result)


# In[4]:


#Given a list of lists containing strings, write code that will create a new list of lists containing the length of each string.
#For example, given the following list of lists:  
#[['C++', 'Java', 'Python', 'Swift'],
#['San Francisco','Berkeley','Oakland'],
#['Apple', 'Banana', 'Cherry', 'Dragonfruit', 'Grape']]
#Produce the output: 
#[[3, 4, 6, 5], [13, 8, 7], [5, 6, 6, 11, 5]]

result = []
my_list = [
    ['C++', 'Java', 'Python', 'Swift'],
    ['San Francisco','Berkeley','Oakland'],
    ['Apple', 'Banana', 'Cherry', 'Dragonfruit', 'Grape']
    ]
for sublist in my_list:
    subresult = []
    for word in sublist:
        word_number = len(word)
        subresult.append(word_number)        
    result.append(subresult)
print(result)


# In[5]:


#5
#Given the following list of dictionaries:
#[{'name': 'Lisa', 'score': 93},
#{'name': 'Jeff', 'score': 85},
#{'name': 'Elon', 'score': 89},
#{'name': 'Satya', 'score': 90},
#{'name': 'Tim', 'score': 82}]
#Write code to calculate the average score.


my_dict = [{'name': 'Lisa', 'score': 93},{'name': 'Jeff', 'score': 85},{'name': 'Elon', 'score': 89},{'name': 'Satya', 'score': 90},{'name': 'Tim', 'score': 82}]
all_value = [entry['score'] for entry in my_dict]
average_value = sum(all_value) / len(all_value)
print(average_value)


# In[6]:


#Write code to print the name of the person with the highest score.

students = [{'name': 'Lisa', 'score': 93},{'name': 'Jeff', 'score': 85},{'name': 'Elon', 'score': 89},{'name': 'Satya', 'score': 90},{'name': 'Tim', 'score': 82}]

best_student = {}
high_score = 0
for student in students:
    if student['score'] > high_score:
        high_score = student['score']
        best_student = student

print(best_student['name'])

