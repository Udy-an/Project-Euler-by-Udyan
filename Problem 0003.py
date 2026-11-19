#Largest prime factor of 600851475143

from sympy import isprime
n = 600851475143

s=set()
for i in range(2,int((n**0.5)+1)):
    if isprime(i) and n%i==0:
        s.add(i)
        n=int(n/i)
print(s)
print(max(s))
product = 1
for factor in s:
    product *= factor
print(product)
