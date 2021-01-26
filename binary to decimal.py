binary=int(input("binary="))
power=0
decimal=0
while binary>0:
    decimal+=(binary%10)*2**power
    power=power+1
    binary=binary//10
print("decimal\n",decimal)

    
