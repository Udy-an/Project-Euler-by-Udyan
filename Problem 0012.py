#Finding the first triangular number with over certain exclusive factors
import itertools
from math import isqrt 
def independent_factors_over(number, number_of_exclusive_factors): 
     set_of_factors = set()
     for denominator in range(1, int(isqrt(number)+1)):
         if number % denominator == 0:
             set_of_factors.add(denominator)
             set_of_factors.add(number // denominator)
     if len(set_of_factors) > number_of_exclusive_factors:
         return number
     else:
         return False
         
     
 
def eligible_triangular_number(number_of_exclusive_factors):
     summation = 0
     for i in itertools.count(1,1):
         summation = summation + i
         if independent_factors_over(summation, number_of_exclusive_factors) :
            return summation

        
number_of_exclusive_factors = int(input("The first triangular number with how many exclusive factors do you want? "))
print(eligible_triangular_number(number_of_exclusive_factors))     




############# alternative solution by calude#################




from itertools import count   # count(1) generates 1, 2, 3, ... forever
from math import isqrt        # integer square root, e.g. isqrt(30) = 5

# limit: we want the first triangular number with MORE than this many factors
limit = int(input("More than how many factors? "))

# n: position in the triangular sequence (1st, 2nd, 3rd, ...)
for n in count(1):

    # t: the nth triangular number = 1 + 2 + ... + n, computed with the formula n(n+1)/2
    t = n * (n + 1) // 2

    # k: a candidate divisor. We only test k from 1 up to sqrt(t), because every
    # divisor k at or below sqrt(t) has a partner t // k at or above sqrt(t).
    #
    # "if t % k == 0" keeps only the k values that divide t exactly.
    #
    # For each divisor k found, we add up its contribution to the factor count:
    #   - normally 2, because k and its partner t // k are two different factors
    #   - 1 when k * k == t, because then k and its partner are the same number
    #     (e.g. for 36, k = 6 pairs with 6, which is only one factor)
    # In Python, (k * k == t) is True (1) or False (0), so 2 - (k * k == t) gives 1 or 2.
    #
    # sum(...) adds these contributions, giving the total number of factors of t.
    if sum(2 - (k * k == t) for k in range(1, isqrt(t) + 1) if t % k == 0) > limit:
        print(t)   # the first triangular number with more than `limit` factors
        break      # stop the infinite loop from count(1)
