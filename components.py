"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
from random import randint


class Snake:

    def __init__(self, max_y, max_x):
        """
        Snake object.
        The positions x and y are the inverse of what is usually used in a
        matrix notation, considering a matrix x is a column index and y is a
        row index.

        :param max_y: maximum value for y
        :type max_y: int
        :param max_x: maximum value for x
        :type max_x: int
        """
        self.head_symbol = 'O'
        self.body_symbol = 'o'
        self.head_direction = 'RIGHT'
        self.tail_direction = self.head_direction
        self.body = [{'y': max_y // 2, 'x': max_x // 2}]
        self.length = 1
        self.initial_start()

    def initial_start(self):
        for i in range(1, 3):
            self.body.append({'y': self.body[i-1]['y'], 'x': self.body[i-1]['x']-1})
            self.length += 1

    def get_head_position(self):
        """
        Getter for the head position of the snake.

        :return: y and x head position
        """
        return self.body[0]['y'], self.body[0]['x']

    def get_body(self):
        """
        Getter for the snake body.

        :return: list with x and y positions and direction of snake body
        """
        return self.body

    def increase_body(self):
        """
        Adds an element to the snake body at its tail.
        """
        # Get tail position.
        t_y = self.body[-1]['y']
        t_x = self.body[-1]['x']

        # Update tail.
        y, x = 0, 0
        if self.tail_direction == 'UP':
            y += 1
        elif self.tail_direction == 'DOWN':
            y -= 1
        elif self.tail_direction == 'LEFT':
            x += 1
        elif self.tail_direction == 'RIGHT':
            x -= 1

        self.body.append({'y': t_y + y, 'x': t_x + x})
        self.length += 1

    def move(self, direction):
        """
        Move the snake.

        :param direction: direction of movement (-1, UP, DOWN, RIGHT, LEFT)
        """
        # Move the snake body except for the head.
        for i in range(self.length - 1, 0, -1):
            self.body[i]['y'] = self.body[i-1]['y']
            self.body[i]['x'] = self.body[i-1]['x']

        # Move the snake head.
        if direction != -1:
            self.head_direction = direction
        y, x = 0, 0
        if self.head_direction == 'UP':
            y -= 1
        elif self.head_direction == 'DOWN':
            y += 1
        elif self.head_direction == 'LEFT':
            x -= 1
        elif self.head_direction == 'RIGHT':
            x += 1
        self.body[0]['y'] += y
        self.body[0]['x'] += x

        # Update the tail direction.
        if self.length == 1:
            self.tail_direction = self.head_direction
        else:
            if self.body[-1]['y'] > self.body[-2]['y']:
                self.tail_direction = 'UP'
            elif self.body[-1]['y'] < self.body[-2]['y']:
                self.tail_direction = 'DOWN'
            elif self.body[-1]['x'] > self.body[-2]['x']:
                self.tail_direction = 'LEFT'
            elif self.body[-1]['x'] < self.body[-2]['x']:
                self.tail_direction = 'RIGHT'

    def check_collision(self):
        """
        Check if the head of the snake hits its body.

        :return: True if collision, False otherwise.
        """
        if self.length == 1:
            return False
        h_y, h_x = self.body[0]['y'], self.body[0]['x']
        for body_part in self.body[1:]:
            b_y = body_part['y']
            b_x = body_part['x']
            if h_y == b_y and h_x == b_x:
                return True
        return False


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
        self.x = None
        self.y = None
        self.generate_random_position()

    def get_current_position(self):
        """
        Getter for the current position of the food.

        :return: tuple with y and x positions
        """
        return self.y, self.x

    def generate_random_position(self):
        """
        Generate a random position for the food.
        """
        self.y = randint(1, self.max_y - 2)
        self.x = randint(1, self.max_x - 2)
