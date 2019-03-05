"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import curses
from snake.game import Game


def play_game(stdsrc):
    snake_game = Game(stdsrc)

    snake_game.play()


if __name__ == '__main__':
    # Start game.
    curses.wrapper(play_game)
