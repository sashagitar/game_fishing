import random
class Pers:
    hp=int()
    son=int()
    golod=int()
    happy=int()
    money=int()
    def __init__(self ):
        self.hp=100
        self.son=100
        self.golod=100
        self.happy=100
        self.money=500
    def chec(self):
        if (self.golod<=0):
            self.hp-=10
        if(self.happy<=0):
            self.hp-=5
        if(self.son<=0):
            a=random.randint(1,8)
            self.hp-=a
        if (self.hp<=0):
            return 'PIP'
    def stats(self):
        print (f"ХП - {self.hp}"+'\n'+f"Сон- {self.son}")