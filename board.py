from parameters import *

class Board:
    def __init__(self,block,food):
        self.block=block
        self.food=food
        self.board=[]
        for i in range(width):
            self.board.append([])
            for j in range(height):
                self.board[i].append(variable(block,food,i,j))
    def Update(self):
        for i in range(width):
            self.board.append([])
            for j in range(height):
                self.board[i][j].update()

class variable:
    def __init__(self,block,food,i,j):
        self.block_list=[]
        self.food_list=[]
        for blocks in block.blockers:
            if blocks.Collide(i,j):
                self.block_list.append(blocks)
        for foods in food.foods:
            if foods.Collide(i,j):
                self.food_list.append(foods)
        if len(self.block_list)==0:
            self.block=False
        else:
            self.block=True
        if len(self.food_list)==0:
            self.food=False
        else:
            self.food=True
    def update(self):
        for food in self.food_list:
            if(food.stock<=0):
                self.food_list.remove(food)
        if len(self.food_list)==0:
            self.food=False
        else:
            self.food=True



