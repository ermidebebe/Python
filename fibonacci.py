count_1=0
count_2=1
print(count_1,count_2,sep=' , ',end=', ')
for i in range(50):
    sum=count_1+count_2
    count_1=count_2
    count_2=sum
    print(sum,end=' , ')
    if sum>100:
        break
