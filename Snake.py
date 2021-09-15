import random

import pygame as pg
import colors


class Snake:
    WIDTH = 30
    HEIGHT = 10
    min_speed = 5
    max_speed = 20

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y

    def draw(self, win):
        rect = (self.x, self.y, self.WIDTH, self.HEIGHT)
        pg.draw.rect(win, self.color, rect)

    def move(self):
        self.x += random.randint(self.min_speed, self.max_speed) / 10
