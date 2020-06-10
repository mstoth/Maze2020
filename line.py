import turtle
s=turtle.Screen()
s.bgcolor('blue')
t=turtle.Turtle()
t.penup()
for x in range(-190,210,20):
    t.goto(x,190)
    t.shape('square')
    t.color('white')
    t.stamp()
