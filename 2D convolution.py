def conv2D(x,h):
    y=[]
    print(len(h[0]))
    sum=0
    for n1 in range(len(x)+len(h)-1):
        y.append([])
        for n2 in range(len(x[0])+len(h[0])-1):
            for k1 in range(max(0,n1-(len(h)-1)),min(n1,len(x)-1)+1):
                for k2 in range(max(0,n2-(len(h)-1)),min(n2,len(x[0])-1)+1):
                    sum=sum+int(x[k1][k2])*int(h[n1-k1][n2-k2])    
            y[n1].append(sum)
            sum=0
    return y
def main():
    x=input('x=')
    h=input('h=')
    x=x.split(';')
    h=h.split(';')
    X=[]
    H=[]
    for i in x:
        X.append(i.split(','))
    for i in h:
        H.append(i.split(','))
    print('y=',conv2D(X,H))
main()
