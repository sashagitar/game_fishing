from prodykt import Prodykt
class Holodos:
    eda=[]

    def __init__(self):
        self.eda=[]

    def add(self,prodykt:Prodykt):
        self.eda.append(prodykt)

    def delete(self, id_:int) ->Prodykt:
        if len(self.eda) > id_ >= 0:
            prodykt=self.eda[id_]
            self.eda.pop(id_)
            return prodykt
        else:
            return None
        
    def __str__(self) -> str:
        s=''
        for i in self.eda:
            s+=str(self.eda[i])+'\n'
        return s
