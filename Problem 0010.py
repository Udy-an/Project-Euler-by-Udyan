#summation of primes
def prime_check(x):
    if x < 2:
      return False
    elif x == 2:
       return True
    elif x % 2 == 0:
       return False
    else:
      for denominator in range(3,int((x**0.5)+1), 2):
         if x % denominator == 0 :
           return False
           break
      return True
         
summation = 0
for number in range(2000001):
   if prime_check(number):
      summation = summation + number
print("Summation of All the Primes below 2000000: ", summation)
    
