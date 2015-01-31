import c
import unittest

class TestC(unittest.TestCase):
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

    def test_solve(self):
        self.assertEqual("UULLLLUUBBBB", c.solve(self.faces))

    def test_is_passable(self):
        """Replay each node in test_solve to make sure that the nodes are passable."""
        self.assertTrue(c.is_passable((1, 1, 1), self.faces))
        self.assertTrue(c.is_passable((1, 1, 2), self.faces)) # U
        self.assertTrue(c.is_passable((1, 1, 3), self.faces)) # U
        self.assertTrue(c.is_passable((1, 2, 3), self.faces)) # L
        self.assertTrue(c.is_passable((1, 3, 3), self.faces)) # L
        self.assertTrue(c.is_passable((1, 4, 3), self.faces)) # L
        self.assertTrue(c.is_passable((1, 5, 3), self.faces)) # L
        self.assertTrue(c.is_passable((1, 5, 4), self.faces)) # U
        self.assertTrue(c.is_passable((1, 5, 5), self.faces)) # U
        self.assertTrue(c.is_passable((1, 5, 5), self.faces)) # B
        self.assertTrue(c.is_passable((2, 5, 5), self.faces)) # B
        self.assertTrue(c.is_passable((3, 5, 5), self.faces)) # B
        self.assertTrue(c.is_passable((4, 5, 5), self.faces)) # B
        self.assertTrue(c.is_passable((5, 5, 5), self.faces)) # B
        
if __name__ == '__main__':
    unittest.main()
