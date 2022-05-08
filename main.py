from fish import Fish
from fishing import Fishing
from holodos import Holodos
from magaz import Magazin
from pers import Pers
from prodykt import Prodykt
from sadok import Sadok

FISHING = Fishing()
MAGAZ = Magazin()
PERS = Pers()
SADOK = Sadok()
HOLODOS = Holodos()
def fishing():
    print ('\n'*20)
    if Fish != None:
        sadok.Add(Fish)

    pass

def sadok():
    print(SADOK)
    input('хотите продать рыбу')
    if ('yes') :
        PERS.money+=SADOK
    pass

def eat():
    pass

def magaz():
    print(MAGAZ)
    vib=input('что хочешь купить')
    if vib.isdigit():
        prodykt=Magazin.bue(int(vib))
        if prodykt!=None:
            if PERS.money>Prodykt.price:
                HOLODOS.Add(prodykt)
                PERS.money==prodykt.price
            else:
                print('не достаточно денег')
        else:
            print('вы ввели неправ число')
    else:
        print('вы ввели не число')


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
    else:
        input('\нажмите ENTER, чтобы продолжить')
    


def choise(go:str):
    if go =='1':
        fishing()
    elif go=='2':
        eat()
    else:
        print('вы ввели неверное действие')

    

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
    switch.get(go, '')
    main()

def  start():
    print('''Добро Пожалвать в игру про рыбалку!(ВЫХОДА НЕТ)!''')
    input('\nНажмите ENTER, чтобы продолжить')

if __name__ == '__main__':
    start()
    main()