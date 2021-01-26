def sort(number):
    tupl=[]
    number1=[]
    for i in range(len(number)):
           tupl.append(number[i][len(number[i])-1])
    tupl.sort()
    for i in range(len(number)):
        for j in range(len(number)):
              if tupl[i]==number[j][len(number[i])-1]:
                  number1.append(number[j])
    return number1
print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))   
