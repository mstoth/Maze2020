import unittest
import turtle

class MazeTests(unittest.TestCase):
    def testItExists(self):
        m=Maze() # this should fail
    def testScreen(self):
        m=Maze()
        self.assertTrue(type(m.screen)==turtle._Screen,"No Screen!")
        

class Maze():
    """ This class creates a random maze """
    def __init__(self):
        self.screen=turtle._Screen()

      
if __name__=="__main__":
    unittest.main()

