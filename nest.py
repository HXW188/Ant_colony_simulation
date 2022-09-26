import random
import pygame
from vector import Vector
from parameters import *
from ant import Ant

pygame.font.init()
text_color = (white)
text_font = pygame.font.SysFont("Arial", 35)

class Nest:
    def __init__(self, position, n_ants,pheromone,board):
        self.position = position
        self.n_ants   = n_ants
        self.stock    = 0
        self.board=   board
        self.radius   = Nest_radius
        self.color    = blue
        self.pheromone= pheromone
        self.shortest_path=[]
        self.minimum_striddle=999999
        self.path=[]
        self.miss=0
        self.found_path=0
        self.min_striddle=999999
        self.ants     = self.InitializeAnts()

    def InitializeAnts(self):
        return [Ant(self,self.board ,self.pheromone) for _ in range(self.n_ants)]

    def Update(self):
        for ant in self.ants:
            ant.Update()
        # if(self.miss>=self.n_ants*200):
        #     self.pheromone.__init__()

    def Update_pheromone(self):
        # self.pheromone.ACS_online_update(self.position,self.shortest_path,self.min_striddle)
        self.pheromone.AC_online_update(self.position,self.path)
        for ant in self.ants:
            ant.back_home()
        self.found_path=0
        self.minimum_striddle=self.min_striddle
        self.path=[]

    def Update_pheromone_1(self):
        self.pheromone.ACS_online_update(self.position,self.path)
        for ant in self.ants:
            ant.back_home()
        self.found_path=0
        self.minimum_striddle=self.min_striddle
        self.path=[]


    def Show(self, screen, show_stock=True):
        pygame.draw.circle(screen, self.color, self.position.xy(), self.radius)
        if show_stock:
            text_surface = text_font.render(str(self.stock), True, text_color)
            text_rectangle = text_surface.get_rect(center=self.position.xy())
            screen.blit(text_surface, text_rectangle)
        for ant in self.ants:
            ant.Show(screen)



