# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:52:24 2018

@author: Youssef
"""

from Strategies import DepthFirst
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
             [0,1,0,0],
             [1,0,1,2],
             [0,0,0,0]]



# Generates a random grid of size MxN (min, 4x4)
def genGrid(length, width):
    # To be implemented, by ...
    return TEST_GRID



# Searches for a possible winning plan
def search(grid, strategy, visualize):
    # implemented by Marwan and Youssef
    
    #
    inventory = random.randint(1,5)
    row = len(grid)-1
    column = len(grid[0])-1
    
    init_state = State(grid, row, column, inventory_curr=inventory, inventory_max=inventory)
    world = SaveWesteros(init_state)
    
    strategy = DepthFirst(world)
    winning_sequence = strategy.form_plan()


    # Visualize the winning plan
    print(winning_sequence)
 
    return ["Representation of the sequence of moves to the goal",
            "Cost of the solution",
            "Number of nodes expanded during search"]
    
    
    
# Visual representation of discovered solution applied to the grid 
def visualize():
    # To be implemented, by ...
    pass



search(TEST_GRID, 1, False)