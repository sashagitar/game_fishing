from matplotlib import image
from matplotlib import pyplot as plt
import random
op=input("Введите ник-")
print(f'''Привет меня зовут {op},и я стал бомжом.
И единственное что у меня осталось -это дедушкина удочка.
И я должен наловить рыбы себе на дом''')
live = 100 ###Жизнь
money = 10 ### солько накопеных денег на дом
karas=0
lesh=0
karp=0
ok=0
som=0
j=0
klad=75
fg=0
hf=0
lin=0
ghk=int(0)
ghj=0
plo=0
r=0
vyn=0
promo1="Pusha2022"
promo=[]
sadok=[]
eat = 70 ###Голод
Time = 9 ###Время - день\ночь
day = 1 ###Какой сейчас день
money = 100 ###Деньги
sa=bool()
go = None ###Действие
p = '\n'
holodos = [('Буханка хлеба','25','руб','20'),('Колбаса','150','руб','60')] ###Холодильник
perehod = None ###Вспомогательная переменная действия
magaz = [('Буханка хлеба','25','руб','20'),('Колбаса','150','руб','60'),('Молоко','40','руб','35'),
('Бич-пакет','15','руб','10'),('Огурцы','20','руб/кг','15'),('Помидоры','35','руб/кг','25'),
('Сыр','120','руб','50'),('Пельмени','150','руб','70'),('Макароны','60','руб','45'),
('Тушёнка','70','руб','50'),('Кофе','50','руб','20'),('Чай','15','руб','10')] ###Магазин
kost = 0 ###Счётчик int
i = None ###Счётчик

while True:
    if Time  == 24 :
        Time = 0
        day += 1
    if Time == 27 :
        Time = 3
        day += 1
    print('День ', day )
    if(24<Time):
        day+=1
        Time-=24
    if (Time > 5) & (Time <= 10) : ###Часы
        print('Время', Time, 'утра' )
    elif (Time > 10) & (Time <= 18) :
        print('Время', Time, 'дня' )
    elif (Time > 18) & (Time <= 21) :
        print('Время', Time, 'вечера' )
    elif (Time > 21) | (Time >= 0) & (Time <= 5) :
        print('Время', Time, 'ночи' )
    print('Ваши статы:')
    print('Здоровье = ',live)
    print('Сытость = ', eat)
    print('Деньги = ', money,' руб')
    print(p*1)
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
    if (go.lower() == '8') | (go.lower() == 'Промокод'):
        promo=str(input('Введите промокод '))
        if(promo==promo1):
            klad+=20
            print("Промокод актевирован(+20% К выподению клада)")
            promo1=[]
        else:
            print("Введён неверный или не действительный промокод")
 
    if (go.lower() == '7') | (go.lower() == 'Настойки'):
        ghj=int(input("Включить(1) или выключить(0) "))
    if (go.lower() == '1') | (go.lower() == 'Порыбачить'):
        if(0<ghj):
            img = image.imread(r"water.jpg")
            print(type(img))
            print(img.shape)
            plt.imshow(img)
            plt.show()
        else:
            print()
        if (Time >= 9) and (Time < 21): ###Если день
            perehod = random.randint(3,10)
            eat -= 10
            Time += 2
        else: ###Если ночь
            perehod = random.randint(10,20)
            eat -= 20
            Time += 3
        sa=random.randint(0,99)
        print(sa)
        if(sa<2):
            if(0<ghj):
                img = image.imread(r"karas.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("karas")
            karas+=1
            sadok.append("karas")
        if(2<sa<5):
            if(0<ghj):
                img = image.imread(r"karp.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("kerp")
            sadok.append("karp")
            karp+=1
        if(5<sa<18):
            if(0<ghj):
                img = image.imread(r"lesh.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("лещ")
            sadok.append("lash")
            lesh+=1
        if(18<sa<29):
            if(0<ghj):
                img = image.imread(r"vyn.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            print("Вьюн")
            vyn+=1
            sadok.append("Вьюн")
        if(29<sa<35):
            if(0<ghj):
                img = image.imread(r"com.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("сом")
            sadok.append("сом")
            som+=1
        if(35<sa<40):
            if(0<ghj):
                img = image.imread(r"az.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Жерих")
            sadok.append("жерих")
            j+=1
        if(40<sa<47):
            if(0<ghj):
                img = image.imread(r"ersh.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("ёрж")
            r+=1
            sadok.append("ёрж")
        if(47<sa<55):
            if(0<ghj):
                img = image.imread(r"Плотва.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Плотва")
            sadok.append("Плотва")
            plo+=1
        if(55<sa<66):
            if(0<ghj):
                img = image.imread(r"lin.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Линь")
            sadok.append("Линь")
            lin+=1
        if(66<sa<72):
            if(0<ghj):
                img = image.imread(r"shyka.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Щука")
            fg+=1
            sadok.append("Щука")
        if(74<sa<klad):
            if(0<ghj):
                img = image.imread(r"klad.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Клад")
            money+=random.randint(100,12022)
        if(75<sa<85):
            if(0<ghj):
                img = image.imread(r"kartinki-okun-38.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Окунь")
            sadok.append("Окунь")
            ok+=1
        if(85<sa<100):
            if(0<ghj):
                img = image.imread(r"Berh.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print("Верхоплавка")
            sadok.append("Верхоплавка")
            hf+=1
    if (go.lower() == '3') | (go.lower() == 'Рынок'):
        print('Рынок')
        money+=karas*20
        money+=karp*100
        money+=lesh*50
        money+=hf*45
        money+=r*65
        money+=fg*564
        money+=som*2000
        money+=ok*76
        money+=j*867
        money+=lin*100
        money+=plo*50
        money+=vyn*250
        sadok=[]
        karas=0
        karp=0
        lesh=0
        hf=0
        r=0
        fg=0
        som=0
        ok=0
        j=0
        lin=0
        plo=0
        vyn=0
        print('Cадок', sadok)
    if (go.lower() == '4') | (go.lower() == 'Садок'):
        print("карасей", karas)
        print("карпов", karp)
        print("лещей", lesh)
        print("Верхоплавок", hf)
        print("ёржей", r)
        print("Щук", fg)
        print("Сомов", som)
        print("окуней", ok)
        print("Жерихов", j)
        print("Линей", lin)
        print("Плотва", plo)
        print("Вьюнов", vyn)
        input('\nНажмите ENTER, чтобы продолжить')
    if (go.lower() == '5') | (go.lower() == 'Купить дом'):
        if(money>100000):
            if(0<ghj):
                img = image.imread(r"dom.jpg")
                print(type(img))
                print(img.shape)
                plt.imshow(img)

                plt.show()
            else:
                print()
            print('''ВЫ прошли игру поздровляем''')
            break
        if(money<100000):
            print("Вас выкинули из агенства недвижемости ")
    if (go.lower() == '2') | (go.lower() == 'покушать'):
        kost = 0
        print('вы заглядываете в инвентарь, там:')
        if holodos == [] :
                print('*ПУСТО*')
        else: ###Выводит что в инвентаре
            for i in holodos :
                if i[0] == 'Кофе' :
                    print(kost + 1,'. ', i[0],', даёт бодрости - ', i[3])
                elif  i[0] == 'Чай' :
                    print(kost + 1,'. ', i[0],', Прибовляет желания жить - ', i[3])
                else:
                    print(kost + 1,'. ', i[0],', даёт сытости - ', i[3])
                kost += 1
        perehod = input('выберите, "кушать" или идити в "магазин"\n')
        if perehod.lower() == 'кушать' :
            perehod = input('Введите номер продукта:')
            live+=20
            try:
                perehod = (int(perehod)-1)
                if (kost <= (perehod)) | (perehod <= -1)  :
                    print('Введено неверное значение')
##############################################################################################
                    if (Time >= 9) and (Time < 21): ###Если день
                        Time += 2
                    else: ###Если ночь
                        Time += 3
                    del holodos[perehod]
                else:
                    eat += int(holodos[perehod][3])
                    if (Time >= 9) and (Time < 21): ###Если день
                        Time += 2
                    else: ###Если ночь
                        Time += 3
                    del holodos[perehod]
            except ValueError:
                print('Это не число!')
           
        elif perehod.lower() == 'магазин' :
            kost = 0
            for i in magaz : ### Выводит магазин
                if holodos == () :
                   print('*ПУСТО*')
                elif i[0] == 'Кофе' :
                    print(kost + 1,'. ', i[0], '- стоит',i[1],i[2],', даёт бодрости - ', i[3])
                elif  i[0] == 'Чай' :
                    print(kost + 1,'. ', i[0], '- стоит',i[1],i[2],', прибавляет желания жить - ', i[3])
                else:
                    print(kost + 1,'. ', i[0], '- стоит',i[1],i[2],', даёт сытости - ',i[3])
                kost += 1
            kost = input('сколько продукктов вы хотите купить?') 
            if (kost == '') :
                print('Введено неверное значение')
                input('Нажмите ENTER чтобы вернуться')
                kost = 0
            try:
                kost = int(kost)
                if (kost <= 0) : 
                    print('Введено неверное значение')
                    input('Нажмите ENTER чтобы вернуться')
                if (kost > 0) & (Time >= 9) & (Time < 21) : ###Если день
                    Time += 2
                elif (kost > 0): ###Если ночь
                    Time += 3
                while kost > 0: ### Прцесс покупки
                    perehod = int(input('Введите номер продукта(ЧИСЛО!!!!):'))-1
                    if (perehod < 0) | (perehod > 12) :
                        print('Такого продукта нет')
                    elif (money - int(magaz[perehod][1])) >= 0 :
                        holodos.append(magaz[perehod])
                        money-= int(magaz[perehod][1])
                        print('у вас осталось =',money,'руб.')
                        kost -= 1
                    else:
                        print('Недостаточно средств!')
                        kost -= 1
            except ValueError:
                print('Это не число!')
                input('Нажмите ENTER чтобы вернуться')
        else:
            print('Вы ввели не правильное сообщение')
            input('Нажмите ENTER чтобы вернуться')
#######################################################################################################
                
        if (Time >= 9) and (Time < 21): ###Если день
            eat -= 5
            Time += 2
        else: ###Если ночь
            eat -= 5
            Time += 3
        if (Time >= 9) and (Time < 21): ###Если день
            eat -= 5
            Time += 2
        else: ###Если ночь
########################################################################################################################################
            if (Time >= 9) and (Time < 21): ###Если день
                eat -= 20
                Time += 2
            elif (Time >= 21) | ((Time >= 0 ) & (Time < 6)): ###Если ночь
                    eat -= 5
                    Time += 6
            elif Time == 6 :
                    eat -= 25
                    Time += 3
            else:
                print('')
#######################################################################################################################
    if (go.lower() == '6') | (go.lower() == 'выход') :
        perehod = input('Вы уверены? Прогресс будет утерян.\n')
        if perehod.lower() == 'да' :
            break 
    if(live<50):
        print('Следите за здоровьем а то умрете!!!!!')
    if(live<0):    
        img = image.imread(r"mem.jpg")
        print(type(img))
        print(img.shape)
        plt.imshow(img)

        plt.show()
        print('Вы умерли')
        break
    input('\n\nНажмите ENTER, чтобы продолжить')
    if (go == '') | (go.lower() != ('1')) & (go.lower() != ('2')) & (go.lower() != ('3')) & (go.lower() != ('4')) & (go.lower() != ('5')) & (go.lower() != ('6')) & (go.lower() != ('кодить')) & (go.lower() != ('покушать')) & (go.lower() != ('расслабиться')) & (go.lower() != ('подзаратотать')) & (go.lower() != ('попросить отсрочку')) & (go.lower() != ('выход')):
        print('Введено не верное значение')     
    if eat <=5 :
        live -= 5
        print('Вы очень голодны, если так будет продолжаться, то вы умрёте от голода!')
    if eat < 0 :
        eat = 0
    if eat > 150 :
        eat = 70
        print('вы переели и прочистились')
    if (live <= 10) & (eat >= 70) :
        live += 15

go = None
i = None
perehod = None
Kost = 0
print('Ваши статы:')
print('День ', day )
if (Time > 5) & (Time <= 10) : ###Часы
    print('Время', Time, 'утра' )
elif (Time > 10) & (Time <= 18) :
    print('Время', Time, 'дня' )
elif (Time > 18) & (Time <= 21) :
    print('Время', Time, 'вечера' )
elif (Time > 21) | (Time > 0) & (Time <= 5) :
    print('Время', Time, 'ночи' )
print('Здоровье = ',live)
print('Голод = ', eat)
print('Деньги = ', money,' руб')
input('\n Нажмите ENTER, чтобы закончить')
