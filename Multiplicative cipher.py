def main():
   
    mul_key={1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17,25:25}
    k=0;
    while(1):
        print("please enter key b/n zero and 25 ")
        k=int(input("key="))
        if k>0 and k<26:
            break
    text=input("plain text: ")
    text.lower()
    c=encrypt(text,k)
    print("cipher text:" ,c)
    p=decrypt(c,mul_key,k)
    print("decrypted text:" ,p)
def encrypt(text,k):
    t=[]
    c=""
    for i in range(len(text)):
        if text[i]==" ":
            continue
        t.append(((ord(text[i])-97)*k)%26)
    for i in range(len(t)):
        c=c+chr(t[i]+97)
    return c
def decrypt(c,mul_key,k):
    t=[]
    p=""
    for i in range(len(c)):
        t.append(((ord(c[i])-97)*mul_key[k])%26)
    for i in range(len(t)):
        p=p+chr(t[i]+97)
    return p
main()
