import random
def main():
    pain=[]
    print('Here Is The Lottery Number ')
    for i in range(7):
        pain.append(random.randint(0,9))
    for i in pain:
        print(i,end='')
def nothing(lst,n):
    for i in lst:
        if i>n:
            print(i)
main()
