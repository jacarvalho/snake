"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""

import curses
import configparser
import argparse
from game import Game


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument("--config_file", required=True, help="configuration file .ini")
    args = vars(argparser.parse_args())

    # Load configurations.
    config = configparser.ConfigParser()
    config.read(args['config_file'])

    # Start game.
    curses.wrapper(Game,
                   int(config['DEFAULT']['WINDOW_HEIGHT']),
                   int(config['DEFAULT']['WINDOW_WIDTH']))
