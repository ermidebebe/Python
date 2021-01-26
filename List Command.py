if __name__ == '__main__':
    N = int(input())
    lst=[]
    for  i in range(N):
        string=input()
        if string.split()[0]=='print':
            print(lst)
        elif string.split()[0]=='pop':
            lst.pop()
        elif string.split()[0]=='sort':
            lst.sort()
        elif string.split()[0]=='reverse':
            lst.reverse()
        elif string.split()[0]=='insert':
            lst.insert(int(string.split()[1]),int(string.split()[2]))
        elif string.split()[0]=='remove':
            lst.remove(int(string.split()[1]))
        elif string.split()[0]=='append':
            lst.append(int(string.split()[1]))
        

