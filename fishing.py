import random #импортируют функцию рандома
from fish import Fish #импортирует клаас 'рыба'  
class Fishing: #класс рыбалка
    vid=['Карась','Карп','Лещ','Окунь','Сом','Ёрж','Плотва','Жерих','Линь','Вюн','Верхоплавка','Щука','Клад']# виды рыб
    price=[254,349,700,700,550,70,500,1200,520,650,7,450,5000]#цена рыб
    shans=[(0,9),(10,18),(19,26),(27,31),(32,33),(34,41),(42,53),(54,56),(57,60),(61,67),(68,78),(79,83),(84,84),(85,100)]#шанс выодения рыб
    ves=[(350,650),(1750,2550),(3750,4250),(2400,2600),(3500,4500),(382,750),(975,1500),(2750,5000),(4000,7500),(115,200),(2,10),(500,1400)]#вес рыбы
    def __init__(self):#
        self.test_fish = Fish('test1',99,10)#тестовая рыба

    def go_fishing(self)->Fish:#начало рыалки   
        ran=random.random()*100#выдает не целое число от 0 до 1 и умножает на 100
        for i in range(len(self.shans)-1):
            fish = self.get_fish(i, ran)#сохранение
            if fish != None:
                return fish
        return None

    def get_fish(self, i:int, ran:int) ->Fish:#сохранение
        if ((self.shans[i][0] <= ran) & (ran <= self.shans[i][1])):#шанс
            a = self.ves[i][0]
            b = self.ves[i][1]
            ves = random.randint(a,b)
            return Fish(self.vid[i], self.price[i], ves)
        else:
            return None

    