class Fish:
    vid=str()
    price=int()
    ves=float()
    def __init__(self,vid:str,ves:float,price:int):
        self.vid= vid
        self.ves= ves/1000
        self.price= ves*price/1000
    def __str__(self) -> str:
        return f"{self.vid} Цена:{self.price} Вес:{self.ves} кг" 
    def sell(self)->int:        
        return self.price
        