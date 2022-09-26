from parameters import *
import pygame
from vector import Vector
import random
import numpy as np
from math import exp

class Pheromone:
    def __init__(self):
        a=[]
        for i in range(width):
            a.append([])
            for j in range(height):
                a[i].append([])
                for k in range((1+2*smell_radius)**2):
                    a[i][j].append(0.1)
        self.prefer_matrix=a
        self.evaporation_rate=evaporation_rate

    def init_para(self,board):
        count=0
        for i in range(width):
            for j in range(height):
                c=Vector(i,j)
                self.prefer_matrix[i][j][int(((1+2*smell_radius)**2-1)/2)]=0
                for indice in range((1+2*smell_radius)**2):
                    flag_matrix=anti_transform(indice)
                    matrix=c+flag_matrix
                    x=matrix.x
                    y=matrix.y
                    if(x>=0 and y>=0 and x<=width-1 and y<=height-1):
                        if(board.board[x][y].block):
                            self.prefer_matrix[i][j][indice]=0
                            # print(i,j,indice,'\n')
                    elif(x<0 or y<0 or x>=width or y>=height):
                        self.prefer_matrix[i][j][indice] = 0
                        # print(i, j, indice, '\n')
                        count += 1
    def pheromone_direction(self,position):
        x=position.x
        y=position.y
        pre_matrix=self.prefer_matrix[x][y]
        count = 0
        para_2 = []
        for zeta in pre_matrix:
            length = anti_transform(count).Magnitude()
            count = count + 1
            para_2.append(length)
        para_1 = pre_matrix
        denomitor = 0
        chosen_sequence = []
        for i in range(len(para_1)):
            value = pow(para_1[i], alpha) * pow(para_2[i], beta)
            chosen_sequence.append(value)
            denomitor += value
        chosen_sequence = [i / denomitor for i in chosen_sequence]
        chosen_sequence = np.array(chosen_sequence)
        index = [i for i in range(len(chosen_sequence))]
        max_index = np.random.choice(index, p=chosen_sequence.ravel())
        velocity=anti_transform(max_index)
        return(velocity)

    def offline_update(self,x,y,indice):
        self.prefer_matrix[x][y][indice]=(1-self.evaporation_rate)* self.prefer_matrix[x][y][indice]+self.evaporation_rate*initial_pheromone

    def ACS_online_update(self,start_position,path_way):
        for i in range(width):
            for j in range(height):
                for indice in range(len(self.prefer_matrix[i][j])):
                    self.prefer_matrix[i][j][indice]*=(1-self.evaporation_rate)
        for path in path_way:
            x = start_position.x
            y = start_position.y
            length=0
            for indice in path:
                length+=distance_vector[indice]
            for indice in path:
                self.prefer_matrix[x][y][indice]+=200/(length)
                velocity=anti_transform(indice)
                x+=velocity.x
                y+=velocity.y


    def AC_online_update(self,start_position,path_way):
        for i in range(width):
            for j in range(height):
                for indice in range(len(self.prefer_matrix[i][j])):
                    self.prefer_matrix[i][j][indice]*=(1-self.evaporation_rate)
        for path in path_way:
            x = start_position.x
            y = start_position.y
            length=0
            for indice in path:
                length+=distance_vector[indice]
            for indice in path:
                self.prefer_matrix[x][y][indice]+=50/(length)
                velocity=anti_transform(indice)
                x+=velocity.x
                y+=velocity.y


