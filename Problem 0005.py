#finding the smallest positive integer that is evenly divisible by all numbers from 1 to 20, Approach 1: Uding a generator function
def infinite_natural_numbers(start,step):
    while True:
        yield start
        start +=step

 for numerator in infinite_natural_numbers(20,20):
    if all(numerator % denominator == 0 for denominator in range(20,1,-1)):
        print(numerator)
        break    

# finding the smallest positive integer that is evenly divisible by all numbers from 1 to 20, Approach 2: Using itertools module
import itertools
divisors = range(20,1,-1)
for dividend in itertools.count(20,20):
    if all(dividend % divisor == 0 for divisor in divisors):
        print(dividend)
        break
