class Name:
    def __init__(self):
        self.name=''
        self.age=0
        self.year=0
        self.dream=''
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_year_dream(self,year,dream):
        self.year=year
        self.dream=dream
    def print(self):
        print('Name',self.name+'\n'+'Age'+str(self.age)+'\nYear'+str(self.year)+'\nDream'+self.dream)
        
