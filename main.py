from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    ATTACK_RANGE = (1, 3)    #Непонятна логика назначения дефолтных переменнх. Можно ведь их просто в качестве аргументов передавать из переменных подкласса
    DEFENCE_RANGE = (1, 5)
    SKILL = 'Удача'
    SKILL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name


    def attack(self):
        damage = f'{DEFAULT_ATTACK + randint(*self.ATTACK_RANGE)} урона' # Посмотреть, как работает звёздочка перед self
        return f'{self.name} нанёс урон противнику равный {damage}'
    

    def defence(self):
        block = f'{DEFAULT_DEFENCE + randint(*self.DEFENCE_RANGE)} урона'
        return f'{self.name} блокировал {block}'
    
    def special(self):
        return (f'{self.name} применил специальное умение '
                f' <<{self.SKILL} {self.SKILL_BUFF}»')
    
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'
    

    # def start_training(self):


class Warrior(Character):
    ATTACK_RANGE = (3, 5)
    DEFENCE_RANGE = (5, 10)
    SKILL = 'Выносливость'
    SKILL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. Сильный, выносливый '
                             'и отважный.')

    def __init__(self, name):
        super().__init__(name)
 

class Mage(Character):
    ATTACK_RANGE = (5, 10)
    DEFENCE_RANGE = (-2, 2)
    SKILL = 'Атака'
    SKILL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. Обладает высоким '
                             'интеллектом.')
    
    def __init__(self, name):
        super().__init__(name)


class Healer(Character):
    ATTACK_RANGE = (-3, -1)
    DEFENCE_RANGE = (2, 5)
    SKILL = 'Защита'
    SKILL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = ('могущественный заклинатель. Черпает силы из '
                             'природы, веры и духов.')
    
    def __init__(self, name):
        super().__init__(name)

warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())