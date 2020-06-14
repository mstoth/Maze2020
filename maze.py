import unittest
import turtle
import random
SIZE=400
EAST=0;NORTH=1;WEST=2;SOUTH=3
INVALID = -1
EMPTY = 0
WALL = 1
VISITED = 2
END = 3

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
    def testSetMatrixValueAt(self):
        self.m.setMatrixValueAt(self.m.turtle.pos(),1)
        self.assertTrue(self.m.matrix[0][0],1)
    def testDig(self):
        self.m.dig(EAST)
        self.assertTrue( self.m.getMatrixValueAt(self.m.turtle.position())==0)
        self.assertTrue( self.m.turtle.position() == (-170,190))
        self.m.reset()
        self.assertTrue( self.m.dig(WEST) == (-190,190))
        self.m.reset()
        self.m.dig(EAST)
        self.m.dig(SOUTH)
        r=self.m.dig(WEST)
        self.assertTrue(r == (-190,170),"r is " + str(r))
        self.m.reset()
        self.m.dig(EAST)
        self.m.dig(SOUTH)
        self.m.dig(WEST)
        r=self.m.dig(NORTH)
        self.assertTrue( r == (-190,170), "should be at (-190,190) but got " + str(r))
    def testNoBreakThrough(self):
        self.m.setMatrixValueAt((-150,190),0)
        r=self.m.dig(EAST)
        assert r==(-190,190),"Not at Home position, got " + str(r)
    def testAllDirections(self):
        self.m.setMatrixValueAt((-190,150),0)
        print(self.m.turtle.position())
        r=self.m.dig(SOUTH)
        self.assertTrue( r==(-190,190),"got " + str(r))
        self.m.setMatrixValueAt((-150,190),0)
        r=self.m.dig(EAST)
        self.assertTrue( r==(-190,190),"got " + str(r))
        self.m.turtle.goto(-150,150)
        r=self.m.dig(WEST)
        self.assertTrue( r==(-150,150),"got " + str(r))
        self.m.turtle.goto(-190,150)
        r=self.m.dig(NORTH)
        self.assertTrue( r==(-190,150),"got " + str(r))
        self.m.reset()
        r=self.m.dig(NORTH)
        self.assertTrue( r==(-190,190),"got " + str(r))
        self.m.turtle.goto(-190,-170)
        print (self.m.turtle.position()[1]-20)
        r=self.m.dig(SOUTH)
        self.assertTrue( r==(-190,-170),"got " + str(r))
    def testNeighbors(self):
        r=self.m.neighbors()
        self.assertTrue( (r[0][1]==INVALID and r[1][1]==WALL and
                          r[2][1]==WALL and r[3][1]==INVALID),"got " + str(r))
        self.m.reset()
        self.m.turtle.goto(-170,170)
        r = self.m.neighbors()
        self.assertTrue( (r[0][1]==INVALID and r[1][1]==WALL and
                          r[2][1]==WALL and r[3][1]==WALL),"got " + str(r))
        self.m.reset()
        self.m.turtle.goto(-150,150)
        r = self.m.neighbors()
        self.assertTrue( (r[0][1]==WALL and r[1][1]==WALL and r[2][1]==WALL and r[3][1]==WALL), "got " + str(r))

    def testMakeMaze(self):
        self.m.makeMaze()
        self.assertTrue( ((self.m.getMatrixValueAt((-170,190))==EMPTY and
                           self.m.getMatrixValueAt((-150,190))==EMPTY) or  \
       (self.m.getMatrixValueAt((-190,170))==EMPTY and
        self.m.getMatrixValueAt((-190,150))==EMPTY)),"got " + \
       str(self.m.getMatrixValueAt((-170,190))) + "," + \
       str(self.m.getMatrixValueAt((-150,190))) + "," + \
       str(self.m.getMatrixValueAt((-190,170))) + "," + \
       str(self.m.getMatrixValueAt((-190,150))))


class Maze():
    """ This class creates a random maze """
    def __init__(self):
        self.reset()

    def direction(self,pos1,pos2):
        """ returns the direction from position 1 to position 2 """
        if pos1[0]==pos2[0]:
            if pos1[1]>pos2[1]: # North
                return NORTH
            else:
                return SOUTH
        else:
            if pos2[0]>pos1[0]: # East
                return EAST
            else:
                return WEST

    def makeMaze(self):
        n=self.neighbors()
        while len(n)>0:
            nchoice=random.choice(n)
            n.remove(nchoice)
            if nchoice[1]==WALL:
                d=self.direction(self.turtle.position(),nchoice[0])
                self.dig(d)
                self.dig(d)
                return

    def neighbors(self):
        p=self.turtle.position()
        r=[]
        r.append([(p[0],p[1]+40),self.getMatrixValueAt((p[0],p[1]+40))])
        r.append([(p[0],p[1]-40),self.getMatrixValueAt((p[0],p[1]-40))])
        r.append([(p[0]+40,p[1]),self.getMatrixValueAt((p[0]+40,p[1]))])
        r.append([(p[0]-40,p[1]),self.getMatrixValueAt((p[0]-40,p[1]))])
        return r

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

    
    def dig(self,dir):
        if dir == EAST:
            if self.turtle.position()[0]<190:
                if self.turtle.position()[0]+40 > 190:
                    return self.turtle.position()
                if self.getMatrixValueAt((self.turtle.position()[0]+40,self.turtle.position()[1]))>0:
                    self.turtle.goto(self.turtle.position()[0]+20,self.turtle.position()[1])
                    self.setMatrixValueAt(self.turtle.position(),0)
        elif dir == SOUTH:
            if self.turtle.position()[1]>-190:
                if self.turtle.position()[1]-40 < -190:
                    return self.turtle.position()
                if self.getMatrixValueAt((self.turtle.position()[0],self.turtle.position()[1]-40))>0:
                    self.turtle.goto(self.turtle.position()[0],self.turtle.position()[1]-20)
                    self.setMatrixValueAt(self.turtle.position(),0)
        elif dir ==  WEST:
            if self.turtle.position()[0]>-190:
                if self.turtle.position()[1]-40 < -190:
                    return self.turtle.position()
                if self.getMatrixValueAt((self.turtle.position()[0]-40,self.turtle.position()[1]))>0:
                    self.turtle.goto(self.turtle.position()[0]-20,self.turtle.position()[1])
                    self.setMatrixValueAt(self.turtle.position(),0)
        elif dir ==  NORTH:
            if self.turtle.position()[1]<190:
                if self.turtle.position()[1]+40 > 190:
                    return self.turtle.position()
                if self.getMatrixValueAt((self.turtle.position()[0],self.turtle.position()[1]+40))>0:
                    self.turtle.goto(self.turtle.position()[0],self.turtle.position()[1]+20)
                    self.setMatrixValueAt(self.turtle.position(),0)
        return self.turtle.position()
        
    def getMatrixValueAt(self,pos):
        x=int((pos[0]+200)/20)
        y=20-int((pos[1]+200)/20)-1
        if x<0 or y<0 or x>19 or y>19:
            return -1
        v=self.matrix[x][y]
        return v

    def setMatrixValueAt(self,pos,value):
        x=int((pos[0]+200)/20)
        y=20-int((pos[1]+200)/20)-1
        try:
            self.matrix[x][y]=value
        except:
            return False
        oldPos = self.turtle.position()
        self.turtle.goto(pos)
        if value==0:
            self.turtle.color('white')
            self.turtle.stamp()
        if value==1:
            self.turtle.color('blue')
            self.turtle.stamp()
        self.turtle.goto(oldPos)
        return True
    
if __name__ == "__main__":
    unittest.main()
