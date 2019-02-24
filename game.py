"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import curses
import time
from components import Snake, Food


class Game:

    def __init__(self, stdscr, board_height=20, board_width=20, initial_speed=5):
        self.stdscr = stdscr
        self.board_height = max(10, board_height)
        self.board_width = max(10, board_width)
        self.speed = initial_speed
        self.score = 0

        self.direction_map = {-1: -1, curses.KEY_UP: 'UP', curses.KEY_DOWN: 'DOWN',
                              curses.KEY_RIGHT: 'RIGHT', curses.KEY_LEFT: 'LEFT'}

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

    def exit_game(self, msg):
        """
        Exits the game. Clears the board and prints a message.

        :param msg: message to print.
        """
        self.stdscr.clear()
        self.stdscr.nodelay(False)
        msg = msg + '\nPress any key to quit the game.'
        i = 0
        for line in msg.split('\n'):
            self.stdscr.addstr(self.board_height // 2 + i, 1, line + '\n')
            i += 1
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
        f_y, f_x = self.food.get_current_position()
        return True if (s_y == f_y and s_x == f_x) else False

    def place_food(self):
        """
        Place the food in a random position, where it doesn't hit the snake.
        """
        collision = True
        while collision:
            collision = False
            self.food.generate_random_position()
            f_y, f_x = self.food.get_current_position()
            for snake_body in self.snake.get_body():
                s_y = snake_body['y']
                s_x = snake_body['x']
                if s_y == f_y and s_x == f_x:
                    collision = True
                    break

    def render(self):
        """
        Renders the board, snake and food.
        """
        # Draw the game board.
        self.stdscr.box('#', '#')

        # Display the score.
        self.stdscr.addstr(0, self.board_width // 2 - 5, "Score: {}".format(self.score))

        # Render Snake.
        snake_head_symbol = self.snake.head_symbol
        snake_body_symbol = self.snake.body_symbol
        for i, snake_body in enumerate(self.snake.get_body()):
            s_y = snake_body['y']
            s_x = snake_body['x']
            snake_symbol = snake_body_symbol
            if i == 0:
                snake_symbol = snake_head_symbol
            self.stdscr.addch(s_y, s_x, snake_symbol)

        # Render Food.
        f_y, f_x = self.food.get_current_position()
        self.stdscr.addch(f_y, f_x, 'F')

        # Update the screen.
        self.stdscr.refresh()

    def check_collisions(self):
        """
        Checks for food, snake and board collisions.
        """
        # Check for food collisions.
        if self.check_food_colision():
            # Increase the score.
            self.score += 1
            # Increase the snake body.
            self.snake.increase_body()
            # Place the food in a random position.
            self.place_food()
            # Increase game speed.
            self.speed *= 1.05

        # Check for body and board collisions.
        if self.snake.check_collision() or self.check_board_collision():
            # Exit the game if the snake hits itself or board walls.
            self.exit_game("You lost!\nScore: {}".format(self.score))

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
            c = self.stdscr.getch()
            self.stdscr.clear()

            if c == ord('q'):
                exit(0)

            self.snake.move(self.direction_map[c])

            # Check for food, snake or board collisions.
            self.check_collisions()

            time.sleep(1 / self.speed)

