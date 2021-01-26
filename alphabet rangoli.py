def print_rangoli(size):
    alphabet=[]
    for i in range(n):
        if i==n-1:
            alphabet.append(chr(97+n-1))
        else:
            alphabet.append(chr(45))
    for i in range(n-1):
        alphabet1=alphabet[0:n-1]
        alphabet1.reverse()
        alpha=alphabet+alphabet1
        print('-'.join(alpha))
        for k in range(1,n):
            alphabet[k-1]=alphabet[k]
        alphabet[n-1]=chr(ord(alphabet[n-1])-1)
    for  i in range(n):
        alphabet1=alphabet[0:n-1]
        alphabet1.reverse()
        alpha=alphabet+alphabet1
        print('-'.join(alpha))
        for l in range(len(alphabet)):
            alphabet[l]=chr(ord(alphabet[l])+1)
        for k in range(i+1):
            alphabet[k]=chr(45)

n=int(input("size="))
print_rangoli(n)
