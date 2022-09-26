from math import pi, degrees, radians
import warnings
from vector import *
width =200
height =200
screen_offset=0
resolution = (width, height)
ant_count = 200
food_stock_count = 3
food_stock=999999999
blocker_stock=120
blocker_ex=True
food_position=[Vector(width-1,height-1)]
evaporation_rate=0.8
alpha=1
beta=5
Nest_radius=1
ant_size = 1
food_radius=5
detection_radius=1
white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
blue  = (0, 0, 255)
green = (0, 255, 0)
yellow= (255, 255, 0)
smell_radius=5
blocker_radius=smell_radius*1.5
wander_delta_angle = pi/2
initial_pheromone=0.1
finished_round=20

def vector_produce(smell_radius):
    a=[]
    radius_1=1+2*smell_radius
    radius_2=(1+2*smell_radius)**2
    for i in range(radius_2):
        m=i%radius_1-smell_radius
        n=-int(i/radius_1)+smell_radius
        a.append([m,n])
    return a
moduel_vector=vector_produce(smell_radius)

def distance_produce(moduel_vector):
    a=[]
    for i in moduel_vector:
        distance=(i[0]**2+i[1]**2)
        a.append(pow(distance,1/2))
    return a
distance_vector=distance_produce(moduel_vector)
def transform(vector_):
    try:
        x=vector_.x
        y=vector_.y
        vector_1=[x,y]
        index=moduel_vector.index(vector_1)
        return index
    except:
        warnings.warn("The vector in tour is wrong")

def anti_transform(indice):
    try:
        x=moduel_vector[indice][0]
        y=moduel_vector[indice][1]
        return Vector(x,y)
    except:
        warnings.warn("the indice of the prefer_matrix is wrong")


def path_transform(startpoint,path):
    for indice in path:
        startpoint+=anti_transform(indice)
    return startpoint



