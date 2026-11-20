# This program finds the largest and smallest palindromic numbers that are products of two three-digit numbers.

def ispalindrome(x):
    return str(x) == str(x)[::-1]

palindrome_set = set()
for num1 in range(100,1000):
    for num2 in range(100,1000):
        product = num1*num2
        if ispalindrome(product):
            palindrome_set.add(product)

print("Palindrome set:", palindrome_set)
print("The largest palindrome of two three-digit numbers is: ", max(palindrome_set))
print("The smallest palindrome of two three-digit numbers is: ", min(palindrome_set))
