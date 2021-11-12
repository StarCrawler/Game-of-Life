import pygame as pg
import sys

pg.font.init()
displaySize = width, height = 720, 576
screen = pg.display.set_mode(displaySize)

class Button(object):
    """docstring for Button."""


    def __init__(self, Name, Width, Height, Color, XPos, YPos, Display):
        self.hisName = Name
        self.hisWidth = Width
        self.hisHeight = Height
        self.hisColor = Color
        self.hisX = XPos
        self.hisY = YPos
        self.hisDisplay = Display
        self.buttonFont = pg.font.SysFont('Comic sans MS', 20)


    def printButton(self):
        text = self.buttonFont.render(self.hisName, True, pg.Color(0, 0, 0))
        pg.draw.rect(self.hisDisplay, self.hisColor, pg.Rect(self.hisX, self.hisY, self.hisWidth, self.hisHeight))
        self.hisDisplay.blit(text,(200,100+(50-10)))

    def isClicked(self):

testButton = Button("Test", 200, 100, pg.Color(100, 100, 100), 100, 100, screen )
while 1:
    screen.fill(pg.Color(255, 255, 255))
    testButton.printButton()
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
             sys.exit(0)
