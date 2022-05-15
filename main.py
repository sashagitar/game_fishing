import random
from matplotlib import image
from matplotlib import pyplot as plt
from prodykt import Prodykt
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
    if s== ('да') and ('возможно') and ('+'):
        PERS.money+=SADOK.bue()
    else:
        print("Вы обидели кошку.(Пощады не ждите)")

def holodos():
    print(HOLODOS)
    tea=input('Вы берите еду')
    if tea.isdigit() == True : 
        product=Holodos.delet(int(tea))
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
    print(MAGAZ)
    mas = input("Выберите еду для Шлёпы :")
    if mas.isdigit():
        product = MAGAZ.duy(int(mas))
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
    print ('\n'*20)


def sleep():
    print(PERS)
    ot=input('хотите поспать?')
    if (ot=='yes'):
        PERS.son+=100
        PERS.happy=100
    pass

def happe():
    print('''
    Выберите действие:
        1.Поиграть в футбол
        2.Пойти в бар
        3.Пойти в ночной клуб
        4.Посмотреть телевизор
    ''')
    perehod = input('Выберите действие(НОМЕР!!!):\n')
    try:
        if (perehod == '') :
            print('Введено неправлельное значение')
        elif int(perehod) > 4 :
            print('Введено неправлельное значение')
    except ValueError:
            print('Введено неправлельное значение')
    if perehod == '1' :
            ###Если день
            PERS.sleep -= 10
            PERS.golod -= 10
            PERS.happy += 30
    if perehod.lower() == '2' :
        ###Если день
            PERS.sleep -= 30
            PERS.golod += 20
            PERS.happy  += 10
    if perehod.lower() == '3' :
        ###Если день
            PERS.sleep -= 10
            PERS.golod -= 30
            PERS.happy += 89
    if perehod.lower() == '4' :
        ###Если день
            PERS.sleep -= 30
            PERS.golod += 20
            PERS.happy  += 10
    input('\n\nНажмите ENTER, чтобы продолжить')
    print('\n'*50)


def finish():
    a = random.randint(0,100)
    if a == 1:
        img = image.imread(r"imagefish\mem.jpg")
        print(type(img))
        print(img.shape)
        plt.imshow(img)
        plt.show()
        print("Легендарная концовка")
        print('Вы умерли')
        exit()
    else:
        img = image.imread(r"imagefish\Minecraft.jpg")
        print(type(img))
        print(img.shape)
        plt.imshow(img)
        plt.show()
        print('Вы умерли')
        exit()

def dayHaus():
    if PERS.money < 1000000:
        print('Вам не хвотает денег!!\n')
    else:
        sas = input('Ходите купить дом? \n')
        if sas == ('да') and ('возможно'):
            PERS.money -= 1000000
            PERS.home += 'Дом'
            print('ПОЗДРАВЛЯЮ!! Вы купили дом')
            print('Игра окончина!!!')
            exit()
        else:
            if sas== ('нет') and ('no'):
                input('\nНажмите ENTER, чтобы продолжить')
          

def exit_():
    print ('\n'*20)
    ass = input('Вы уверны что хотите выйти:\n')
    if ass == ('да') and ('возможно'):
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
        '6' : exit_
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