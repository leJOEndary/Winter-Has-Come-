# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:32:40 2018

@author: Youssef
"""
from SearchProblem import GeneralSearchProblem
from Node import Node


 
    

    
class SaveWesteros(GeneralSearchProblem):    

    def __init__(self, initial_state):
        self.INITIAL_STATE =  initial_state
        
        
    
    # This function is used by the agent to test if a Goal State is reached
    def goal_test(self):     
        # To be implemented, by ...
        return False

    
    
    # The initial state of our problem
    def initial_state(self):
        # To be implemented, by ...
        return self.INITIAL_STATE
        
    

    # This function assigns cost to a sequence of actions. 
    # Typically, it is the sum of the costs of individual actions
    # in the sequence.
    def path_cost(self, sequence):    
        # To be implemented, by ...
        
        # These are the default costs for each action
        # In case of killing, cost should vary depending on the number of adjacent white walkers.
        cost_default =  {"Initial":0,
                         "Up":1,
                         "Down":1,
                         "Right":1,
                         "Left":1,
                         "Kill":10}
        return None

    
    
    # The set of states reachable from the initial state by any sequence of actions.
    #
    # N.B. Norhan mentioned that we will need to avoid pre-calculating all 
    # states and rather calculate each state as we encounter it to save space.
    def state_space(self):
        # To be implemented, by ...
        return None

    

    # The set of possible actions available to the agent, in the current state
    def operators(self, state): 
        #implemented by Marwan & Youssef      
        result=[]
        
        if state.POS_ROW < len(state.GRID)-1:
            result.append("Down")
            
        if state.POS_COLUMN < len(state.GRID[0])-1:
            result.append("Right")   
            
        if state.POS_COLUMN > 0:
            result.append("Left")
            
        if state.POS_ROW > 0:
            result.append("Up")
            
        if self.jonInDanger(state):
            result.append("Attack")
            
        return result
 
    
    
    
    # Returns true if there's an adjacent WhiteWalker (Represented by 1 in the grid)
    def jonInDanger(self, state):
        #implemented by Marwan & Youssef  
        row = state.POS_ROW
        column = state.POS_COLUMN
        grid = state.GRID
    
        # Checking for danger down
        if row < len(grid)-1:
            if grid[row+1][column] == 1:
                return True
            
        # Checking for danger right
        if column < len(grid[0])-1:
            if grid[row][column+1] == 1:
                return True
            
        # Checking for danger up
        if row > 0:
            if grid[row-1][column] == 1:
                return True
            
        # Checking for danger left
        if column > 0:
            if grid[row][column-1] == 1:
                return True
                         
        return False

    