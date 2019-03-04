"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import curses
import configparser
from snake.game import Game


def play_game(stdsrc, configs):
    snake_game = Game(stdsrc, board_height=int(configs['DEFAULT']['WINDOW_HEIGHT']),
                      board_width=int(configs['DEFAULT']['WINDOW_WIDTH']),
                      initial_speed=int(configs['DEFAULT']['INITIAL_SPEED']))

    snake_game.play()


if __name__ == '__main__':
    # Load configurations.
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Start game.
    curses.wrapper(play_game, config)
