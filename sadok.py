from fish import Fish 
class Sadok:
    sadok=[]
    n=int()
    cost= int()

    def __init__(self):
        self.sadok = []
        self.n = 0
        self.cost=0

    def add(self,f:Fish):
        self.sadok.append(f)
        self.n+=1
        self.cost+=f.price
        
    def __str__(self) -> str():
        s=''
        if self.n > 0:
            for i in self.sadok:
                s+=str(i)+'\n'
            return s+'Общая стоимость: '+str(self.cost)+'\n'
        else:
            return 'Рыбы нет' and self.n
    def bue(self):
        pribel = self.cost
        self.sadok = []
        self.n = 0
        self.cost = 0
        return pribel