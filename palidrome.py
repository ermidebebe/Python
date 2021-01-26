number=int(input("number=:"))
count=0
sum=0
num=number
while num>0:
    count=count+1
    num=num//10
num=number
for i in range(count-1,-1,-1):
    sum+=(num%10)*10**i
    num=num//10
if sum==number:
    print("the number is palindrome")
else:
    print("the number is not palindrome")

    

