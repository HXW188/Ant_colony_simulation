import pygame
from parameters import *
from vector import Vector
from colony import Colony



pygame.display.init()
screen = pygame.display.set_mode(resolution)
food_position=food_position
nest_position=Vector(0,0)
pause = False
screen.fill((255, 255, 255))
colony = Colony(nest_position, food_position)




#If you want to run the experiment 1 and 2 use this code
while True:
    if not pause:
        screen.fill((255, 255, 255))
    for event in pygame.event.get():
        pass
    if not pause:
        colony.Update()
        colony.Show(screen)
        if colony.replex>=22:
            colony.Showpath(screen)
        pygame.display.flip()
pygame.quit()





#If you want to run the experiment 3 and 4 use this code
# path=colony.find_best_path(nest_position, food_position,screen)
# mid_path=[]
# final_path=[]
# division=4
# for i in range(division):
#     mid_path.append(path[int(i*len(path)/division):int((i+1)*len(path)/division)])
# start_point=nest_position
# for path in mid_path:
#     end_point=path_transform(start_point,path)
#     end_point_1=[end_point]
#     path_123=colony.find_best_path_3(start_point, end_point_1, screen)
#     print(path_123)
#     for i in path_123:
#         final_path.append(i)
#     start_point=end_point
# print(final_path)
# length=0
# for i in final_path:
#     length+=distance_vector[i]
# print(length)
# for i in range(50):
#     colony.nest.path.append(final_path)
#     colony.nest.Update_pheromone()
# while(True):
#     for event in pygame.event.get():
#         pass
#     screen.fill((255, 255, 255))
#     colony.Update()
#     colony.Show(screen)
#     if colony.replex >= 22:
#             colony.Showpath(screen)
#     pygame.display.flip()