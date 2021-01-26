pay_Rate=float(input("pay_rate="))
Hours_worked=int(input("total_hours_worked="))
if(Hours_worked<=40):
   print("your total salar=%15.2f"%(pay_Rate*Hours_worked))
else:
    print("your total salary=%15.2f"%(pay_Rate*Hours_worked+(Hours_worked-40)*pay_Rate*1.5))


