from fish import Fish 
from pers import Pers
class Sadok:
    sadok=[]
    n=int()
    x=0
    def __init__(self):
        self.sadok = []
        self.n = 0
        self.cost=0
    def Aad(self,f:Fish):
        self.sadok.append(f)
        self.n+=1
        self.cost+=self.prise
    def sold(self):
        sum=0
        for i in self.sadok:
            sum+=self.cost 
        return sum
    def __str__(self,cost) -> str():
        s=''
        if self.n!=0:
            for i in self.sadok:
                s+=str(i)+'\n'
            return s+'Общая стоимость: '+str(self.cost)+'\n'
        else:
            return 'Рыбы нет'