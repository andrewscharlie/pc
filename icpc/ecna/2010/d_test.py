import d
import unittest

from math import radians

class TestD(unittest.TestCase):
    def test_no_subjects(self):
        camera = [0, 0]
        subjects = []
        f = radians(45)

        self.assertEqual(0, d.solve(camera, subjects, f))
        
    def test_one_subject(self):
        camera = [0, 0]
        subjects = [[1, 1]]
        f = radians(45)

        self.assertEqual(1, d.solve(camera, subjects, f))

    def test_one_subject_camera_not_at_origin(self):
        camera = [1, 1]
        subjects = [[2, 2]]
        f = radians(45)

        self.assertEqual(1, d.solve(camera, subjects, f))
        
    def test_two_subjects_two_shots(self):
        camera = [0, 0]
        subjects = [[1, 0], [0, 1]]
        f = radians(45)

        self.assertEqual(2, d.solve(camera, subjects, f))

    def test_two_subjects_one_shot(self):
        camera = [0, 0]
        subjects = [[1, 0], [0, 1]]
        f = radians(91)

        self.assertEqual(1, d.solve(camera, subjects, f))

    def test_three_subjects_one_shot(self):
        camera = [0, 0]
        subjects = [[1, 0], [0, 1], [1, 1]]
        f = radians(91)

        self.assertEqual(1, d.solve(camera, subjects, f))

    def test_three_subjects_two_shots(self):
        camera = [0, 0]
        subjects = [[1, 0], [0, 1], [-1, 1]]
        f = radians(91)

        self.assertEqual(2, d.solve(camera, subjects, f))

    def test_three_subjects_three_shots(self):
        camera = [0, 0]
        subjects = [[1, 1], [-1, 1], [-1, -1]]
        f = radians(89)
        
        self.assertEqual(3, d.solve(camera, subjects, f))

if __name__ == '__main__':
    unittest.main()
