# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:16:45 2018

@author: Youssef
"""

# Implemented by Marwan and Youssef
class State():
        
    def __init__(self, grid, row, column, inventory_max, inventory_curr, alive=True):
       
       self.GRID = grid
       self.POS_ROW = row
       self.POS_COLUMN = column
       self.INVENTORY_MAX = inventory_max
       self.INVENTORY_CURR = inventory_curr
       self.ALIVE = alive
       
    
    
       
    def get_new_state(self, action):
        
        def remove_white_walkers(grid, row, column):
            grid[row+1][column] = 0
            grid[row-1][column] = 0
            grid[row][column+1] = 0
            grid[row][column-1] = 0
            return grid
       
        row = self.POS_ROW
        column = self.POS_COLUMN
        inventory_max = self.INVENTORY_MAX
        inventory_curr = self.INVENTORY_CURR
        grid = self.GRID
        alive = self.ALIVE
        
        
        if action == "Attack":
            inventory_curr-=1
            grid = remove_white_walkers(grid, row, column)
        
        else:
        
            if action == "Right":
                column += 1
            if action == "Left":
                column -= 1
            if action == "Up":
                row -= 1
            if action == "Down":
                row += 1
            
            if grid[row][column] == 2:
                inventory_curr == inventory_max
            if grid[row][column] == 1:
                alive = False
        
        
        return State(grid, row, column, inventory_max, inventory_curr, alive)
            
        
            
        
            
            
        
        
            
            