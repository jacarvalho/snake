"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
from random import randint
from collections import namedtuple


Point = namedtuple('Point', ['y', 'x'])


class Snake:

    def __init__(self, y=0, x=0, initial_size=3):
        """
        Snake object.
        The positions x and y are the inverse of what is usually used in a
        matrix notation, considering a matrix x is a column index and y is a
        row index. The top left corner is (0, 0).

        :param y: y position of snake head
        :type y: int
        :param x: x position of snake head
        :type x: int
        :param initial_size: initial size for the snake
        :type initial_size: int
        """
        self.head_symbol = 'O'
        self.body_symbol = 'o'
        self.head_direction = 'RIGHT'
        self.body = [Point(y, x)]
        self.size = initial_size

        self.setup_snake()

    def setup_snake(self):
        """
        Setup a snake body horizontally with the head on the right side.
        """
        for i in range(0, self.size):
            self.body.append(Point(self.body[i].y, self.body[i].x - 1))

    def get_head_position(self):
        """
        Getter for the snake head position.

        :return: y and x head position
        """
        return self.body[0].y, self.body[0].x

    def get_tail_position(self):
        """
        Getter for the snake tail position.

        :return: y and x tail position
        """
        return self.body[-1].y, self.body[-1].x

    def get_body_position(self, ind):
        """
        Getter for the snake body positions at ind.

        :param ind: position index
        :type ind: int
        :return: y and x position at index ind
        """
        return self.body[ind].y, self.body[ind].x

    def get_positions(self):
        """
        Getter for the snake positions.

        :return: list with x and y positions of the snake
        """
        return self.body

    def change_direction(self, direction):
        """
        Change the snake direction.

        :param direction: direction of snake head
        :type direction: str
        """
        self.head_direction = direction

    def increase_body(self):
        """
        Adds an element to the snake body at its tail.
        """
        y, x = self.get_tail_position()
        if self.size == 1:
            if self.head_direction == 'UP':
                y += 1
            elif self.head_direction == 'DOWN':
                y -= 1
            elif self.head_direction == 'LEFT':
                x += 1
            elif self.head_direction == 'RIGHT':
                x -= 1
        else:
            # Get tail and penultimate positions to determine the direction of body increase.
            t_y, t_x = self.get_tail_position()
            t_y_p, t_x_p = self.get_body_position(-2)
            if t_y > t_y_p:
                y += 1
            elif t_y < t_y_p:
                y -= 1
            elif t_x > t_x_p:
                x += 1
            elif t_x < t_x_p:
                x -= 1

        self.body.append(Point(y, x))
        self.size += 1

    def move(self):
        """
        Move the snake.
        """
        # Delete the tail.
        if self.size > 1:
            del self.body[-1]

        # Move the snake tail to the front.
        h_y, h_x = self.get_head_position()
        y, x = 0, 0
        if self.head_direction == 'UP':
            y -= 1
        elif self.head_direction == 'DOWN':
            y += 1
        elif self.head_direction == 'LEFT':
            x -= 1
        elif self.head_direction == 'RIGHT':
            x += 1
        self.body.insert(0, Point(h_y + y, h_x + x))


class Food:

    def __init__(self, max_y=0, max_x=0):
        """
        Food class.

        :param max_y: maximum value for y
        :type max_y: int
        :param max_x: maximum value for x
        :type max_x: int
        """
        self.max_y = max_y
        self.max_x = max_x
        self.position = Point(None, None)
        self.random_position()

    def get_position(self):
        """
        Getter for the current position of the food.

        :return: y and x food position
        """
        return self.position.y, self.position.x

    def random_position(self):
        """
        Generate a random position for the food.
        """
        self.position = Point(randint(1, self.max_y - 2), randint(1, self.max_x - 2))
