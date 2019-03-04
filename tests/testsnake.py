"""
Copyright 2019
Author: Joao Carvalho <joao.ac.carvalho@gmail.com>
"""
import unittest
import curses
from snake.components import Snake, Point
from snake.game import Game


class TestSnake(unittest.TestCase):

    def test_setup_snake(self):
        snake = Snake(5, 5, initial_size=3)
        body = [Point(5, 5), Point(5, 4), Point(5, 3)]
        self.assertEqual(snake.get_body(), body)

    def test_body_position(self):
        snake = Snake(5, 5, initial_size=3)
        self.assertEqual(snake.get_body_position(1), Point(5, 4))

    def test_increase_body(self):
        # Moving RIGHT.
        snake = Snake(5, 5, initial_size=3)
        snake.increase_body()
        body = [Point(5, 5), Point(5, 4), Point(5, 3), Point(5, 2)]
        self.assertEqual(snake.get_body(), body)

        # Moving LEFT.
        snake = Snake(5, 5, initial_size=3)
        snake.body = [Point(5, 5), Point(5, 6), Point(5, 7)]
        snake.increase_body()
        body = [Point(5, 5), Point(5, 6), Point(5, 7), Point(5, 8)]
        self.assertEqual(snake.get_body(), body)

        # Moving UP.
        snake = Snake(5, 5, initial_size=3)
        snake.body = [Point(5, 5), Point(6, 5), Point(7, 5)]
        snake.increase_body()
        body = [Point(5, 5), Point(6, 5), Point(7, 5), Point(8, 5)]
        self.assertEqual(snake.get_body(), body)

        # Moving DOWN.
        snake = Snake(5, 5, initial_size=3)
        snake.body = [Point(5, 5), Point(4, 5), Point(3, 5)]
        snake.increase_body()
        body = [Point(5, 5), Point(4, 5), Point(3, 5), Point(2, 5)]
        self.assertEqual(snake.get_body(), body)

        # Moving LEFT and twisted.
        snake = Snake(5, 5, initial_size=3)
        snake.body = [Point(5, 5), Point(5, 6), Point(4, 6)]
        snake.increase_body()
        body = [Point(5, 5), Point(5, 6), Point(4, 6), Point(3, 6)]
        self.assertEqual(snake.get_body(), body)

        # Moving DOWN and twisted.
        snake = Snake(5, 5, initial_size=3)
        snake.body = [Point(5, 5), Point(4, 5), Point(4, 6)]
        snake.increase_body()
        body = [Point(5, 5), Point(4, 5), Point(4, 6), Point(4, 7)]
        self.assertEqual(snake.get_body(), body)

    def test_change_direction(self):
        snake = Snake(5, 5, initial_size=3)
        snake.change_direction('UP')
        self.assertEqual(snake.head_direction, 'UP')

    def test_move(self):
        # Moving RIGHT.
        snake = Snake(5, 5, initial_size=3)
        snake.head_direction = 'RIGHT'
        snake.move()
        body = [Point(5, 6), Point(5, 5), Point(5, 4)]
        self.assertEqual(snake.get_body(), body)

        # Moving UP.
        snake = Snake(5, 5, initial_size=3)
        snake.head_direction = 'UP'
        snake.move()
        body = [Point(4, 5), Point(5, 5), Point(5, 4)]
        self.assertEqual(snake.get_body(), body)

        # Moving DOWN.
        snake = Snake(5, 5, initial_size=3)
        snake.head_direction = 'DOWN'
        snake.move()
        body = [Point(6, 5), Point(5, 5), Point(5, 4)]
        self.assertEqual(snake.get_body(), body)


class TestGame(unittest.TestCase):

    def test_board_collision(self):
        # Right border.
        game = curses.wrapper(Game, board_height=20, board_width=20)
        game.snake.body = [Point(10, 19), Point(10, 18)]
        self.assertTrue(game.check_board_collision())

        # Upper border.
        game = curses.wrapper(Game, board_height=20, board_width=20)
        game.snake.body = [Point(0, 5), Point(1, 5), Point(2, 5)]
        self.assertTrue(game.check_board_collision())

        # No collision.
        game = curses.wrapper(Game, board_height=20, board_width=20)
        game.snake.body = [Point(1, 5), Point(2, 5), Point(3, 5)]
        self.assertFalse(game.check_board_collision())

    def test_food_collision(self):
        # Collision.
        game = curses.wrapper(Game, board_height=20, board_width=20)
        game.snake.body = [Point(1, 5), Point(2, 5), Point(3, 5)]
        game.food.position = Point(1, 5)
        self.assertTrue(game.check_food_colision())

        # No collision.
        game = curses.wrapper(Game, board_height=20, board_width=20)
        game.snake.body = [Point(1, 5), Point(2, 5), Point(3, 5)]
        game.food.position = Point(10, 10)
        self.assertFalse(game.check_food_colision())


if __name__ == '__main__':
    unittest.main()
