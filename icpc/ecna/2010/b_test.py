import b
import unittest

class TestB(unittest.TestCase):
    def test_solve_no_flips(self):
        grid = [[1]]
        flips = []

        expected = [1]
        self.assertEqual(expected, b.solve(grid, flips))

    def test_solve_left_flip(self):
        grid = [[1, 2]]
        flips = ["L"]

        expected = [2, -1]
        self.assertEqual(expected, b.solve(grid, flips))

    def test_solve_right_flip(self):
        grid = [[1, 2]]
        flips = ["R"]

        expected = [1, -2]
        self.assertEqual(expected, b.solve(grid, flips))

    def test_solve_top_flip(self):
        grid = [[1], [2]]
        flips = ["T"]

        expected = [2, -1]
        self.assertEqual(expected, b.solve(grid, flips))

    def test_solve_bottom_flip(self):
        grid = [[1], [2]]
        flips = ["B"]

        expected = [1, -2]
        self.assertEqual(expected, b.solve(grid, flips))

    def test_solve_all_flips(self):
        grid = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
        flips = list("LRTB")

        expected = [5, -4, -6, 3, 1, -2, 9, 7, -8]
        self.assertEqual(expected, b.solve(grid, flips))

if __name__ == '__main__':
    unittest.main()
