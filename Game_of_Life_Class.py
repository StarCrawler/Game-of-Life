import pygame as pg

class Button(object):
    """docstring for Button."""


    def __init__(self, Name, Color, XPos, YPos, Display):
        self.hisName = Name
        self.startColor = Color
        self.hisColor = 0
        self.hisWidth = 0
        self.hisHeight = 0
        self.hisX = XPos
        self.hisY = YPos
        self.hisDisplay = Display
        self.buttonFont = pg.font.SysFont('Comic sans MS', 20)


    def printButton(self):
        text = self.buttonFont.render(self.hisName, True, pg.Color(0, 0, 0))
        self.hisWidth = text.get_rect()[2] + 20
        self.hisHeight = text.get_rect()[3] + 20
        pg.draw.rect(self.hisDisplay, self.hisColor, pg.Rect(self.hisX, self.hisY, self.hisWidth, self.hisHeight))
        self.hisDisplay.blit(text,(self.hisX + self.hisWidth/2 - text.get_rect()[2]/2,self.hisY + self.hisHeight/2 - text.get_rect()[3]/2))

    def isCollided(self,Pos):
        if Pos[0] >= self.hisX and Pos[0] <= self.hisX + self.hisWidth and Pos[1] >= self.hisY and Pos[1] <= self.hisY + self.hisHeight:
            return True

    def isClicked(self):
        if pg.mouse.get_pressed()[0] and self.isCollided(pg.mouse.get_pos()):
            return True

    def isHoover(self):
        if self.isCollided(pg.mouse.get_pos()):
            self.hisColor = pg.Color(200,200,200)
        else:
            self.hisColor = self.startColor
