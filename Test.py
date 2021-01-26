from random import shuffle
text=input()
print(text)
factorial=1
for i in range(1,len(text)+1):
    factorial*=i
permutations=[list(text)]
for k in range(factorial-1):
    value=list(text)
    shuffle(value)
    while value in permutations:
        shuffle(value)
    permutations.append(value)
    text=''
    for i in value:
        text+=i
    print(text)
    
