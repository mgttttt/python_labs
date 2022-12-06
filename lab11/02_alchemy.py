# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

class Water():
    def __str__(self):
        return 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None

class Air():
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Storm():
    def __str__(self):
        return 'Шторм'
    def __add__(self, other):
        return None


class Fire():
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

class Earth():
    def __str__(self):
        return 'Земля'
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Mud()
        else:
            return None

class Steam():
    def __str__(self):
        return 'Пар'

class Mud():
    def __str__(self):
        return 'Грязь'
    def __add__(self, other):
        return None

class Lightning():
    def __str__(self):
        return 'Молния'
    def __add__(self, other):
        return None

class Dust():
    def __str__(self):
        return 'Пыль'
    def __add__(self, other):
        return None

class Lava():
    def __str__(self):
        return 'Лава'
    def __add__(self, other):
        return None

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#

print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Air(), '+', Fire(), '=', Fire() + Air())

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
