# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:16:45 2018

@author: Youssef
"""

# Implemented by Youssef
class State():
        
    # State Constructor
    def __init__(self, grid, row, column, inventory_max, inventory_curr):       
       self.GRID = grid
       self.POS_ROW = row
       self.POS_COLUMN = column
       self.INVENTORY_MAX = inventory_max
       self.INVENTORY_CURR = inventory_curr
       
       
    # Computes next state from the current state and a given action.  
    def get_new_state(self, action):
        
        # Removes neighbouring White Walkers
        def remove_white_walkers(grid, row, column):
            
            if row < len(grid)-1:
                if grid[row+1][column] ==1:
                    grid[row+1][column] = 0   
                    
            if row > 0:
                if grid[row-1][column] ==1:
                    grid[row-1][column] = 0   
                    
            if column < len(grid[0])-1:    
                if grid[row][column+1] == 1:
                    grid[row][column+1] = 0
                    
            if column > 0:
                if grid[row][column-1] == 1:
                    grid[row][column-1] = 0
                
            return grid
       
        
        # Initializing the new state values as the current one
        row = self.POS_ROW
        column = self.POS_COLUMN
        inventory_max = self.INVENTORY_MAX
        inventory_curr = self.INVENTORY_CURR
        
        # The grid must be assigned cell by cell, else it will be assigned by reference and will cause problems.
        grid = self.clone_grid(self.GRID)

        
        # Updating the grid & other state attributes 
        if action == "Attack":
            inventory_curr-=1
            grid = remove_white_walkers(grid, row, column)
        else:
            
            # Updating Position
            if column < len(grid[0])-1: 
                if action == "Right":       
                    column += 1
                    
            if column > 0:
                if action == "Left":
                    column -= 1
                
            if row > 0:
                if action == "Up":
                    row -= 1
                    
            if row < len(grid)-1:
                if action == "Down":
                    row += 1
            
            # Checking & Updating if we step on DragonStone or WhiteWalker or Obstacle
            if grid[row][column] == 2:
                inventory_curr = inventory_max
        
        return State(grid, row, column, inventory_max, inventory_curr)
            
    # Returns different (GRID) object of the same value 
    def clone_grid(self, grid):         
        new_grid = []
        for row in grid:
            new_row = []
            for cell in row:
                new_row.append(cell)
            new_grid.append(new_row)
        return new_grid

    def __str__(self):        
        result = "\n" + "DragonGlass available: " + str(self.INVENTORY_CURR)        
        grid = self.clone_grid(self.GRID)
        
        # Making a J Appear
        jon_x = self.POS_ROW
        jon_y = self.POS_COLUMN
        grid[jon_x][jon_y] = "J"
        
        grid_str = ""
        for row in grid:
            for cell in row:
                if cell == 0:
                    cell = "[ ]"
                elif cell == 1:
                    cell = "[W]"
                elif cell == 2:
                    cell = "[D]"
                elif cell == 3:
                    cell = "[O]"
                else:
                    cell = "[J]"   
                grid_str += cell
            grid_str += "\n"
                    
        result += "\n"+grid_str
        return result
                
            
            
                    
        
        
        
        
        
            
            
        
        
            
            