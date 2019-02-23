"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import curses
import time
from core import Snake, Food


class Game:

    def __init__(self, stdscr, win_height, win_width):
        self.stdscr = stdscr
        self.win_height = max(10, win_height)
        self.win_width = max(10, win_width)

        # Resize screen.
        self.stdscr.resize(self.win_height, self.win_width)

        # Instantiate components.
        self.snake = Snake(self.win_height, self.win_width)
        self.food = Food(self.win_height, self.win_width)

        # Start playing.
        self.play()

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

            # Check if a key was pressed.
            c = self.stdscr.getch()
            self.stdscr.clear()

            if c == curses.KEY_UP:
                self.snake.move('UP')
            elif c == curses.KEY_DOWN:
                self.snake.move('DOWN')
            elif c == curses.KEY_LEFT:
                self.snake.move('LEFT')
            elif c == curses.KEY_RIGHT:
                self.snake.move('RIGHT')
            elif c == ord('q'):
                exit(0)

            time.sleep(0.2)
            self.snake.move(self.snake.last_key)


    def render(self):
        """
        Renders the board, snake and food.
        """
        # Draw a game border.
        self.stdscr.border()

        # Render Snake.
        s_y, s_x = self.snake.get_position()
        self.stdscr.addch(s_y, s_x, 'S')

        # Render Food.
        f_y, f_x = self.food.get_position()
        self.stdscr.addch(f_y, f_x, 'F')

        # Update the screen.
        self.stdscr.refresh()
