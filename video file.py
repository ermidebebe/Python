def main():
    print('W or w for writing to a file')
    print('R or r for reading a file')
    choice=input("choice>>")
    if choice=='W' or choice=='w':
        write()
    elif choice=='R' or choice=='r':
        read()
def write():
    print('how many lines do you want to be printed')
    n=int(input('lines>>'))
    file=open('video time.txt','a')
    print('please enter your vidoe name and playback time like this\nname  time')
    for i in range(n):
        file.write(input()+'\n')
    file.close()
def read():
    print('Here is your video names and playback name')
    print('Name  PlayBack time')
    file=open('video time.txt','r')
    total=0
    for val in file:
        total+=int(val.split('  ')[1])
        print(val.rstrip('\n'))
    print('TOTAL->'+str(total))
main()
