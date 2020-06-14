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
        self.assertTrue(self.m.s.window_width==SIZE)
        self.assertTrue(self.m.s.window_height==SIZE)
    def testMatrixSize(self):
        self.assertTrue(len(self.m.matrix)==SIZE/20)
    def testReset(self):
        self.m.reset()
        self.assertTrue(0==self.m.matrix[0][0])
        self.assertTrue(self.m.turtle.pos()==(-(SIZE/2-10),SIZE/2-10))
    def testGetMatrixValue(self):
        self.assertTrue(self.m.getMatrixValueAt(self.m.turtle.position())==0)
    def testSetMatrixValue(self):
        self.assertTrue(self.m.turtle.position(),0)

class Maze():
    """ This class creates a random maze """
    def __init__(self):
        self.reset()

    def reset(self):
        self.s=turtle.getscreen()
        self.s.window_width=SIZE
        self.s.window_height=SIZE
        self.s.screensize(SIZE,SIZE)
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(-(SIZE/2-10),SIZE/2-10)
        self.matrix=[[1 for i in range(int(SIZE/20))] for i in range(int(SIZE/20))]
        self.s.bgcolor('blue')
        self.turtle.shape('square')
        self.turtle.color('white')
        self.turtle.stamp()
        self.matrix[0][0]=0

    def getMatrixValueAt(self,pos):
        x=int((pos[0]+200)/20)
        y=20-int((pos[1]+200)/20)-1
        v=self.matrix[x][y]
        return v

    def setMatrixValueAt(self,pos,value):
        x=int((pos[0]+200)/20)
        y=20-int((pos[1]+200)/20)-1
        try:
            self.matrix[y][x]=value
        except:
            return False
        if value==0:
            self.turtle.color('white')
            self.turtle.stamp()
        if value==1:
            self.turtle.color('blue')
            self.turtle.stamp()
        return True
    
if __name__ == "__main__":
    unittest.main()
