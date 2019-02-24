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
        self.symbol = 'o'
        self.body = [{'y': max_y // 2, 'x': max_x // 2, 'direction': 'LEFT'}]
        self.length = 1
        self.turning_points = []

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
        tail = self.body[-1]
        y = tail['y']
        x = tail['x']
        direction = tail['direction']
        if direction == 'UP':
            self.body.append({'y': y+1, 'x': x, 'direction': direction})
        elif direction == 'DOWN':
            self.body.append({'y': y-1, 'x': x, 'direction': direction})
        elif direction == 'LEFT':
            self.body.append({'y': y, 'x': x+1, 'direction': direction})
        elif direction == 'RIGHT':
            self.body.append({'y': y, 'x': x-1, 'direction': direction})
        self.length += 1

    def move_body(self):
        """
        Move the snake body.
        """
        for i, snake_p in enumerate(self.body):
            s_y = snake_p['y']
            s_x = snake_p['x']

            # At a turning point, change the direction.
            for turn_point in self.turning_points:
                t_y = turn_point['y']
                t_x = turn_point['x']
                t_d = turn_point['direction']
                if s_y == t_y and s_x == t_x:
                    snake_p['direction'] = t_d
                    if i == self.length - 1:
                        # When the tail reaches a turning point, delete the first turning point.
                        del self.turning_points[0]

            d = snake_p['direction']
            y, x = 0, 0
            if d == 'UP':
                y -= 1
            elif d == 'DOWN':
                y += 1
            elif d == 'LEFT':
                x -= 1
            elif d == 'RIGHT':
                x += 1
            snake_p['y'] += y
            snake_p['x'] += x

    def move(self, ch=None):
        """
        Move the snake head.

        :param ch: direction of movement
        """
        if ch:
            # Set a turning point if directions do not match.
            if ch != self.body[0]['direction']:
                if self.length != 1:
                    y = self.body[0]['y']
                    x = self.body[0]['x']
                    self.turning_points.append({'y': y, 'x': x, 'direction': ch})
            self.body[0]['direction'] = ch
        self.move_body()

    def check_collision(self):
        """
        Check if the head of the snake hits its body.

        :return: True if collision, False otherwise.
        """
        if self.length == 1:
            return False
        h_y, h_x = self.body[0]['y'], self.body[0]['x']
        for snake_p in self.body[1:-1]:
            b_y = snake_p['y']
            b_x = snake_p['x']
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
