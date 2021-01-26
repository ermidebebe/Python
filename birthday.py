def menu():
    '''display menu and return selected element if it is in
     given menu else it forces to enter again'''
    menu=[1,2,3,4,5]
    choice=0
    while choice not in menu:
        print('please select one the following menu\n'+'---'*12)
        print(1,'Look up a BirthDay')
        print(2,'Add a new BirthDay')
        print(3,'Change a BirthDay')
        print(4,'Delete a BirthDay')
        print(5,'Quit Program')
        choice=int(input('choice:'))
    return choice
def response(choice,birthday):
    name=input('Name:')
    if choice==1:
        print(birthday.get(name,'Entry does not found'))
    elif choice==2:
        birthday[name]=input('BirthDay:')
    elif choice==3:
        if name in birthday:
            birthday[name]=input('BirthDay:')
        else:
            print('Entry does not found')
    else:
        if name in birthday:
            del birthday[name]
        else:
            print('Entry does not found')
def main():
    choice=menu()
    birthday={}
    while choice!=5:
       response(choice,birthday)
       print()
       choice=menu()
main()      
        
    
    
