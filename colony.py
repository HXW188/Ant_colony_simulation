from parameters import *
from vector import *
from nest import *
from pheromone import *
from food import *
from board import *
import time
from blocker import *


class Colony:
    def __init__(self,nest_position,food_position):
        self.food = FoodMap(food_position)
        self.replex=0
        self.blocker=BlokerMap(blocker_stock)
        self.pheromone = Pheromone()
        self.board=Board(self.blocker,self.food)
        self.nest = Nest(nest_position, ant_count,self.pheromone,self.board)
        self.pheromone.init_para(self.board)
        self.time_past=[time.time()]

    def Update(self):
        self.nest.Update()
        self.food.Update()
        self.board.Update()
        if(self.replex<=2):
            if(self.nest.found_path>=2+self.replex):
                self.time_past.append(time.time())
                self.replex += 1
                self.nest.Update_pheromone_1()
                print(format(self.nest.min_striddle, '.2f'), self.replex,format(self.time_past[len(self.time_past) - 1] - self.time_past[len(self.time_past) - 2], '.2f'))
                return()
        if(self.nest.found_path>=finished_round):
            self.time_past.append(time.time())
            self.replex+=1
            self.nest.Update_pheromone()
            print(  format(self.nest.min_striddle, '.2f'),self.replex,       format(self.time_past[len(self.time_past)-1]-self.time_past[len(self.time_past)-2], '.2f'))

    def Update_1(self):
        self.nest.Update()
        self.food.Update()
        self.board.Update()
        if (self.nest.found_path >= finished_round):
            self.time_past.append(time.time())
            self.replex += 1
            self.nest.Update_pheromone()
            print(format(self.nest.min_striddle, '.2f'), self.replex,
                  format(self.time_past[len(self.time_past) - 1] - self.time_past[len(self.time_past) - 2], '.2f'))


    def find_best_path(self,start_point,end_point,screen):
        colony=Colony(start_point,end_point)
        pygame.display.init()
        pause=False
        while(colony.replex<=28):
            if not pause:
                screen.fill((255, 255, 255))
            for event in pygame.event.get():
                pass
            if not pause:
                colony.Update()
                colony.Show(screen)
                if colony.replex >= 22:
                    colony.Showpath(screen)
                pygame.display.flip()
        return colony.nest.shortest_path

    def find_best_path_3(self,start_point,end_point,screen):
        colony=Colony(start_point,end_point)
        pygame.display.init()
        pause=False
        while(colony.replex<=28):
            if not pause:
                screen.fill((255, 255, 255))
            for event in pygame.event.get():
                pass
            if not pause:
                colony.Update_1()
                colony.Show(screen)
                if colony.replex >= 22:
                    colony.Showpath(screen)
                pygame.display.flip()
        return colony.nest.shortest_path



    def find_best_path_2(self,start_point,end_point,screen):
        colony=Colony(start_point,end_point)
        pygame.display.init()
        pause=False
        while(colony.replex<=28):
            if not pause:
                screen.fill((255, 255, 255))
            for event in pygame.event.get():
                pass
            if not pause:
                colony.Update()
                colony.Show(screen)
                if colony.replex >= 22:
                    colony.Showpath(screen)
                pygame.display.flip()
        return colony.nest.shortest_path



    def find_best_path_1(self,start_point,end_point,screen):
        colony = Colony(start_point, end_point)
        while (colony.nest.found_path < 1):
            screen.fill((255, 255, 255))
            colony.Update()
            colony.Show(screen)
            pygame.display.flip()
        path=colony.nest.path[0]
        mid_path = []
        final_path = []
        division = 10
        for i in range(division):
            mid_path.append(path[int(i * len(path) / division):int((i + 1) * len(path) / division)])
        start_point = start_point
        for path in mid_path:
            end_point = path_transform(start_point, path)
            path_123 = colony.find_best_path(start_point, end_point, screen)
            print(path_123)
            for i in path_123:
                final_path.append(i)
            start_point = end_point
        for i in range(2):
            colony.nest.path.append(final_path)
            colony.nest.Update_pheromone()
        while (True):
            screen.fill((255, 255, 255))
            colony.Update()
            colony.Show(screen)
            pygame.display.flip()

    def ReUpdate(self):
        self.nest.path=self.nest.shortest_path
        self.pheromone.__init__()
        self.pheromone.init_para()
        self.nest.Update_pheromone()

    def Show(self, screen):
        self.nest.Show(screen)
        self.food.Show(screen)
        self.blocker.Show(screen)

    def Showpath(self,screen):
        self.food.Show(screen)
        self.blocker.Show(screen)
        path=self.nest.shortest_path
        nest=self.nest.position
        for i in path:
            pygame.draw.circle(screen, red, nest.xy(), 1)
            nest=nest+anti_transform(i)


