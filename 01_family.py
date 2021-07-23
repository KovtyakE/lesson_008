# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return '-----Дом----- \nДенег: {} \nЕды: {} \nКошачьей еды: {} \nГрязи: {}'.format(
            self.money, self.food, self.cat_food, self.dirt)

    def daily_dust(self):
        self.dirt += 5
        cprint('В доме за ночь накопилось немного пыли', color='white')


class Husband:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.hungry_count = 0
        self.is_alive = True

    def __str__(self):
        # return super().__str__()
        return '{} сытость {} счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if home.food >= 30:
            self.fullness += 30
            home.food -= 30
            self.hungry_count = 0
            cprint('{} поел'.format(self.name), color='green')
        elif 20 >= home.food > 0:
            self.fullness += home.food
            home.food = 0
            self.hungry_count = 0
            cprint('{} доел остатки еды'.format(self.name), color='green')
        else:
            cprint('{}: Нет еды!'.format(self.name), color='red')
            self.hungry_count += 1
            if self.hungry_count == 3:
                self.fullness = 0

    def work(self):
        self.fullness -= 10
        self.happiness -= 5
        home.money += 150
        cprint('{} сходил на работу'.format(self.name), color='blue')

    def gaming(self):
        self.fullness -= 10
        if self.happiness <= 80:
            self.happiness += 20
        cprint('{} играл в Genshin Impact'.format(self.name), color='magenta')

    def pet_the_cat(self):
        self.fullness -= 10
        which_cat_to_pet = randint(0, len(cats) - 1)
        if self.happiness <= 95:
            self.happiness += 5
        cprint('{} гладил кота по имени {}'.format(self.name, cats[which_cat_to_pet].name), color='magenta')

    def act(self):
        if home.dirt > 90:
            self.happiness -= 10
        dice = randint(1, 6)
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            self.is_alive = False
        elif self.happiness < 5:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            self.is_alive = False
        elif self.fullness < 50:
            self.eat()
        elif self.happiness < 40:
            self.gaming()
        elif home.money < 100:
            self.work()
        elif dice == 1:
            self.gaming()
        elif dice == 3 and self.fullness < 100:
            self.eat()
        elif dice == 4:
            self.pet_the_cat()
        else:
            self.work()


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.hungry_count = 0
        self.is_alive = True

    def __str__(self):
        # return super().__str__()
        return '{} сытость {} счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if home.food >= 30:
            self.fullness += 30
            home.food -= 30
            self.hungry_count = 0
            cprint('{} поела'.format(self.name), color='green')
        elif 20 >= home.food > 0:
            self.fullness += home.food
            home.food = 0
            self.hungry_count = 0
            cprint('{} доела остатки еды'.format(self.name), color='green')
        else:
            cprint('{}: Нет еды!'.format(self.name), color='red')
            self.hungry_count += 1
            if self.hungry_count == 3:
                self.fullness = 0

    def shopping(self):
        self.fullness -= 10
        if home.food <= 90:
            home.money -= 50
            home.food += 50
        if home.cat_food <= 70:
            home.money -= 50
            home.cat_food += 50
        cprint('{} сходила в магазин за продуктами'.format(self.name), color='green')

    def buy_fur_coat(self):
        home.money -= 350
        self.happiness += 60
        cprint('{} купила себе шубку'.format(self.name), color='magenta')

    def clean_house(self):
        self.fullness -= 10
        self.happiness -= 5
        if home.dirt <= 100:
            home.dirt = 0
            cprint('{} убралась в доме'.format(self.name), color='white')
        else:
            home.dirt -= 100
            cprint('{} убралась в доме'.format(self.name), color='white')

    def gaming(self):
        self.fullness -= 10
        if self.happiness <= 90:
            self.happiness += 10
        cprint('{} играла в Genshin Impact'.format(self.name), color='magenta')

    def pet_the_cat(self):
        self.fullness -= 10
        which_cat_to_pet = randint(0, len(cats) - 1)
        if self.happiness <= 95:
            self.happiness += 5
        cprint('{} гладила кота по имени {}'.format(self.name, cats[which_cat_to_pet].name), color='magenta')

    def act(self):
        if home.dirt > 90:
            self.happiness -= 10
        dice = randint(1, 6)
        if self.fullness <= 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
            self.is_alive = False
        elif self.happiness < 5:
            cprint('{} умерла от депрессии'.format(self.name), color='red')
            self.is_alive = False
        elif home.cat_food == 0 and home.money >= 100:
            self.shopping()
        elif self.fullness < 50:
            self.eat()
        elif self.happiness < 50 and home.money >= 350:
            self.buy_fur_coat()
        elif (home.food < 100 or home.cat_food < 80) and home.money >= 100:
            self.shopping()
        elif home.dirt >= 90:
            self.clean_house()
        elif (dice == 1 or dice == 2) and home.dirt >= 40:
            self.clean_house()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.eat()
        elif dice == 5:
            self.pet_the_cat()
        else:
            self.gaming()


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.fullness = 30
        self.name = name
        self.hungry_count = 0
        self.is_alive = True

    def __str__(self):
        # return super().__str__()
        return 'Кот {} сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if home.cat_food >= 10:
            self.fullness += 20
            home.cat_food -= 10
            self.hungry_count = 0
            cprint('Кот {} поел)'.format(self.name), color='green')
        elif 10 > home.food > 0:
            self.fullness += home.cat_food
            home.cat_food = 0
            self.hungry_count = 0
            cprint('Кот {} доел остатки еды)'.format(self.name), color='green')
        else:
            cprint('Кот {}: Мяу!!! (Нет еды!)'.format(self.name), color='red')
            if self.hungry_count == 1:
                self.fullness = 0
            self.hungry_count += 1

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} спал весь день)'.format(self.name), color='white')

    def tear_wallpaper(self):
        self.fullness -= 10
        home.dirt += 5
        cprint('Кот {} дерёт обои)'.format(self.name), color='white')

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 0:
            cprint('Кот {} умер от голода'.format(self.name), color='red')
            self.is_alive = False
        elif self.fullness < 50:
            self.eat()
        elif (dice == 1 or dice == 2) and self.fullness < 90:
            self.eat()
        elif dice == 3 or dice == 4:
            self.sleep()
        else:
            self.tear_wallpaper()


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.hungry_count = 0
        self.is_alive = True

    def __str__(self):
        # return super().__str__()
        return 'Ребенок {} сытость {} счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if home.food >= 10:
            self.fullness += 10
            home.food -= 10
            self.hungry_count = 0
            cprint('{} поела'.format(self.name), color='green')
        else:
            cprint('{}: Нет еды!'.format(self.name), color='red')
            if self.hungry_count == 2:
                self.fullness = 0
            self.hungry_count += 1

    def sleep(self):
        self.fullness -= 10
        cprint('Ребёнок {} поспал'.format(self.name))

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            self.is_alive = False
        elif self.fullness < 50:
            self.eat()
        elif dice == 1 and self.fullness < 90:
            self.eat()
        else:
            self.sleep()


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
cats = [Cat(name='Мурзик'),
        Cat(name='Снежок')
        ]

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.daily_dust()
    serge.act()
    masha.act()
    kolya.act()
    for cat in cats:
        cat.act()
    if serge.is_alive:
        cprint(serge, color='cyan')
    if masha.is_alive:
        cprint(masha, color='cyan')
    if kolya.is_alive:
        cprint(kolya, color='cyan')
    for cat in cats:
        if cat.is_alive:
            cprint(cat, color='blue')
    cprint(home, color='yellow')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
