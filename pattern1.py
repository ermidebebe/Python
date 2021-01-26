for i in range(9):
    for j in range(9):
        if ((i<=4 and j<=4) and i>=j) or ((i>=4 and j<=4)and i+j<=8):
            print('*',end='')
    print("")
for i in range(10):
    for j in range(10):
        if  i>=9-j and (i>=5) or ((i<=5)and i<=j) :
            print('*',end='')
        else:
            print(" ",end='')
    print("")
for i in range(9):
    for j in range(5):
        if  i>=8-j and (i>=4) or ((i<=4)and i<=j) :
            print('*',end='')
        else:
            print(" ",end='')
    print("")
