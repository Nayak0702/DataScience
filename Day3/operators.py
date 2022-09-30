# area of circle
from cmath import pi
import math
r = 30
area = pi * r ** 2
print(area)
print (3.24  * 30 * 30)

#area of rectangle
length = 40 
width = 50
area = length * width
print(area)

# Calculating the weight of the object
mass = 30
gravity = 9.18
weight  = mass * gravity
print(weight)

# Calculating the density of the liquid
mass = 50
volume  =5
density = mass/ volume
print(density)


#Comparison Opeartors
print(3<3)
print(3<=2)
print(2>3)
print(3==3)
print(2!=1)
print(2!=2)
print(len("mango")== len("avacado"))
print(len("mango")!=len ("Mango"))
print(len("python")> len("statistics"))
print(len("avacado")< len("Mando"))

print("True == True", True == True)
print("True == False", True == False)
print("False == False" , False == False)


print(True == True)
print(True == False)
print(False == True)
print(False == False)

# is, in , is not , not in 
print('hun 'in 'h')
print('h '  in 'hun')
print('coding' not in 'coding')
print(4 is not 5)
print('Vijetha' in 'Vijetha Nayak')
print('pinky' in 'p')
print( 'o' in 'piky')
#print(4 is  2 ** 2)

# and or questions
print(3>2 and 4>3)
print(1>4 and 1>5)
print(3>3 and 3>2)
print(2>3 and 5>7)

print  (not 3>2)
print(not True)
print( not False)
print(not not True)
print(not not False)

print(not(3>2 and 8<9))

age = int(27)
height = float(165)
complex = 1+2j
print(age, height, complex)

# area of triangle
base = 11
height  = 20 
area = 0.5 * base * height
print( area)

# Perimeter of the traingle
a = 5
b = 20.0
c= 35.8
perimeter = a+b+c
print(perimeter)

# area of rectangle and perimeter
length = 20
width = 50
area = length* width
perimeter = 2 * (length + width)
print(area)
print(perimeter)

#area of circle and circumference of circle
r = 50
area = pi * r ** 2
circumference = 2 * pi * r
print(area)
print(circumference)


#To find slope, x-intercept, y-intercept

#SLOPE

A = -2
B = 1
m = -(A/B)
print(m)

# x-intercept
y = 0
C = 2
X = (y-C)/m
print (X) 

# y- intercept
x = 0 
C = -2
y = m * x + C
print(y)

x1, y1, x2, y2 = 2,2,6,10
M = (y2 - y1)/(x2 - x1)
print(M)
print(m == M)

#find the product
x = 9
y = x ^ 2 + 6 * x + 9
print(y)

p = len('python')
q = len('dragon')
print(p)
print(q)
print(p != q)

print('on' in ('python' and 'dragon'))

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in ('python' and 'jargon'))

l = len('python')
print(float(l))
print(str(l))



# number = int(input("Enter a number to check if entered number is even or odd"))
# if number%2 == 0:
#     print("even")
# else:
#     print("not even")
     
h = 7//3
print(h)
print(7/3)

print(int(9.8))

print(type('10')==type(10))

print(int(9.8) == 10)

# Pay per person program
# Hour = int(input("Enter Total hours: "))
# rate = int(input("\n Enter rate per hour wage"))
# pay = Hour * rate 
# print("\n Total pay:", pay)

#Year lived program 
year = int(input("Enter the number f years you have lived"))
seconds = year*365*24*60*60 
print("\n Number of seconds you have lived so far", seconds)


