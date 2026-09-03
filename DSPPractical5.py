import math 
num = 16 
print("Square root:", math.sqrt(num)) 
print("Factorial:", math.factorial(5)) 
print("Power:", math.pow(2, 3)) 
print("Log:", math.log(10))

from functools import reduce 
numbers = [1, 2, 3, 4, 5] 
result = reduce(lambda x, y: x + y, numbers) 
print("Sum using reduce:", result) 

