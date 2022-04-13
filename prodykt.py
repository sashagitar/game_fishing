from magaz import Magaz
class Prodykt:
    vid=str()
    price=int()
    stats=int()
    id_ = int()

    def __init__(self,id_:str,vid:str,ves:int,price:int,stats:int):
        self.vid= vid
        self.ves= ves
        self.stats = stats
        self.price= price
        self.id_ = id_
        
    def __str__(self) -> str:
        if self.id_ == 1:
            return f"{self.vid} Цена:{self.price} Сон + {self.stats} " 
        if self.id_ == 2:
            return f"{self.vid} Цена:{self.price} Радость + {self.stats} " 
        else:
            return f"{self.vid} Цена:{self.price} Сытость + {self.stats} " 
