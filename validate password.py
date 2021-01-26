def isvalid_password(password):
    valid=True
    validpassword=False
    numeric=False
    lower=False
    if len(password)<=7:
        valid=False
    for i in range(len(password)):
        if password[i:i+1].isupper():
            validpassword=True
        if password[i:i+1].islower():
            lower=True
        if password[i:i+1].isdigit():
            numeric=True
    if valid and validpassword and numeric and lower:
        return True
    else:
        return False
def main():
    print("please insert password that is seven or more characters long and \
it must has atleast one upppercase and lowercase character and atleast one digit")
    password=input("password:")
    if isvalid_password(password):
        print('you entered correct password')
    else:
        print('you entered incorret password')
main()
         
