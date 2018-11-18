# животные, родительский    
class Animals:
    sum_weight = 0                                      # общий вес популяции
    max_weight = 0                                      # максимальный вес особи
    name_animal_max_weight = ''
    def __init__(self,name, weight):                    # задать имя, вес
        self.name = name
        self.weight = weight
        Animals.sum_weight += self.weight               # определение массы всех животных
        if self.weight > Animals.max_weight:            # определение имени животного с максимальным весом
            Animals.max_weight = self.weight
            Animals.name_animal_max_weight = self.name

    def feed(self):                                     # все умеют есть
        print('Вы покормили %s!' %  (self.name))

# домашняя птица
class Livestock(Animals):
    def give_eggs(self):
        print(self.name, 'дает яйцо')
#    гусь
class Goose(Livestock):
    vox = 'Га-га-га'
    def give_voice(self):
        print(self.vox)
#    курица
class Hen(Livestock):
    vox = 'Ко-ко-ко'
    def give_voice(self):
        print(self.vox)
#    утка
class Duck(Livestock):
    vox = 'Кря-кря-кря'
    def give_voice(self):
        print(self.vox)

# домашняя скотина
class Fowl(Animals):
    pass
#   корова
class Cow(Fowl):
    vox = 'Му-му-мууу'
    def give_voice(self):
        print(self.vox)
    
    def give_milk(self):
        print('Корова %s дала молоко' % (self.name))
#   овца
class Sheep(Fowl):
    vox = 'Беее'
    def give_voice(self):
        print(self.vox)

    def trim(self):
        print('Овца %s поделилась шерстью' % (self.name))
#   коза
class Goat(Fowl):
    vox = 'Бйяяя'
    def give_voice(self):
        print(self.vox)

    def give_milk(self):
        print('Коза %s дала молоко' % (self.name))

weight_list = {}                                         # листок для записи веса

# ... и был день пятый, и создал Бог птиц...
White = Goose('Белый', 2.99)
Grey = Goose('Серый', 3.99)
Koko = Hen('Коко', 1)
Kukareku = Hen('Кукареку', 1.25)
Kryakva = Duck('Кряква', 1.5)
weight_list = [White.weight, Grey.weight, Koko.weight, Kukareku.weight, Kryakva.weight] # вносим вес скота
# ... и настал день шестой, и создал Бог животных...
Manya = Cow('Манька', 250)
Barashek = Sheep('Барашек', 110)
Kudryavyi = Sheep('Кудрявый', 100)
Roga = Goat('Рога', 88)
Kopyta = Goat('Копыта', 99)
weight_list += [Manya.weight, Barashek.weight, Kudryavyi.weight, Roga.weight, Kopyta.weight]    # добавляем еще веса копытных

print('Добро пожаловать на ферму дяди Вани, бывшую ферму дяди Джо, который в России спился и застрелился!', 'Здесь проживают:', sep='\n')
print('Корова по кличке %s весом %d кг.' % (Manya.name, Manya.weight))
print('Овцы %s и %s весом %d и %d кг. соответственно.' % (Barashek.name, Kudryavyi.name, Barashek.weight, Kudryavyi.weight))
print('Козы %s и %s весом %d и %d кг. соответственно.' % (Roga.name, Kopyta.name, Roga.weight, Kopyta.weight))
print('Курицы %s и %s весом %.2f и %.2f кг.' % (Koko.name, Kukareku.name, Koko.weight, Kukareku.weight))
print('Гуси %s и %s весом %.2f и %.2f кг.' % (Grey.name, White.name, Grey.weight, White.weight))
print('Утка %s весом %.2f кг.' % (Kryakva.name, Kryakva.weight))

print('Общий вес животных составляет:', Animals.sum_weight, 'кг.')

weight_list.sort(reverse=True)
print('Самое тяжелое животное весит %.2f кг. Его кличка %s.' % (weight_list[0], Animals.name_animal_max_weight))

print('\nЧто тут происходит? Да все замечательно, все здоровы и довольны:')
Manya.give_milk(); Barashek.trim(); Kudryavyi.trim(); Roga.give_milk(); Kopyta.give_milk()         # кто какую пользу приносит
for obj in [White, Grey, Koko, Kukareku, Kryakva]:
    obj.give_eggs()

s = ''
i = 0
while s not in ('y', 'n'):
    print('Хотите покормить животных? (y/n)')
    s = input()
    if s == 'n':
        break
    elif s == 'y' and i <= 2:
        for obj in [Manya, Barashek, Kudryavyi, Roga, Kopyta, Koko, Kukareku, Kryakva, Grey, White]:        # накормить всех
            obj.feed()
        i += 1
    if i >= 2 and s == 'y':
        print('Довольно! Дядя Ваня будет сердиться!')
    s = ''

print('\nУже уходите? И чаю не выпьете?')
print('Корова %s промычала вам' % (Manya.name))
Manya.give_voice()
print('Овцы %s и %s посылают вам' % (Barashek.name, Kudryavyi.name))
Barashek.give_voice(); Kudryavyi.give_voice()
print('Козы %s и %s блеют вам' % (Roga.name, Kopyta.name))
Roga.give_voice(); Kopyta.give_voice()
print('Курицы %s и %s посылают вам' % (Koko.name, Kukareku.name))
Koko.give_voice(); Kukareku.give_voice()
print('Утка %s крякает вам' % (Kryakva.name))
Kryakva.give_voice()
print('Гуси %s и %s кричат вам' % (Grey.name, White.name))
Grey.give_voice(); White.give_voice()