import random
print("here are the values of 10 tosses")
for i in range(10):
    number=random.randint(1,2)
    if number==1:
        print("Head")
    else:
        print("Tail")
