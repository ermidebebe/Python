def date():
    month=[['1','January'],['2','February'],['3','March'],['4','Appril'],['5','May'],\
          ['6','June'],['7','Jully'],['8','August'],['9','september'],['10','October'],
          ['11','November'],['12','December']]
    print('please enter date in mm/dd/yy format')
    str_date=input('date:')
    for i in range(len(month)):
        if month[i][0]==str_date.split('/')[0]:
            return month[i][1]+' '+str_date.split('/')[1]+', '+str_date.split('/')[2]
def main():
    print('Here is the day you entered in word format'\
          ,date(),sep='\n')
main()
        

