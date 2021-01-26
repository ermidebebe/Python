def process():
    square=[]
    ro=[]
    row=[0]*3
    column=[0]*3
    diagonal=[0]*2
    for i in range(3):
       for j in range(3):
           ro.append(int(input('Row'+str(i+1)+' Column'+str(j+1)+' :')))
       square.append(ro)
       ro=[]
    print(square)
    for i in range(3):
        for j in range(3):
            row[i]+=square[i][j]
            column[i]+=square[j][i]
            if i==j:
               diagonal[0]+=square[i][j]
            if i+j==2:
               diagonal[1]+=square[i][j]
    for i in range(3):
        if column[i]!=15:
            return False
        if row[i]!=15:
            return False
    for i in diagonal:
        if i!=15:
            return False
    return True
def main():
    if process():
        print('The Square is Magical')
    else:
        print('It is not magical')
main()
