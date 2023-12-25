# 1
#Given the following string:
#s = " Programming Python"
#Write three ways to get the letter "P" using the index operator.
#Write two ways to get the slice, "Python"

s1 = " Programming Python"
print(s1[1])
print(s1[13])
print(s1[1:2])

# 1
#Given the following string:
#s = " Programming Python"
#Write two ways to get the slice, "Python"

s2 = " Programming Python"
print(s2[12:19])
print(s2[-7:])

# 2
#The following string has multiple spaces in around each word:
#"   I am    Programming    Python!       "
#Write code to create a new string with just single spaces in between:
#"I am Programming Python!"

string1 = "   I am    Programming    Python!       "
string1 = string1.strip()
print(string1.replace("    "," "))

#3
#Given the following values:
#length = 5
#width = 2.5
#height = 2.73
#Write an f-string that will produce the following:
#'The box has a length: 5, width: 2.5 and height: 2.73. The volume is: 34.1.'
#Make sure to make your f-string flexible, so if any of the values change, the string output will reflect the changes.
#N.B.: Volume is length * width * height.

length = 5
width = 2.5
height = 2.73
volume = length * width * height
print(f"The box has a length:{length} and height:{height}. The volume is:{volume}")
      
#4
#4.a
#Using only operators ( [ ], =, +, del) change the following list:
#[1, 2, 3, 4, 5, 6, 7, 8]
#to
#[2, 4, 6, 8, 10, 12, 14]
#Note: do not simply set the list to the final state (e.g.: mylist = [2, 4, 6, 8, 10, 12, 14])
#Same as 4a, but use only methods (append(), remove(), etc…)

my_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list1[0] = 2
my_list1[1] = 4
my_list1[2] = 6
my_list1[3] = 8
my_list1[4] = 10
my_list1[5] = 12
my_list1[6] = 14
del my_list1[7]
print(my_list1)


#4
#4.b
#[1, 2, 3, 4, 5, 6, 7, 8]
#to
#[2, 4, 6, 8, 10, 12, 14]
#Same as 4a, but use only methods (append(), remove(), etc…)

my_list3 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list3.remove(1)
my_list3.remove(3)
my_list3.remove(5)
my_list3.remove(7)
my_list3.append(10)
my_list3.append(12)
my_list3.append(14)
print(my_list3)


#5
#The following tuple with string items has some errors:
#t = ('anita', 0, 'brandon', 'chitra', 5, 7)
#Write code to:
# 1. Capitalize the string names (use string methods).
# 2. Remove the numeric items (use either operators or methods)
# 3. Set t to the tuple with the corrections from above.

t = ['anita', 0, 'brandon', 'chitra', 5, 7]
t[0] = t[0].capitalize()
t[2] = t[2].capitalize()
t[3] = t[3].capitalize()
t.pop()
t.pop()
del t[1]
t = tuple(t)
print(t)
