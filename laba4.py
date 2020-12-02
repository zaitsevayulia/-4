class Garbage:
    def __init__(self, name):
        self.name = name
        self.usefull = 100

    def message(self):
        print('Разделяйте мусор правильно!')


class Organic(Garbage):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def foodworm(self):
        if self.size < 15:
            self.usefull -= 90
            print('Полезность:', self.usefull, 'Покормите червей чем-то покрупнее')

    def thankyou(self):
        if self.usefull > 10:
            print('Черви благодарны вам!')

    def sort(self):
        print('Скормить червям', self.usefull)


class Paper(Garbage):
    def __init__(self, name, useless):
        super().__init__(name)
        self.useless = useless

    def newUsefull(self):
        if self.useless is True:
            self.usefull = 0
            print('Бесполезный мусор :(')

    def sort(self):
        if self.usefull > 0:
            print('Отвезти в Мегу', self.usefull)
        else:
            m.newUsefull()


class Plastic(Garbage):
    def __init__(self, name, fraction):
        super().__init__(name)
        self.fraction = fraction
        self.sound = 3

    def sort(self):
        if self.fraction == 1:
            self.usefull += 1
            print('Сомните и сдайте в контейнер', self.usefull)
        elif self.fraction == 2 or self.fraction == 5:
            self.usefull += 10
            print('Сдайте на благотворительность', self.usefull)
        else:
            print('Ждите раздельного сбора или выбрасывайте')

    def __bool__(self):
        return True if self.fraction else False


class Metall(Garbage):
    def __init__(self, name):
        super().__init__(name)

    def sort(self):
        print('Вымойте и отвезите в Мегу', self.usefull)


newspaper = Paper('newspaper', False)
newspaper.newUsefull()

cheque = Paper('cheque', True)
cheque.newUsefull()

apple = Organic('apple', 10)
apple.message()
apple.foodworm()
apple.thankyou()

cap = Plastic('cap', 1)
cap.sort()
print(cap.__bool__())

bottle = Metall('bottle')
trash = [apple, newspaper, cap, cheque, bottle]
for m in trash:
    m.sort()
