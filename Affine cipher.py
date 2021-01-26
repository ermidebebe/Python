def main():
   
    mul_key={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}
    while(1):
        print("please enter correct key for multiplicative cipher")
        k1=int(input("k1="))
        if k1 in mul_key:
            break
    
    while(1):
        print("please enter key b/n zero and 25 ")
        k2=int(input("k2="))
        if k2>0 and k2<26:
            break
    text=input("plain text: ")
    text.lower()
    c=encrypt(text,k1,k2)
    print("cipher text:" ,c)
    p=decrypt(c,mul_key,k1,k2)
    print("decrypted text:" ,p)
def encrypt(text,k1,k2):
    t=[]
    text=text.lower()
    for i in range(len(text)):
        if text[i]==" ":
            continue
        t.append(((ord(text[i])-97)*k1)%26)
    c=""
    for i in range(len(t)):
        c=c+chr(((t[i]+k2)%26)+97)
    return c
def decrypt(c,mul_key,k1,k2):
    t=[]
    p=""
    for i in range(len(c)):
        t.append(((ord(c[i])-97)-k2)%26)
    for i in range(len(t)):
        p=p+chr(((t[i]*mul_key[k1])%26)+97)
    return p
main()
