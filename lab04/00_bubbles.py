#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import simple_draw as sd

sd.resolution = (1200, 600)

def bubbles(point, radius, step, color):
    for _ in range(3):
        sd.circle(point, radius=radius, color=color, width=1)
        radius += step

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
bubbles(sd.get_point(300, 300), 50, 5, sd.COLOR_GREEN)
time.sleep(1)
sd.clear_screen()
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for i in range(10):
    bubbles(sd.get_point(150 + i * 100, 300), 30, 5, sd.COLOR_GREEN)
time.sleep(1)
sd.clear_screen()
# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

for i in range(10):
    bubbles(sd.get_point(150 + i * 100, 300), 30, 5, sd.COLOR_GREEN)
    bubbles(sd.get_point(150 + i * 100, 200), 30, 5, sd.COLOR_GREEN)
    bubbles(sd.get_point(150 + i * 100, 400), 30, 5, sd.COLOR_GREEN)
time.sleep(1)
sd.clear_screen()

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for _ in range(100):
    bubbles(sd.random_point(), 30, 5, sd.random_color())
    time.sleep(0.1)

sd.pause()
