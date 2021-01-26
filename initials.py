def initials():
    print("please enter you profile as follows")
    first_name=input('first name:')
    middle_name=input('middle name:')
    last_name=input('last name:')
    return first_name[:1].upper()+'.'+middle_name[:1].upper()+'.'+last_name[:1].upper()
def main():
    print('here is your initial name')
    print(initials())
main()
