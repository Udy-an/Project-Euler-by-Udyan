# This program finds the difference between the square of the summation and the summation of the squares of the first 100 natural numbers.
summation = 0
for number in range(101):
    summation = summation + number
square_of_summation = summation ** 2

n=100
sum_of_squares = (n*(n+1)*((2*n)+1))/6
difference = square_of_summation - sum_of_squares
print("The difference between the square of the summation and the summation of the squares of the first 100 natural numbers is: ", difference)

