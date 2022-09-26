import pygame
from parameters import *
from random import randint
from vector import Vector

pygame.font.init()
text_color = (white)


class Bloker:
    def __init__(self, position):
        self.position = position
        self.color = (0, 0 , 255)
        self.radius=blocker_radius

    def Show(self, screen):
        pygame.draw.circle(screen, self.color, self.position.xy(), self.radius)

    def Collide(self,x,y):
        if self.position.WithinRange(Vector(x,y),self.radius):
            return True
        else:
            return False


class BlokerMap:
    def __init__(self, block_stock):
        self.size = blocker_stock
        self.blockers= self.InitializeFood()

    def InitializeFood(self):
        if (blocker_ex==False):
            return []
        else:
            a=[Bloker(Vector(int(1/3*width),i)) for i in range(self.size)]
            b=[Bloker(Vector(int(2/3*width),height-i-1)) for i in range(self.size)]
            return a+b

    def Show(self, screen):
        for blocker in self.blockers:
            blocker.Show(screen)

