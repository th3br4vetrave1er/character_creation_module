from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


# Создание родительского класса.
class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (
            f'{self.name} нанёс противнику урон, '
            f'равный {value_attack}.'
        )

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (
            f'{self.name} блокировал {value_defence} ед. урона.'
        )

    def special(self):
        return (
            f'{self.name} применил специальное умение '
            f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"'
        )

    def __str__(self):
        return (
            f'{self.__class__.__name__} {self.BRIEF_DESC_CHAR_CLASS}.'
        )


# Дочерние классы.
class Warrior(Character):
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = (
        ' дерзкий воин ближнего боя. '
        'Сильный, выносливый и отважный'
    )


class Mage(Character):
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = (
        ' находчивый воин дальнего боя. '
        'Обладает высоким интеллектом'
    )


class Healer(Character):
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = (
        ' могущественный заклинатель. '
        'Черпает силы из природы, веры и духов'
    )


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())
