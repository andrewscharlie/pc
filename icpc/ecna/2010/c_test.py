import c
import unittest

class TestC(unittest.TestCase):
    def test_solve(self):
        faces = [["XXXXXXX",
                  "X     X",
                  "X XXX X",
                  "X     X",
                  "X XXX X",
                  "X XXX X",
                  "XXXXXXX"],
                 ["XXXXXXX",
                  "X     X",
                  "X X X X",
                  "X X X X",
                  "X X X X",
                  "X X X X",
                  "XXXXXXX"],
                 ["XXXXXXX",
                  "X     X",
                  "X     X",
                  "X     X",
                  "X     X",
                  "X     X",
                  "XXXXXXX"],
                 ["XXXXXXX",
                  "X     X",
                  "X X X X",
                  "X     X",
                  "X X X X",
                  "X     X",
                  "XXXXXXX"],
                 ["XXXXXXX",
                  "X XXX X",
                  "X XXX X",
                  "X XXX X",
                  "X XXX X",
                  "X     X",
                  "XXXXXXX"],
                 ["XXXXXXX",
                  "X     X",
                  "X XXX X",
                  "X X X X",
                  "X XXX X",
                  "X     X",
                  "XXXXXXX"]]
        self.assertEqual("UULLLLUUBBBB", c.solve(faces))

if __name__ == '__main__':
    unittest.main()
