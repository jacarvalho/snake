"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""

import curses
import configparser
import argparse
from snake.game import Game


def play_game(stdsrc, configs):
    if configs:
        snake_game = Game(stdsrc, board_height=int(configs['DEFAULT']['WINDOW_HEIGHT']),
                          board_width=int(configs['DEFAULT']['WINDOW_WIDTH']))
    else:
        snake_game = Game(stdsrc)

    snake_game.play()


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument("--config_file", required=False, help="configuration file .ini")
    args = vars(argparser.parse_args())

    # Load configurations.
    config = configparser.ConfigParser()
    if args['config_file']:
        config.read(args['config_file'])

    # Start game.
    curses.wrapper(play_game, config)
