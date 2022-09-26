import pygame
from parameters import *
from random import randint
from vector import Vector

pygame.font.init()
text_color = (white)

class Food:
    def __init__(self, position):
        self.position = position
        self.stock = food_stock
        self.bite_size = 1
        self.color = (220, 130 , 30)
        self.radius=food_radius

    def Bite(self):
        self.stock -= self.bite_size

    def Update(self):
        if self.stock < 0:
            pass

    def Collide(self,x,y):
        if self.position.WithinRange(Vector(x,y),self.radius):
            return True
        else:
            return False

    def Show(self, screen, show_remaining = True):
        if self.stock > 0 :
            pygame.draw.circle(screen, self.color, self.position.xy(), 1)
        if show_remaining:
            text_font = pygame.font.SysFont("Arial", 1)
            text_surface = text_font.render(str(self.stock), True, text_color)
            text_rectangle = text_surface.get_rect(center=self.position.xy())
            screen.blit(text_surface, text_rectangle)
class FoodMap:
    def __init__(self,position):
        self.size = food_stock
        self.foods = self.InitializeFood(position)

    def InitializeFood(self,position):
        return[Food(positions) for positions in position]
        return [Food(Vector(width-1,height-1))]
        return [ Food(Vector(randint(screen_offset, width-screen_offset), randint(screen_offset, height-screen_offset))) for _ in range(self.size)]

    def Update(self):
        for f in self.foods:
            f.Update()
            if f.stock <= 0:
                self.foods.remove(f)

    def Show(self, screen):
        for food in self.foods:
            food.Show(screen)
