def get_sales():
    print("plaese enter the amount you sold")
    return int(input("sales=$"))
def get_advance():
    print("plaese enter the amount of advance")
    advance=int(input("advance=$"))
    while advance>2000:
        print("the andvance must be less than $2000")
        advance=int(input("advance=$"))
    return advance
def commision(sales):
    if sales<10000:
        commision=10
    elif sales<=14999:
        commision=12
    elif sales<=17999:
        commision=14
    elif sales<=21999:
        commision=16
    else:
        commision=18
    return commision
def calculate():
    sales=get_sales()
    return (sales*(commision(sales)/100)-get_advance())
def main():
    pay=calculate()
    if pay>=0:
        print("here is the your payment",pay,sep='=')
    if pay<0:
        print(pay,"you should reimburse the company")
    
main()
   
