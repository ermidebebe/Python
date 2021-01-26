if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sort=[]
    sort.append(arr[0])
    for i in arr:
        if i not in sort:
            sort.append(i)
    sort.sort()
    sort.reverse()
    if  len(sort)>=2:
        print(sort[1])
            
    
    
    
