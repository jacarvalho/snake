"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import curses
import time
from components import Snake, Food


class Game:

    def __init__(self, stdscr, board_height=20, board_width=20, initial_speed=10):
        self.stdscr = stdscr
        self.board_height = max(10, board_height)
        self.board_width = max(10, board_width)
        self.speed = initial_speed

        # Sets the sreen.
        self.start_screen()

        # Instantiate snake and food.
        self.snake = Snake(self.board_height, self.board_width)
        self.food = Food(self.board_height, self.board_width)

        # Start playing.
        self.play()

    def start_screen(self):
        """
        Sets options for the game screen.
        """
        # Hide cursor.
        curses.curs_set(0)
        # Resize screen.
        self.stdscr.resize(self.board_height, self.board_width)

    def check_board_collision(self):
        """
        Check if the snake hit the board wall.

        :return: True if the snake hits the board wall, False otherwise.
        """
        s_y, s_x = self.snake.get_head_position()
        if s_y == 0 or s_y == self.board_height - 1 or s_x == 0 or s_x == self.board_width - 1:
            return True
        return False

    def check_food_colision(self):
        """
        Checks if the head of the snake ate the food.

        :return: True if the head of the snake is at the same position as the food, False otherwise.
        """
        s_y, s_x = self.snake.get_head_position()
        f_y, f_x = self.food.get_position()
        return True if (s_y == f_y and s_x == f_x) else False

    def place_food(self):
        """
        Place the food in a random position, where it doesn't hit the snake.
        """
        while self.check_food_colision():
            self.food.random_position()

    def render(self):
        """
        Renders the board, snake and food.
        """
        # Draw the game board.
        self.stdscr.box('#', '#')

        # Render Snake.
        snake_symbol = self.snake.symbol
        for snake_p in self.snake.get_body():
            s_y = snake_p['y']
            s_x = snake_p['x']
            self.stdscr.addch(s_y, s_x, snake_symbol)

        # Render Food.
        f_y, f_x = self.food.get_position()
        self.stdscr.addch(f_y, f_x, 'F')

        # Update the screen.
        self.stdscr.refresh()

    def play(self):
        """
        Implements the game logic.
        """
        self.stdscr.clear()
        # Do not wait for a key press.
        self.stdscr.nodelay(True)

        while True:
            # Render objects on screen.
            self.render()

            # Move the snake.
            # Check if a key was pressed.
            c = self.stdscr.getch()
            self.stdscr.clear()
            if c == -1:
                # If no key was pressed, move it in the direction of the previous key pressed.
                self.snake.move()
            elif c == curses.KEY_UP:
                self.snake.move('UP')
            elif c == curses.KEY_DOWN:
                self.snake.move('DOWN')
            elif c == curses.KEY_LEFT:
                self.snake.move('LEFT')
            elif c == curses.KEY_RIGHT:
                self.snake.move('RIGHT')
            elif c == ord('q'):
                exit(0)

            # Check for food collisions.
            if self.check_food_colision():
                # Increase the snake body.
                self.snake.increase_body()
                # Place the food in a random position.
                self.place_food()
                # Increase game speed.
                self.speed *= 1.05
                continue

            # Check for body and board collisions.
            if self.snake.check_collision() or self.check_board_collision():
                # Exit the game if the snake hits itself or board walls.
                exit(0)

            time.sleep(1 / self.speed)

