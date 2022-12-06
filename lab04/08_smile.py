#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def print_smile(x, y, color):
    position = sd.get_point(x, y)
    sd.circle(position, radius=50, color=color, width=2)
    sd.line(sd.get_point(position.x - 30, position.y - 20), sd.get_point(position.x + 30, position.y - 20), color=color, width=2)
    sd.line(sd.get_point(position.x - 15, position.y + 20), sd.get_point(position.x - 15, position.y + 20), color=color, width=5)
    sd.line(sd.get_point(position.x + 15, position.y + 20), sd.get_point(position.x + 15, position.y + 20), color=color, width=5)

for i in range(10):
    print_smile(sd.random_point().x, sd.random_point().y, sd.random_color())
# TODO здесь ваш код

sd.pause()
