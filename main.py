from itertools import product
from re import A
from fishing import Fishing
from holodos import Holodos
from magaz import Magaz
from pers import Pers
from sadok import Sadok

FISHING = Fishing()
MAGAZ = Magaz()
PERS = Pers()
SADOK = Sadok()
HOLODOS = Holodos()

p = \n
PERS.golod = a
PERS.happy = b
PERS.son = c

def fishing():
    print ('\n'*20)
    FISHING.go_fishing()
    fish=FISHING.go_fishing()
    if fish == None:
        print('Эх укатилась рыбешка')
    else:
        SADOK.add(fish)
        print('Вы поймали :', fish)
    input()

def sadok():
    print ('\n'*20)
    print(SADOK)
    s = input('Вы хотететь продать кошке?')
    if s== ('да') and ('yes') and ('+'):
        PERS.money+=SADOK.bue()
    else:
        print("Вы обидели кошку")

def eat():
    print(HOLODOS)
    tea=input('Вы берите еду(Номер прдукта!!!!)')
    if tea.isnumeric() == True :
        product=Holodos.delet(int(tea))
        if product != None
        if product.id_ == 0:
            PERS.golod += product.stats
        if product.id_ == 1:
            PERS.son += product.stats
        if product.id_ == 2:
            PERS.happy += product.stats
        else:
            print('Ошибка NOOOOO')
        print('Вы накормили Серегу:,\n produkt')
        input('\n\nНажмите ENTER, чтобы продолжить')
        print(p*50)
    else:
        print('вы ввели не верное число!!!')
        input('\n\nНажмите ENTER, чтобы продолжить')

def magaz():
    print ('\n'*20)
    print(MAGAZ)
    vib = input("Выберите еду для Сереги :")
    if vib.isdigit():
        product = MAGAZ.duy(int(vib))
        if product !=None:
            if PERS.money>=product.price:
                PERS.money -= product.price
                HOLODOS.add(product)
            else:
                print("У вас недостаточно средств")
        else:
            print('Вы ввели неверное число')
    else:
        print('Вы ввели неверное  не число!!')


def sleep():
    pass

def happe():
    pass

def finish():
    pass

def dayHaus():
    print ('\n'*20)
    pass

def exit():
    print ('\n'*20)
    input('Вы уверны что хотите выйти:\n')
    if ('да') and ('yes') and ('+'):
        input('\nНажмите ENTER, чтобы продолжить')
        exit()
    else:
        input('\nНажмите ENTER, чтобы продолжить')

def choise(go:str):
    if go == '1':
        fishing()
    elif go =='2':
        eat()
    else:
        print('вы ввели не верное действие')
    

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
    choise(go)
    main()

def  start():
    print('''Добро Пожалвать в игру про рыбалку! Не приятной игры!!!(ВЫХОДА НЕТ)!''')
    input('\nНажмите ENTER, чтобы продолжить')

if __name__ == '__main__':
    start()
    main()