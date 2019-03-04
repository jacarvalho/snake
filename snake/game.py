"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import curses
import time
from .components import Snake, Food


class Game:

    def __init__(self, stdscr, board_height=20, board_width=40, initial_speed=2, speed_increase=0.5):
        """
        Game class implements the logic and manages the gameplay.

        :param stdscr:
        :param board_height:
        :param board_width:
        :param initial_speed:
        :param speed_increase:
        """
        self.stdscr = stdscr
        self.board_height = max(10, board_height)
        self.board_width = max(10, board_width)
        self.speed = initial_speed
        self.speed_increase = speed_increase
        self.score = 0

        self.direction_map = {curses.KEY_UP: 'UP', curses.KEY_DOWN: 'DOWN',
                              curses.KEY_RIGHT: 'RIGHT', curses.KEY_LEFT: 'LEFT'}

        # Setup board, snake and food.
        self.setup_game()
        self.snake = Snake(y=self.board_height//2, x=self.board_width//2, initial_size=3)
        self.food = Food(max_y=self.board_height, max_x=self.board_width)

    def setup_game(self):
        """
        Sets options for the game board.
        """
        # Hide cursor.
        curses.curs_set(0)
        # Resize screen.
        self.stdscr.resize(self.board_height, self.board_width)
        # Clear the screen.
        self.stdscr.clear()
        # Do not wait for a key press.
        self.stdscr.nodelay(True)

    def exit_game(self, exit_code):
        """
        Exits the game. Clears the board and prints a message.

        :param exit_code: 'LOST', 'WIN', 'END'.
        :type exit_code: str
        """
        exit_msg = ""
        if exit_code == 'LOST':
            exit_msg = "You LOST!\nScore: {}".format(self.score)
        elif exit_code == 'WIN':
            exit_msg = "Congrats! You WON!\nScore: {}".format(self.score)
        elif exit_code == 'END':
            exit_msg = "You ended the game!\nScore: {}".format(self.score)

        self.stdscr.clear()
        self.draw_board()
        self.stdscr.nodelay(False)

        exit_msg += '\n\nPress any key to quit the game.'
        offset = 3
        for i, msg in enumerate(exit_msg.split('\n')):
            self.stdscr.addstr(self.board_height // 2 + i, offset, msg)
        self.stdscr.getch()
        exit(0)

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

    def check_snake_collision(self):
        """
        Check if the head of the snake hits its body.

        :return: True if collision, False otherwise.
        """
        if self.snake.size == 1:
            return False
        h_y, h_x = self.snake.get_head_position()
        for i in range(1, self.snake.size):
            b_y, b_x = self.snake.get_body_position(i)
            if h_y == b_y and h_x == b_x:
                return True
        return False

    def place_food(self):
        """
        Place the food in a random position, where it doesn't hit the snake.
        """
        collision = True
        while collision:
            collision = False
            self.food.random_position()
            f_y, f_x = self.food.get_position()
            for snake_body in self.snake.get_body():
                s_y = snake_body.y
                s_x = snake_body.x
                if s_y == f_y and s_x == f_x:
                    collision = True
                    break

    def draw_board(self):
        """
        Renders the board on screen.
        """
        self.stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')

    def draw_snake(self):
        # Draw head.
        h_y, h_x = self.snake.get_head_position()
        self.stdscr.addch(h_y, h_x, self.snake.head_symbol)
        # Draw body.
        if self.snake.size > 1:
            snake_symbol = self.snake.body_symbol
            for i in range(1, self.snake.size):
                s_y, s_x = self.snake.get_body_position(i)
                self.stdscr.addch(s_y, s_x, snake_symbol)

    def draw_food(self):
        f_y, f_x = self.food.get_position()
        self.stdscr.addch(f_y, f_x, 'X')

    def render(self):
        """
        Renders the board, snake and food.
        """
        # Render board.
        self.draw_board()

        # Display the score.
        self.stdscr.addstr(0, self.board_width // 2 - 5, "Score: {}".format(self.score))

        # Render Snake.
        self.draw_snake()

        # Render Food.
        self.draw_food()

        # Update the screen.
        self.stdscr.refresh()

    def check_collisions(self):
        """
        Checks for food, snake and board collisions.
        """
        # Check for food collisions.
        if self.check_food_colision():
            self.place_food()
            # Increase the score, snake body and game speed.
            self.score += 1
            self.snake.increase_body()
            self.speed += self.speed_increase

        # Check for body and board collisions.
        if self.check_snake_collision() or self.check_board_collision():
            self.exit_game('LOST')

    def play(self):
        """
        Implements the game logic.
        """
        while True:
            # Render objects on screen.
            self.render()

            # Read key press.
            c = self.stdscr.getch()
            self.stdscr.clear()

            if c == ord('q'):
                self.exit_game('END')
            elif c in self.direction_map:
                self.snake.change_direction(self.direction_map[c])

            self.snake.move()

            # Check for food, snake or board collisions.
            self.check_collisions()

            time.sleep(1 / self.speed)
