# VARIABLES
from ast import Compare
from math import pi
from tkinter.messagebox import YES


num_int = 10
print('num_int',num_int)
num_str = str(num_int)
print(num_str)

num_int = 10
num_float = float(num_int)
print(num_int, num_float)

num_str = '20'
num_int = int(num_str)
print(num_str, num_int)

num_float = 10.6
num_int = int(num_float)
print(num_int, num_float)

name = 'Vijetha Nayak'
listing = list(name)
print(listing)

print(list(num_str))

#Exercise
print('''Day 2: 30 Days of python programming''')
First_Name = 'Vijetha'
Last_Name = 'Nayak'
Age = 27
Full_Name = 'Vijetha Nayak'
Country = "India"
City = "Bangalore"
Year = 2022 
is_married = False
is_true = YES
is_light_on = True

First_Name, Last_Name, Age, Full_Name, Country, City, Year, is_married, is_true, is_light_on = 'Vijetha', 'Nayak' , 27, 'Vijetha Nayak', "India", "Bangalore", 2022 , False, YES, True

print(type((First_Name, Last_Name, Age, Full_Name, Country, City, Year, is_married, is_true, is_light_on)))

print(type(First_Name))
print(type(Last_Name))
print(type(Full_Name))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Year))
print(type(is_true))
print(type(is_light_on))
print(type(is_married))

print(len(First_Name))

print(First_Name in Last_Name)
print(First_Name in 'Vijetha')

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
value_diff = num_one - num_two
print(value_diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor = num_one // num_two
print(floor)
print(5*5*5*5)

import math
r = 30
area = 2* pi * r
circumference = pi * r * r
print(area)
print(circumference)

# radius = int(input('Enter the radius'))
# areas = 2 * pi * radius
# print(radius)
# print(areas)

floatt = 10.60 
num_int  = int(floatt)
print(num_int )

first_name = input('Enter first name')
last_name = input( 'Enter last name')
age = int(input('Enter age'))
country = input("Enter Country name")
print(first_name)
print(last_name)
print(age)
print(country) 




