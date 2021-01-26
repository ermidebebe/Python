for i in range(100,401):
    j=i
    while i>0:
    
        if (i%10)%2==0:
            t=True
        else:
            t=False
            break
        i=i//10
    #if t:
        #print(j,"",sep=',',end='')

for i in range(8):
   
    if i==2:
        print("* *   * *")
        continue
    if i==3:
         print("*   *   *")
         continue
    print("*       *")
     
        
    
