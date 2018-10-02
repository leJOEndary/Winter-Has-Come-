# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:47:57 2018

@author: Youssef
"""

class Node():
    
    # This is the constructor.
    # Action is a string that indicated the type of the node.
    # We'll represent the children using an array of nodes.
    def __init__(self, action, cost=None, children=[]):      
        # These are the default costs for each action
        # In case of killing, cost should vary depending on the number of adjacent white walkers.
        cost_default =  {"Initial":0,
                         "Up":1,
                         "Down":1,
                         "Right":1,
                         "Left":1,
                         "Kill":2}
        
        self.ACTION = action
        self.COST = cost_default[action] if cost == None else cost
        self.CHILDREN = children
    
    
    def add_child(self, node):
        self.CHILDREN.append(node)
      
    # This function is basically python version of toString
    def __str__(self):       
        return str({"Action":self.ACTION,
                    "Cost":self.COST,
                    "Children":self.CHILDREN})
        
    # To be discussed