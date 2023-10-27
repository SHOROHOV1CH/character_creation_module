from random import randint

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    """Класс Персонаж."""
    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'

    def __init__(self, name: str) -> str:
        self.name = name

    def attack(self) -> str:
        """Возвращает сообщения о результатах цикла атаки персонажем."""
        damage = f'{DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)} урона'
        return f'{self.name} нанёс урон противнику равный {damage}'

    def defence(self) -> str:
        """Возвращает сообщения о результатах
        цикла блокирования урона персонажем."""
        block = f'{DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)} урона'
        return f'{self.name} блокировал {block}'

    def special(self) -> str:
        """Возвращает сообщения о результатах цикла
        применения специального умения персонажем."""
        return (f'{self.name} применил специальное умение '
                f' "{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    def __str__(self) -> str:
        """Возвращает описание класса персонажа."""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'

    def self_name(self) -> str:
        """Возвращает имя персонажа."""
        return self.name


class Warrior(Character):
    """Класс Воин."""
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. Сильный, выносливый '
                             'и отважный')


class Mage(Character):
    """Класс Маг."""
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. Обладает высоким '
                             'интеллектом')


class Healer(Character):
    """Класс Лекарь."""
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = ('могущественный заклинатель. Черпает силы из '
                             'природы, веры и духов')


def start_training(character: Character) -> str:
    """Принимает на вход класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа."""
    comand = {'attack': character.attack,
              'defence': character.defence,
              'special': character.special, }
    if type(character) is Warrior:
        brief = ('ты Воитель — великий мастер ближнего боя.')
    if type(character) is Mage:
        brief = ('ты Маг — превосходный укротитель стихий.')
    if type(character) is Healer:
        brief = ('ты Лекарь — чародей, способный исцелять раны.')
    print(f'{character.self_name()}, {brief}')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in comand:
            print(comand[cmd]())
    return 'Тренировка окончена.'


def choice_char_class(char_name = None) -> Character:
    """Цикл создания персонажа. Вызов функции тренировки персонажа."""
    game_classes: dict[str, type[Character]] = {'warrior': Warrior,
                                                'mage': Mage,
                                                'healer': Healer, }
    approve_choice = None
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        if selected_class in game_classes:
            approve_choice: str = input('Нажми (Y), чтобы подтвердить выбор, или '
                                   'любую другую кнопку, чтобы выбрать '
                                   'другого персонажа ').lower()
    while char_name is None:
        char_name: str = input('Введи имя персонажа: ')
    char_class: Character = game_classes[selected_class](char_name)
    return start_training(char_class)


choice_char_class()
