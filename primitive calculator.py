table={}
def calculator(n):
    x=0
    y=0
    z=0
    if n==1:

        return 0
    if n not in table:
        if n%3==0:
            x=1+calculator(n/3)
        if n%2==0:
            y=1+calculator(n/2)
        z=1+calculator(n-1)
        if x!=0 and y!=0 and z!=0:
            table[n]=min(x,y,z)
        elif x==0 and y==0:
            table[n]=z
        elif x==0 and y!=0:
            table[n]= min(z,y)
        elif x!=0 and y==0:
            table[n]= min(z,x)
    return table[n]
print(calculator(7))
