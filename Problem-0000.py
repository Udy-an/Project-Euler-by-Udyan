#Summation of the odd perfect squares amongst first 129000 perfect square numbers
total = 0

for n in range(1, 129001):
    square = n * n
    if square % 2 != 0:
        total += square

print(total)
