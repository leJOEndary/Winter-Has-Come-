# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:32:40 2018

@author: Youssef
"""
from SearchProblem import GeneralSearchProblem
from Node import Node

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
def Search(grid, strategy, visualize):
    # To be implemented
    return ["Representation of the sequence of moves to the goal",
            "Cost of the solution",
            "Number of nodes expanded during search"]
 
    
    
# Visual representation of discovered solution applied to the grid 
def visualize():
    # To be implemented, by ...
    pass




    
class SaveWesteros(GeneralSearchProblem):
    

    # This function is used by the agent to test if a Goal State is reached
    def goal_test(self):     
        # To be implemented, by ...
        return False

    
    
    # The initial state of our problem
    def initial_state(self):
        # To be implemented, by ...
        return None
        
    

    # This function assigns cost to a sequence of actions. 
    # Typically, it is the sum of the costs of individual actions
    # in the sequence.
    def path_cost(self, sequence):    
        # To be implemented, by ...
        return None

    
    
    # The set of states reachable from the initial state by any sequence of actions.
    #
    # N.B. Norhan mentioned that we will need to avoid pre-calculating all 
    # states and rather calculate each state as we encounter it to save space.
    def state_space(self):
        # To be implemented, by ...
        return None

    

    # The set of possible actions available to the agent
    def operators(self):  
        return ["Up",
                "Down",
                "Right",
                "Left",
                "Attack"]
 
    

