from prodykt import Prodykt
class Holodos:
    eda=[]

    def __init__(self):
        self.eda=[]

    def add(self,prodykt:Prodykt):
        self.eda.append(prodykt)

    def delet(self, id_:int) ->Prodykt:
        prodykt=self.eda[id_]
        self.eda.pop(id_)
        return prodykt
        
    def __str__(self) -> str:
        s=''
        for i in self.eda:
            s+=str(i)
        return s
    