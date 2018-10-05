# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:47:57 2018

@author: Youssef
"""

class Node():
    
    # This is the node constructor.
    # Action is a string that indicated the type of the node.
    # Depth is the depth of this node
    # Parent is the parent node
    # State is the State of the game at this node
    def __init__(self, action, parent, depth, state):     
        self.ACTION = action
        self.STATE = state
        self.DEPTH = depth
        self.PARENT = parent
    
    
