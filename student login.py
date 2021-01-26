def get_login_name(first_name,last_name,ID):
    login=first_name[:3]
    login+=last_name[:3]
    login+=ID[-3:]
    return login
def main():
    print("please enter your profile as follows")
    first_name=input('first name:')
    last_name=input('last name:')
    ID=input('ID:')
    print('your login name is',get_login_name(first_name,last_name,ID))
main()
