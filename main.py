#!/usr/bin/env python3
import pygame as pg
import colors
from Snake import Snake
pg.font.init()

WIDTH, HEIGHT = 1200, 800
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Snake Race')

FINISH_LINE = pg.Rect(1100, 5, 10, HEIGHT - 10)

FPS = 60

WINNER_FONT = pg.font.SysFont('comicsans', 100)


def draw_window(snakes):
    WIN.fill(colors.WHITE)
    pg.draw.rect(WIN, colors.BLAC, FINISH_LINE)
    for snake in snakes:
        snake.draw(WIN)

    pg.display.update()


def check_winner(snakes):
    for snake in snakes:
        if snake.x >= FINISH_LINE.x:
            return snake.name
    return ''


def create_snakes():
    snakes = []
    start_x = 10
    snakes.append(Snake('red', colors.RED, start_x, 10))
    snakes.append(Snake('blue', colors.BLUE, start_x, 60))
    snakes.append(Snake('green', colors.GREEN, start_x, 110))
    return snakes


def draw_winner(winner_name):
    winner_text = WINNER_FONT.render(f'{winner_name} won!!!', 1, colors.BLAC)
    WIN.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2, HEIGHT//2 - winner_text.get_height()//2))
    pg.display.update()
    pg.time.delay(5000)

def main():
    running = True
    clock = pg.time.Clock()

    Snake.max_speed = 100

    snakes = create_snakes()

    winner = ''

    while running:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        for snake in snakes:
            snake.move()
        winner = check_winner(snakes)
        if winner != '':
            draw_winner(winner)
            running = False

        draw_window(snakes)



if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
