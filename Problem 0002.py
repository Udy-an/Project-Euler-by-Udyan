#find the sum of all the even Fibonacci numbers below 4 million of the series: 1,2,...

sum=0
a=1
b=2
while b<=4000000:
    c=a
    if b%2==0:
        sum+=b
    a=b
    b=c+b
print(sum)


