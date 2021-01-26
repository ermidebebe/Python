import random
def main():
    print('please enter of random numbers you want to be written')
    n=int(input('N:='))
    file=open('random.txt','a')
    for i in range(n):
        file.write(str(random.randrange(1,500))+'\n')
    file.close()
main()                  
