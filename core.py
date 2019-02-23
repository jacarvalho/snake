"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
from random import randint


class Snake:

    def __init__(self, max_y, max_x):
        """
        Snake object.
        The positions x and y are the inverse of what is usually used in a matrix notation, considering a matrix x is
        a column index and y is a row index.

        :param max_y: maximum value for y
        :type max_y: int
        :param max_x: maximum value for x
        :type max_x: int
        """
        self.y = max_y // 2
        self.x = max_x // 2
        self.last_key = 'RIGHT'

    def get_position(self):
        """
        Getter for the current position of the snake.

        :return: tuple with y and x positions
        """
        return self.y, self.x

    def move(self, ch):
        if ch == 'UP':
            self.y -= 1
        if ch == 'DOWN':
            self.y += 1
        if ch == 'LEFT':
            self.x -= 1
        if ch == 'RIGHT':
            self.x += 1
        self.last_key = ch


class Food:

    def __init__(self, max_y, max_x):
        """
        Food class.

        :param max_y: maximum value for y
        :type max_y: int
        :param max_x: maximum value for x
        :type max_x: int
        """
        self.max_y = max_y
        self.max_x = max_x
        self.random_position()

    def get_position(self):
        """
        Getter for the current position of the food.

        :return: tuple with y and x positions
        """
        return self.y, self.x

    def random_position(self):
        """
        Generate a random position for the food.
        """
        self.y = randint(1, self.max_y - 2)
        self.x = randint(1, self.max_x - 2)
