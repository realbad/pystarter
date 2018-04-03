from graphics import *

p1 = Point(100, 100)
print(p1.getX())
p2 = Point(169, 21)
print(p2.getY())

win = GraphWin()
p1.draw(win)
p2.draw(win)
win.getMouse()