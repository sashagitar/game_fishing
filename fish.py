class Fish:
    vid=str()
    price=int()
    ves=int()
    def __init__(self,vid:str,ves:int,price:int):
        self.vid= vid
        self.ves= ves
        self.price= ves*price/1000
    def __str__(self) -> str:
        return f"{self.vid} Цена:{self.price} Вес:{self.ves} " 
    def sell(self)->int:        
        return self.price
        