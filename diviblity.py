import random
for num in range(1500,2700):
    if num%5==0 and num%7==0:
        #print()
         
guess=int(input("guess="))
while guess<1 or guess>9:
     print("please enter number between 1 and 9")
     guess=int(input("guess="))
while guess!=5:
    print("you gussed wrong number")
    guess=int(input("guess="))
print("you gussed the correct number")
