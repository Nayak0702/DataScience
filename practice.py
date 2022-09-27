#Program No.1
nums = [1,2,3]
for i in range(1,3):
    nums[i-1]= nums[i]
for i in range(0,3):
    print(nums[i],end="")

#Program No.2
for k in range(1,3):
    print(k)
    
num = (1,2,4,3,8,9)
for i in range(0, len(num),2):
    print(num[i])

# Program No.3
from os import popen
import random
print("Generate the seeded randm number")
print(random.Random().random())
print(random.Random(0).random())
print("Generate the float number between 0 and 1")
print(random.random())


# program No.4
import random
numm = [1,2,3,4,5]
print("original list")
print(numm)
random.shuffle(numm)
print("shuffled list")
print(numm)
words=['Green','Blue','Red','Purple','Black']
print("original list")
print(words)
random.shuffle(words)
print('shuffled words list')
print(words)


#Program No. 5
import random
print("Random generated float numbers btn 0 and 1")
print(random.uniform(0,1))
print("Random float numbers of any range")
random_float = random.uniform(1.0,3.0)
print(random_float)

# Program No. 6
import random
print("create a list of random integers")
population = range(1,100)
nums_list = random.sample(population, 10)
print(nums_list)
no_elements = 4
print("\n randoly select" ,no_elements, "multiple items from the said list ")
result_elements = random.sample(nums_list, no_elements)
print(result_elements)
no_elements  = 9
print("\n random elements" ,no_elements,"number of multiple elements from the said list")
result_elements= random.sample(nums_list,no_elements)
print(result_elements)


#Program No.7
import random
print("Generate a random number from 0 and 1")
random.seed(0)
new_random_value = random.random()
print(new_random_value)
print("Genearate the number from o and 1 in random order")
random.seed(1)
new_random_value = random.random()
print(new_random_value)
print("Genarte random numbers from 0 amd 1")
random.seed(2)
new_random_value = random.random()
print(new_random_value)


#Program No. 8  -  Types based programs

import types
def func():
    return 1

print(isinstance(func, types.FunctionType))
print(isinstance(func, types.LambdaType))
print(isinstance(lambda x: x, types.FunctionType))
print(isinstance(lambda x: x,  types.LambdaType))
print(isinstance(max, types.FunctionType))
print(isinstance(max, types.LambdaType))
print(isinstance(abs,types.FunctionType))
print(isinstance(abs,types.LambdaType))


