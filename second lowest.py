if __name__ == '__main__':
    number=[]
    number1=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        number.append([name,score])
    number.sort()
    number1.append(number[0][1])
    for i in range(len(number)):
        if number[i][1] not in number1:
            number1.append(number[i][1])
    number1.sort()
    for i in range(len(number)):
        if number[i][1]==number1[1]:
            print(number[i][0])
