import e
import unittest

class TestE(unittest.TestCase):
    def test_get_neighbors_not_edge(self):
        expected = [[0, 0], [0, 1], [0, 2],
                    [1, 0], [1, 2],
                    [2, 0], [2, 1], [2, 2]]
        

        self.assertItemsEqual(expected, e.get_neighbors(3, 10, 1, 1))

    def test_get_neighbors_inner_ring(self):
        expected = [[0, 3], [0, 4], [0, 5],
                    [0, 8], [0, 0],
                    [1, 8], [1, 9], [1, 0]]

        self.assertItemsEqual(expected, e.get_neighbors(3, 10, 0, 9))

    def test_get_neighbors_outer_ring(self):
        expected = [[2, 3], [2, 4], [2, 5],
                    [2, 8], [2, 0],
                    [1, 8], [1, 9], [1, 0]]

        self.assertItemsEqual(expected, e.get_neighbors(3, 10, 2, 9))

    def test_count_live_cells(self):
        grid = [[True, False, False, True],
                [True, True, False, False],
                [True, False, False, False]]

        cells = [[2, 0], [1, 1], [0, 2]]
        expected = [[2, 0], [1, 1]]
        
        self.assertEqual(expected, e.get_live_cells(grid, cells))

    def test_solve(self):
        grid = [[True, True, False, False, False, False, False, True],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False]]
        generations = 1

        expected = [[0, 0], [0, 4], [1, 0]]
        self.assertEqual(expected, e.solve(grid, generations))
        
if __name__ == '__main__':
    unittest.main()
