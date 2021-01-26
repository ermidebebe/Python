import random
import os
def main():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
                'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    #os.mkdir("Random questions")
    os.chdir(".\\Random questions")
    question=list(capitals.keys())
    for i in range(35):
       random.shuffle(question)
       file1=open("Answer sheet {}.pdf".format(i+1),'w')
       file2=open("Question sheet {}.txt".format(i+1),'w')
       file1.write("Answer sheet {}\n".format(i+1))
       file2.write("Question sheet {}\n".format(i+1))
       for k in range(50):
           j=[]
           z=[]
           for f in range(3):
               l=random.randint(0,49)
               
               while l==k or l in z:
                   l=random.randint(0,49)
               j.append(capitals[question[l]])
               z.append(l)
           choice=[x for x in j]
           choice.append(capitals[question[k]])
           random.shuffle(choice)
           file1.write("{}.{}\n".format(k+1,'ABCD'[choice.index(capitals[question[k]])]))
           file2.write(("{}.The capital city of {} is _________.\n"+"{:>4}.{}\n"*4).format(k+1,question[k],'A',choice[0],'B',choice[1],'C',choice[2],"D",choice[3]))
       file1.close()
       file2.close()
           
        
main()
