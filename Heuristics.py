# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:46:03 2018

@author: Youssef
"""

class Heuristics():
    
    def __init__(self, Mode):
        self.MODE = Mode
        
        
    def heuristic(self, action, state):
        if self.MODE == "1":
            return self.heuristic_one(action, state)
        else:
            return self.heuristic_two(action, state)
    
    
    
    def heuristic_one(self, action, state):
        
        if action != "Attack":
            grid = state.GRID
            current_row = state.POS_ROW
            current_col = state.POS_COLUMN
            

            # Updating Position
            coords = self.update_position(current_row, current_col, action, grid)
            
            # Get coordinates of each whitewalker (1) in the grid
            ww_locations = self.locate_value(grid, 1)

            # Calculate sum of manhatten distance between updated position and each whitewalker
            total_distance=0

            for location in ww_locations:           
                distance= self.get_manhatten_distance(coords[0],coords[1],location[0], location[1])     
                total_distance+=distance
              
            if total_distance > 0:
                return total_distance//len(ww_locations)
            else:
                return 99    
        else:    
            return 0
        
   
    

    def heuristic_two(self, action, state):

        if state.INVENTORY_CURR > 0:
            return self.heuristic_one(action, state)

        else:
            grid = state.GRID
            current_row = state.POS_ROW
            current_col = state.POS_COLUMN

            # Updating Position
            new_row, new_col = self.update_position(current_row, current_col, action, grid)

            # Get coordinates of the DragonStone (2) in the grid
            dragon_stone_location = self.locate_value(grid, 2)[0]

            # Get manhatten_distance
            distance_to_dragonstone = self.get_manhatten_distance(new_row,new_col, dragon_stone_location[0], dragon_stone_location[1])    
            
            return distance_to_dragonstone
        
        
        
     ###################################################
                         # Helpers #
                 ############################
        
        
        
    def locate_value(self, grid, value):
        positions = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == value:
                    positions.append((i,j))
        return positions
    
    

    def get_manhatten_distance(self, x1, y1, x2, y2):
        delta_x = abs(x1-x2)
        delta_y = abs(y1-y2)
        return delta_x + delta_y
        
        
        
    def update_position(self, current_row, current_col, action, grid):
        if current_col < len(grid[0])-1: 
            if action == "Right":                     
                current_col += 1
        if current_col > 0:
            if action == "Left":
                current_col -= 1
            
        if current_row > 0:
            if action == "Up":
                current_row -= 1
        if current_row < len(grid)-1:
            if action == "Down":
                current_row += 1
        
        return (current_row, current_col)