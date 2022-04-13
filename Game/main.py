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
    print ('\n'*20)
    FISHING.go_fishing
    pass

def sadok():
    print ('\n'*20)
    pass

def eat():
    pass

def magaz():
    print ('\n'*20)
    pass

def sleep():
    pass

def happe():
    pass

def finish():
    pass

def dayHaus():
    print ('\n'*20)
    pass

def exet():
    print ('\n'*20)
    w=input('Вы уверины что хотите выйти из игры?')
    if w == 'да':
        exit()
    pass


def main():
    print ('\n'*20)
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
    ''')
    go = input('\n(Введите число или слово)\n')
    switch = {
        '1': fishing(),
        '2': eat(),
        '3': magaz(),
        '4': sadok(),
        '5': dayHaus(),
        '6': exet(),
    }

def  start():
    print('''Добро Пожалвать в игру про рыбалку!(ВЫХОДА НЕТ)!''')
    input('\nНажмите ENTER, чтобы продолжить')

if __name__ == '__main__':
    start()
    main()