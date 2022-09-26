import pygame
from parameters import *
from vector import Vector
from math import pi, degrees, radians
import random

class Ant:
    def __init__(self,nest,board,pheromone):
        self.nest = nest
        self.position=self.nest.position
        self.tour=[]
        self.path_length=0
        self.board=board
        self.detection_radius=detection_radius
        self.velocity=Vector(0,0)
        self.has_food=False
        self.mode="Food"
        self.color=black
        self.pheromone=pheromone
        self.radius=ant_size
    def Update(self):
        # if(self.path_length>=1.5*self.nest.minimum_striddle):
        #     self.mode="Home"
        flag=self.UpdateVelocity()
        # if(flag==1):
        #     if(self.has_food==False):
        #         if(len(self.tour)!=0):
        #             print("have a look")
        #             x=self.position.x
        #             y=self.position.y
        #             indice=self.tour[len(self.tour)-1]
        #             self.pheromone.offline_update(x,y,indice)
        #             self.position=self.position+self.velocity
        #     else:
        #         self.position=self.position+self.velocity
        # else:
        self.position=self.position+self.velocity
    def UpdateVelocity(self):
        if self.has_food == True:
            self.ReturnToNest()
            self.nest.miss=0
            return 0
        elif self.mode=="Home":
            self.ReturnToNest()
            self.nest.miss+=1
            return 0
        else:
            self.SearchForFood()
            return 1
    def ReturnToNest(self):
        if(self.position.WithinRange(self.nest.position,self.nest.radius)):
            self.back_home()
            return
        indice=self.tour[len(self.tour)-1]
        self.velocity =anti_transform(indice).Negate()
        self.tour.pop()
    def SearchForFood(self):
        x=self.position.x
        y=self.position.y
        if self.board.board[x][y].food:
            self.TakeFood(self.board.board[x][y].food_list[0])
            self.back_home()
            return 0
        self.follow_pheromone()
        return 1
    def follow_pheromone(self):
        self.velocity=self.pheromone.pheromone_direction(self.position)
        indice=transform(self.velocity)
        self.tour.append(indice)
        self.path_length+=self.velocity.Magnitude()
    def back_home(self):
        self.position = self.nest.position
        self.tour = []
        self.velocity=Vector(0,0)
        self.path_length=0
        self.has_food=False
        self.mode="Food"
        self.nest.stock+=1
    def TakeFood(self, food):
        self.has_food = True
        self.velocity=Vector(0,0)
        self.nest.found_path+=1
        self.nest.path.append(self.tour)
        if(self.path_length<=self.nest.min_striddle):
            self.nest.min_striddle=self.path_length
            self.nest.shortest_path=self.tour
        food.Bite()
    def Show(self, screen):
        pygame.draw.circle(screen, self.color, self.position.xy(), self.radius)