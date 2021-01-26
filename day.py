day=int(input("number of day="))
if day>=1 and day<=7:
    if day==1:
        print("Monday")
    elif day==2:
        print("Tuesday")
    elif day==3:
        print("Wednsday")
    elif day==4:
        print("Thursday")
    elif day==5:
        print("Friday")
    elif day==6:
        print("Saturday")
    elif day==7:
        print("sunday")
else:
    print("please enter correct day number")
