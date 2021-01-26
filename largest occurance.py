s = input("input:")
str=[]
count=[]
counted=0
counting=[]
str1=[]
for i in s:
    str.append(i)
str.sort()
for i in range(len(str)):
    for j in range(len(str)):
        if str[i]==str[j]:
            counted=counted+1
    count.append(counted)
    counting.append(counted)
    counted=0
counting.sort()
counting.reverse()
for i in  range(len(str)):
    for j in range(len(str)):
        if counting[i]==count[j]:
             str1.append([str[j],count[j]])
for i in range(3):
    for j in range(2):
        print(str1[i][j],end=' ')
    print()
    
            
         
          
