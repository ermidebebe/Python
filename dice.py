import random
answer='y'
while answer=='y' or answer=='Y':
    print("rolling dice....","their values are",sep="\n")
    print(random.randint(1,6),random.randint(1,6),sep="\n")
    print("if you to simulate again press y or Y or press anything")
    answer=input("answer=")
