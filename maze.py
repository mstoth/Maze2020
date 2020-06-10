import unittest
import turtle

class MazeTests(unittest.TestCase):
    def testItExists(self):
        m=Maze() # this should fail
    def testScreen(self):
        m=Maze()
        self.assertTrue(type(m.s)==turtle._Screen,"No Screen!")
    def testTurtle(self):
        m=Maze()
        self.assertTrue(type(m.turtle)==turtle.Turtle)

class Maze():
    """ This class creates a random maze """
    def __init__(self):
        self.s=turtle.getscreen()
        self.turtle = turtle.Turtle()

if __name__ == "__main__":
    unittest.main()
