from prodykt import Prodykt
class Holodos:
    eda=[]

    def __init__(self):
        self.eda=[]

    def add(self,prodykt:Prodykt):
        self.eda.append(prodykt)

    def delet(self, id_:int) ->Prodykt:
        if (id_ < len(self.eda)):
            prodykt=self.eda[id_]
            self.eda.pop(id_)
            return prodykt
        else:
            return None
        
    def __str__(self) -> str:
        s=''
        id_ = 0
        for i in self.eda:
            s+= str (id_) + ' ' + str(i) + '\n'
            id_+=1
        return s
    