def merge_the_tools(string, k):
    piece=len(string)//k
    segment=[]
    for i in range(piece):
        segment.append(string[k*i:k*(i+1)])
    final=''
    for i in range(len(segment)):
        for j in range(len(segment[i])):
            if final.find(segment[i][j])==-1:
                       final+=segment[i][j]
        segment[i]=final
        final=''
    print( '\n'.join(segment))
def iq_test(numbers):
    t=False
    for i in range(len(numbers.split())):
        for j in range(len(numbers.split())):
            if i!=j and int(numbers.split()[i])%2==int(numbers.split()[j])%2:
                t=True
        if not t:
            return i+1
        t=False
       
                
    
        
            
                
       
    
