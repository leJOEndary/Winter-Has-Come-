# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:52:24 2018

@author: Youssef
"""

from Strategies import DepthFirst, BreadthFirst, UniformCost, IterativeDeepening, Greedy, AStar
from SavingWesteros import SaveWesteros
from State import State
import random
import time

###############################################################################
# We will represent the grid using a 2d array of numbers from: {0,1,2,3}
# 0 = Empty Cell
# 1 = White Walker Cell
# 2 = The DragonStone Castle
# 3 = Obstacle
###############################
# Controls #
############

STRATEGY = "AS"

VISUALIZE = True


INPUT_GRID =[[1,0,1,3],
             [0,3,0,1],
             [3,0,1,3],
             [2,0,0,0]]

# Will be used to generate a random grid if the RANDOMIZE_GRID = True
RANDOMIZE_GRID = False
LENGTH = 4
WIDTH = 4
######################################################
###############################

strategies_dic = {"DF":DepthFirst,
                  "BF":BreadthFirst,
                  "ID":IterativeDeepening,
                  "UC":UniformCost,
                  "GD":Greedy,
                  "AS":AStar} 

# Generates a random grid of size MxN (min, 4x4)
def genGrid():
    if not RANDOMIZE_GRID:
        return INPUT_GRID
    else:       
        grid = []
        print("Generated Grid :")
        for i  in range(LENGTH):
            row = []
            for j in range(WIDTH):
                cell = random.randint(0,3)
                row.append(cell)
            print("                  ",row)
            grid.append(row)
            
        print()
        return grid
        


# Searches for a possible winning plan
def search(grid, strategy, visualize):
    
    # Initializing the world using the Initial State
    inventory = 1#random.randint(1,5)
    row = len(grid)-1 
    column = len(grid[0])-1  
    init_state = State(grid, row, column, inventory_curr=inventory, inventory_max=inventory)   
    world = SaveWesteros(init_state)       
    print("Inventory size  :  ", inventory)
    print("Strategy        :  ", strategy)
    
    # Initializing a strategy instance corresponding to given strategy
    try:
        strategy_Object = strategies_dic[strategy[:2]](world, strategy[2])
    except:
        strategy_Object = strategies_dic[strategy](world)
    
    # Computing the final node
    print("Formulating winning plan...      ", end='')
    final_node = strategy_Object.form_plan()
    print("[Done]\n")
    # Parsing node to Actions and Cost
    representation_of_moves_to_goal = world.parse_action_sequence(final_node)
    solution_cost = world.path_cost(final_node) 
    
    # Visualize the winning plan
    if visualize:
        visualize_plan(final_node)
    
    return [representation_of_moves_to_goal,
            solution_cost,
            final_node.ID]


        
# Visual representation of discovered solution applied to the grid 
def visualize_plan(node):    
    current = node
    states = []
    while current != None:        
        states.append((current.ACTION, current.STATE))
        current = current.PARENT
    
    states.reverse()    
    for i,state in enumerate(states):
        time.sleep(1)
        print("{}-".format(i+1), state[0], state[1])
        

        
result = search(genGrid(), STRATEGY, VISUALIZE)
print("Winning Sequence:  ",result[0])
print("Solution Cost   :  ",result[1])
print("Expanded Nodes  :  ",result[2])

    