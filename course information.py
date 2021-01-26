def process(choice):
    time={'ECEG-3163':['Tuesday(2:30-4:00)','Wednsday(2:30-5:45)'],\
          'ECEG-3171':['Monday(2:30-4:00)','Saturday(2:30-5:45)'],\
          'ECEG-3172':['Wednsday(7:30-11:45)',''],\
          'ECEG-3173':['Thursday(2:30-4:00)','Monday(7:30-11:45)'],\
          'ECEG-3174':['Tuesday(4:15-5:45)','Thursday(7:30-11:45)'],\
          'ECEG-3175':['Thursday(4:15-5:45)','Tuesday(7:30-11:45)']}
    room={'ECEG-3163':['131                ','N-114'],\
          'ECEG-3171':['118                ','N-114'],\
          'ECEG-3172':['Fundamental Lab    ',''],\
          'ECEG-3173':['131                ','N-113'],\
          'ECEG-3174':['E-131              ','132'],\
          'ECEG-3175':['131                ','138']}
    instructor={'ECEG-3163':['Dagmawi.D         ','Meleake.S'],\
                'ECEG-3171':['Rediet.M          ','Rediet.M'],\
                'ECEG-3172':['WOrku.A           ',''],\
                'ECEG-3173':['Yared.T           ','Yared.T'],\
                'ECEG-3174':['Tsegamlak.T       ','Leul.W'],\
                'ECEG-3175':['Mihreteab         ','Mihreteab']}
    print('---'*23+'\n\t\t\t\t'+choice+'\n'+'---'*23)
    print('\t\tLecture\t\t\t\t'+'Tutorial\t'+'\n'+'---'*23)
    print('Time      \t'+time[choice][0]+'\t\t'+time[choice][1]+'\t'+'\n'+'---'*23)
    print('Room      \t'+room[choice][0]+'\t\t'+room[choice][1]+'\t'+'\n'+'---'*23)
    print('Instructor\t'+instructor[choice][0]+'\t\t'+instructor[choice][1]+'\t'+'\n'+'---'*23)
def menu():
    menu=['ECEG-3171','ECEG-3172','ECEG-3163','ECEG-3173','ECEG-3174','ECEG-3175']
    choice='e'
    while choice.lower()!='q' and choice not in menu:
        print('please choose one from the following\n'+'---'*17)
        print('ECEG-3163 for Computer Architecture and Organization')
        print('ECEG-3171 for Digital Signal Processing')
        print('ECEG-3172 for Electrical Engineering Lab V')
        print('ECEG-3173 for Introduction To Instrumentation')
        print('ECEG-3174 for Introduction To Communication')
        print('ECEG-3175 for Introduction to Control Engineering')
        print('Q or q to Quit')
        choice=input('Course:')
    return choice
def main():
    choice=menu()
    while choice.lower()!='q':
        process(choice)
        print()
        choice=menu()
main()

        
    
    
