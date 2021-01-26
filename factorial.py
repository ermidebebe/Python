import math
number=int(input("number=:"))
factorial=1
for i in range(number):
    factorial*=(number-i)
print("factorial=",factorial)
x=int(input("power of e=:"))
e=0
factorial=1
for i in range(100):
    for j in range(i):
         factorial*=(i-j)
    e+=(x**i)/factorial
    factorial=1
print(format(e))
print(math.exp(2))
