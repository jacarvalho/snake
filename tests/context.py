"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from snake.components import Snake, Food, Point
from snake.game import Game
