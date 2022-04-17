class Prodykt:
    name=str()
    price=int()
    stat=int()
    id=int()
    def __init__(self,name:str,price:int,stat:int,id:int):
        self.name=name
        self.price=price
        self.stat=stat
        self.id=id
    def __str__(self)->str:
        if self.id == 0:
            return f"{self.name} Цена:{self.price} сытость + {self.stat}  "
        elif self.id==1:
            return f"{self.name} Цена:{self.price} сон - {self.stat} "
        elif self.id==2:
            return f"{self.name} Цена:{self.price} радость - {self.stat}"

        
    def sell(self)->int:
        return self.price