def convolution(h,x):
    y=[]
    sum=0
    try:
        for n in range(len(h)+len(x)-1):
            for k in range(max(0,n-(len(x)-1)),min(n,len(h)-1)+1):
                sum=sum+int(h[k])*int(x[n-k])
            y.append(sum)
            sum=0;
    except:
        print('please enter your values correctly')
        main()
    return y
def main():
    print('please enter your impulse response separated by comma')
    h=input('h=').split(',')

    print('please enter your input separated by comma')
    x=input('x=').split(',')
    print('y=',convolution(h,x),sep='')
main()
          
