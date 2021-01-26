def choose_best_sum(t, k, ls):
    sum=[]
    best=[]
    for i in range(len(ls)):
        if len(ls)-i>=k-1:
            for j in range(i+1,len(ls)-1):
                 for k in range(j+1,len(ls)):
                      sum.append(ls[i]+ls[j]+ls[k])
    if len(sum)>=1:
        for i in range(len(sum)):
            if sum[i]<=t:
                best.append(sum[i])
    best.sort()
    best.reverse()
    print(best)
    if len(best)>=1:
        return best[0]
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(166, 3,xs))
                
                    
        
            
          
                   
        
                   
