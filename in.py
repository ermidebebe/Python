employee=[]
rate=23
print('please insert hours worked by each employee')
for i in range(6):
    employee.append(int(input('employee '+str((i+1))+':')))
gross_pay=[]
print('here is the gross pay of your employees')
for i in range(6):
    gross_pay.append(rate*employee[i])
    print('employee'+str((i+1))+'=',gross_pay[i])
