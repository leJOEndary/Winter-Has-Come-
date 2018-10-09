# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:52:24 2018

@author: Youssef
"""

from Strategies import DepthFirst, BreadthFirst, UniformCost, IterativeDeepening, Greedy, AStar
from SavingWesteros import SaveWesteros
from State import State
import random


###############################################################################
# We will represent the grid using a 2d array of numbers from: {0,1,2}
# 0 = Empty Cell
# 1 = White Walker Cell
# 2 = The DragonStone Castle
###############################
TEST_GRID = [[1,0,1,0],
             [0,0,0,2],
             [0,0,0,0],
             [0,2,0,0]]

strategies_dic = {"DF":DepthFirst,
                  "BF":BreadthFirst,
                  "ID":IterativeDeepening,
                  "UC":UniformCost,
                  "GD":Greedy,
                  "AS":AStar} 

# Generates a random grid of size MxN (min, 4x4)
def genGrid(length, width):
    # To be implemented, by ...
    return TEST_GRID




# Searches for a possible winning plan
def search(grid, strategy, visualize):
    # implemented by Marwan and Youssef
    
    # Initializing the world using the Initial State
    inventory = random.randint(1,5)
    row = len(grid)-1 
    column = len(grid[0])-1  
    init_state = State(grid, row, column, inventory_curr=inventory, inventory_max=inventory)   
    world = SaveWesteros(init_state) 
    
    # Initializing a strategy instance corresponding to given strategy
    strategy_Object = strategies_dic[strategy](world)  
    
    # Computing the final node  
    final_node = strategy_Object.form_plan()

    # Parsing node to Actions and Cost
    representation_of_moves_to_goal = world.parse_action_sequence(final_node)
    solution_cost = world.path_cost(final_node) 
    

    # Visualize the winning plan
    #if visualize:
    #   visualize(final_node)
    #################### 
 
    return [representation_of_moves_to_goal,
            solution_cost,
            final_node.ID]

    
    
# Visual representation of discovered solution applied to the grid 
def visualize():
    # To be implemented, by ...
    pass



res = search(TEST_GRID, "UC", False)
print(res)