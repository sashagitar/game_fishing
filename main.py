from fishing import Fishing
from holodos import Holodos
from magaz import Magaz
from PERS import PERS
from sadok import Sadok

FISHING = Fishing()
MAGAZ = Magaz()
PERS = PERS()
SADOK = Sadok()
HOLODOS = Holodos()


def fishing():
    print ('\n'*20)
    FISHING.go_fishing()
    fish=FISHING.go_fishing()
    if fish == None:
        print('Эх соход')
    else:
        SADOK.add(fish)
        print('Вы поймали :', fish)
    input()
def sadok():
    print ('\n'*20)
    print(SADOK)
    s = input('Вы хотететь продать кошке?')
    if s== ('да') and ('возможно') and ('1110010011100000') and ('+'):
        PERS.money+=SADOK.bue()
    else:
        print("Вы обидели кошку.(Пощады не ждите)")


def holodos():
    print(HOLODOS)
    tea=input('Вы берите еду')
    if tea.isdigit() == True : 
        product=Holodos.delete(int(tea))
        if product != None:
            if product.id_ == 0:
                PERS.golod += product.stats
            if product.id_ == 1:
                PERS.son += product.stats
            if product.id_ == 2:
                PERS.happy += product.stats
            else:
                print("Ошибка")
        else:
            print('Вы ввели неверное число')
    else:
        print('Вы ввели неверное  не число!!')
       
        print('Вы накормили шлёпу',product)
        input('\nНажмите ENTER, чтобы продолжить')
    if tea.isnumeric() == False :
        print('Вы ввели буквы!!!')
        input('\nНажмите ENTER, чтобы продолжить')
    else:
        print('Вы ввели неверное число!!')
        input('\nНажмите ENTER, чтобы продолжить')


def magaz():
    print ('\n'*20)
    print(MAGAZ)
    vib = input("Выберите еду для Шлёпы :")
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
    print('''
    Выберите действие:
        1.Поиграть в футбол
        2.Пойти в бар
        3.Пойти в ночной клуб
        4.Посмотреть телевизор
        5.Поспать 
    ''')
    perehod = input('Выберите действие(НОМЕР!!!):\n')
    try:
        if (perehod == '') :
            print('Введено неправлельное значение')
        elif int(perehod) > 5 :
            print('Введено неправлельное значение')
    except ValueError:
            print('Введено неправлельное значение')
    if perehod == '1' :
        if (Time >= 9) and (Time < 21): ###Если день
            PERS.sleep -= 10
            PERS.eat -= 10
            PERS.happy += 30
        else: ###Если ночь
            PERS.sleep -= 20
            PERS.eat -= 10
            PERS.happy += 20
    if perehod.lower() == '2' :
        if (Time >= 9) and (Time < 21): ###Если день
            PERS.sleep -= 30
            PERS.eat += 20
            PERS.happy  += 10
        else: ###Если ночь
            PERS.sleep -= 50
            PERS.eat += 10
            PERS.happy  += 20
    if perehod.lower() == '3' :
        if (Time >= 9) and (Time < 21): ###Если день
            PERS.sleep -= 10
            PERS.eat -= 30
            PERS.happy += 89
        else: ###Если ночь
            PERS.sleep -= 30
            PERS.eat += 30
            PERS.happy  += 99
    if perehod.lower() == '4' :
        if (Time >= 9) and (Time < 21): ###Если день
            PERS.sleep -= 30
            PERS.eat += 20
            PERS.happy  += 10
        else: ###Если ночь
            PERS.sleep -= 10
            PERS.eat += 10
            PERS.happy  += 20
    if perehod.lower() == '5' :
        if sleep < 70 :
            if (Time >= 9) and (Time < 21): ###Если день
                PERS.sleep = 100
                PERS.live = 100
                PERS.eat = 20
            elif (Time >= 21) | ((Time >= 0 ) & (Time < 6)): ###Если ночь
                PERS.sleep = 100
                PERS.live = 100
                PERS.eat = 15
            elif Time == 6 :
                PERS.sleep = 70
                PERS.live = 100
                PERS.eat = 5
        else:
            print('Вы достаточно поспали')
    input('\n\nНажмите ENTER, чтобы продолжить')
    print('\n'*50)

def finish():
    pass

def dayHaus():
    print ('\n'*20)
    pass

def exit():
    print ('\n'*20)
    input('Вы уверны что хотите выйти:\n')
    if ('да') and ('возможно') and ('1110010011100000'):
        input('\nНажмите ENTER, чтобы продолжить')
        exit()
    else:
        input('\nНажмите ENTER, чтобы продолжить')

def choise(go:str):
    swith = {
        '1' : fishing,
        '2' : holodos,
        '3' : magaz,
        '4' : sadok,
        '5' : dayHaus,
        '6' : exit
    }
    swith.get(go, lambda: 'вы ввели не верное число')()
    

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
    print('''Добро Пожалвать в игру про рыбалку!(ВЫХОДА НЕТ)!''')
    input('\nНажмите ENTER, чтобы продолжить')

if __name__ == '__main__':
    start()
    main()