from fish import Fish
from fishing import Fishing
from holodos import Holodos
from magaz import Magaz
from pers import Pers
from prodykt import Prodykt
from sadok import Sadok

FISHING = Fishing()
MAGAZ = Magaz()
PERS = Pers()
SADOK = Sadok()
HOLODOS = Holodos()

def fishing():
    pass

def sadok():
    pass

def eat():
    pass

def magaz():
    pass

def sleep():
    pass

def happe():
    pass

def finish():
    pass

def dayHaus():
    pass

def main():
    PERS.chec()
    if PERS.chec() =='RIP':
        finish()
    PERS.stats()
    print('''
    Выберите действие:
    1. Порыбачить
    2. Покушать
    3. Рынок
    4. Садок
    5. Купить дом
    6. Выход
    7. Настройки
    8. Промокод
    ''')
    go = input('\n(Введите число или слово)\n')
    switch = {
        '1': fishing(),
        '2': eat(),
        '3': magaz(),
        '4': sadok(),
        '5': dayHaus()
    }

def  start():
    print('''Добро Пожалвать в Рыбалку!!! Здесь вам престоит ловить рыбу и продовать ее в магазине и 
    получать с этого деньги. В этой игре вы должны купить себе дом!! Не приятоной игры!!(ВЫХОДА НЕТ)!!''')
    input('\nНажмите ENTER, чтобы продолжить')

if __name__ == '__main__':
    start()
    main()