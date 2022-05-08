class Prodykt:
    name=str()
    price=int()
    stats=int()
    id_ = int()
    def __init__(self,id_:str,name:str,ves:int,price:int,stats:int):
        self.name= name
        self.ves= ves
        self.stats = stats
        self.price= price
        self.id_ = id_
    def __str__(self) -> str:
        if self.id_ == 1:
            return f"{self.name} Цена:{self.price} руб; Сон + {self.stats} " 
        if self.id_ == 2:
            return f"{self.name} Цена:{self.price} руб; Радость + {self.stats} " 
        else:
            return f"{self.name} Цена:{self.price} руб; Сытость + {self.stats} " 