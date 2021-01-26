def main():
    try:
        n=int(input('n='))
    except ValueError:
        print('please enter enter 0 or positive integer')
        main()
    line=[]
    file=open('financial.txt','r')
    while True:
        lines=file.readline()
        if lines=='':
            break
        line.append(lines)
    line=line[len(line)-n:-1]
    for i in line:
        print(i.strip('\n'))
main()
    
        

