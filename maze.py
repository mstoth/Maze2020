import unittest
import turtle

class MazeTests(unittest.TestCase):
    def setUp(self):
        self.m=Maze()
    def testScreen(self):
        self.assertTrue(type(self.m.s)==turtle._Screen,"No Screen!")
    def testTurtle(self):
        self.assertTrue(type(self.m.turtle)==turtle.Turtle)
    def testBackground(self):
        self.assertTrue(self.m.s.bgcolor()=='blue')

class Maze():
    """ This class creates a random maze """
    def __init__(self):
        self.s=turtle.getscreen()
        self.turtle = turtle.Turtle()
        self.s.bgcolor('blue')
        
if __name__ == "__main__":
    unittest.main()
