import random

class Card:
    __name=""
    __number=0
    __value=0
    def __init__(self,name,number,value):
        self.__name=name
        self.__number=number
        self.__value=value
    def __init__(self):
        pass
    def setName(self,name):
        self.__name=name
    def setNumber(self,number):
        self.__number=number
    def setValue(self,value):
        self.__value=value
    def getNumber(self):
        return self.__number
    def getValue(self):
        return self.__value
    def __str__(self):
        return ("----------\n{}\n{}\n----------").format(self.__name,self.__number)

class Hand:
    def __init__(self):
        self.__cards=[]
        self.__name=""
    def __init__(self,name):
        self.__name=name
        self.__cards=[]
    def addCard(self,card):
        if isinstance(card,Card):
            self.__cards.append(card)
    def getTotal(self):
        total=0
        for i in self.__cards:
            total+=i.getValue()
        return total
    def getCard(self):
        return self.__cards.copy()
    
def cards():
    card=[]
    for i in range(52):
        card.append(Card())
    name=["Heart","Club","Spades","Diamond"]
    number=["J","K","Q","A"]
    for i in range(2,11):
        number.append(i)
    for i in range(len(card)):
        card[i].setName(name[i//13])
        card[i].setNumber(number[i%13])
        
        if  0<=i%13<=2:
            card[i].setValue(10)
        elif i%13==3:
            card[i].setValue(11)
        else:
            card[i].setValue(card[i].getNumber())
    return card.copy()

def displayCards(cards):
    for i in cards:
        
        print(i,"\n"*3)

def main():
    player=Hand("Player")
    dealer=Hand("Dealer")
    card=cards()
    for i in range(20):
        random.shuffle(card)
    for i in range(2):
        index=random.randint(0,len(card)-1)
        player.addCard(card[index])
        del card[index]
        index=random.randint(0,len(card)-1)
        dealer.addCard(card[index])
        del card[index]
    print("Welcome to our Casino\n\n")
   

    print("Dealer's Card")
    displayCards([dealer.getCard()[0]])
    print(player.getTotal())
    while True:
         displayCards(player.getCard())
         if player.getTotal()==21:
             print("you won")
             break
        elif player.getTotal()>21:
            print("Busted")
            break
        response=input("do you want to hit(y?) ")

        if response.lower()=="y":
            player.
main()
