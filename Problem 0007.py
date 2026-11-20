#finding the 10001st prime number
from sympy import isprime;
import itertools

nth_prime = 10001
prime_count = 0

for number in itertools.count(3,2):
    if isprime(number):
        prime_count += 1
        if prime_count == nth_prime-1:
            print("The 10001st prime number is: ", number)
            break

