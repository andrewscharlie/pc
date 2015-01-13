import a
import unittest

class TestA(unittest.TestCase):

    def test_add_triangles_no_solution(self):
        t0 = a.Triangle([(0, 0), (1, 0), (0, 1)])
        t1 = a.Triangle([(0, 0), (2, 0), (0, 2)])

        expected = []
        self.assertItemsEqual(expected, a.add_triangles(t0, t1))

    def test_add_triangles_one_solution(self):
        t0 = a.Triangle([(0, 0), (0, -1), (3, 0)])
        t1 = a.Triangle([(0, 0), (3, 0), (0, 4)])

        expected = [a.Triangle([(0, -1), (3, 0), (0, 4)])]
        self.assertItemsEqual(expected, a.add_triangles(t0, t1))

    def test_add_triangles_two_solution(self):
        t0 = a.Triangle([(0, 0), (3, 0), (0, 4)])
        t1 = a.Triangle([(4, 0), (7, 0), (7, 4)])

        expected = [a.Triangle([(0, 0), (6, 0), (3, 4)]),
                    a.Triangle([(0, 4), (0, -4), (3, 0)])]

        self.assertItemsEqual(expected, a.add_triangles(t0, t1))

    def test_add_triangles_vertices_shifted(self):
        t0 = a.Triangle([(3, 0), (0, 4), (0, 0)])
        t1 = a.Triangle([(0, 4), (3, 5), (0, 5)])

        expected = [a.Triangle([(0, 0), (3, 1), (0, 5)])]
        self.assertItemsEqual(expected, a.add_triangles(t0, t1))

    def test_get_fits_one_solution(self):
        holes = [a.Triangle([(-2, 0), (0, 0), (-1, 1)]),
                 a.Triangle([(-4, 0), (0, 0), (-2, 2)])]

        triangles = [a.Triangle([(0, 0), (1, 0), (1, 1)]),
                     a.Triangle([(1, 0), (2, 0), (1, 1)]),
                     a.Triangle([(0, 100), (2, 102), (0, 102)]),
                     a.Triangle([(0, 102), (2, 102), (0, 104)])]

        expected = [[(2, 3)], # triangles[2] + triangles[3] = holes[0]
                    [(0, 1)]] # triangles[0] + triangles[1] = holes[1]
        self.assertItemsEqual(expected, a.get_fits(holes, triangles))

    def test_get_fits_two_solutions(self):
        holes = [a.Triangle([(0, 0), (5, 0), (1, 1)])]

        triangles = [a.Triangle([(0, 0), (1, 0), (1, 1)]),
                     a.Triangle([(1, 0), (5, 0), (1, 1)]),
                     a.Triangle([(101, 100), (105, 100), (101, 101)])]

        # triangles[1] or triangles[2] can be the 2nd triangle
        expected = [[(0, 1), (0, 2)]]
        self.assertItemsEqual(expected, a.get_fits(holes, triangles))



    def test_get_solution(self):
        fits = [[(0, 1), (2, 3)],
                [(0, 1)]]

        expected = [(2, 3), (0, 1)]
        self.assertItemsEqual(expected, a.get_solution(fits))

if __name__ == '__main__':
    unittest.main()
