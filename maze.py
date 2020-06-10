import unittest
import turtle
SIZE=400
class MazeTests(unittest.TestCase):
    def setUp(self):
        self.m=Maze()
    def testScreen(self):
        self.assertTrue(type(self.m.s)==turtle._Screen,"No Screen!")
    def testTurtle(self):
        self.assertTrue(type(self.m.turtle)==turtle.Turtle)
    def testBackground(self):
        self.assertTrue(self.m.s.bgcolor()=='blue')
    def testSize(self):
        self.assertTrue(self.m.s.window_width()==SIZE)
        self.assertTrue(self.m.s.window_height()==SIZE)

class Maze():
    """ This class creates a random maze """
    def __init__(self):
        self.s=turtle.getscreen()
        self.turtle = turtle.Turtle()
        self.s.bgcolor('blue')
        self.s.setup(SIZE,SIZE)
        
if __name__ == "__main__":
    unittest.main()
