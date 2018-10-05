# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:09:19 2018

@author: Youssef
"""
import abc
from Node import Node
from queue import Queue

class SearchStrategy(abc.ABC):    
    # returns the next move suggested for the agent, which is the node chosen for expansion
    @abc.abstractmethod
    def form_plan(self):
        pass
    
    
    
# Stack
# Implemented by Marwan and Youssef
class DepthFirst(SearchStrategy):
    
    
    def __init__(self, world):
        self.WORLD = world
        root = Node("Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root        
        self.ACTION_STACK = world.operators(world.INITIAL_STATE)
        
    
    
    # Computes the next node & state from the current ones
    def create_node(self):
        
        # Action is determined from the action_stack
        next_action = self.ACTION_STACK.pop()
        old_node = self.CURRENT
        new_state = old_node.STATE.get_new_state(next_action)
              
        parent = old_node
        if not new_state.ALIVE:
            while parent.ACTION == "Attack":
                parent = parent.PARENT
        else:
            possible_operators = self.WORLD.operators(new_state)
            self.ACTION_STACK.extend(possible_operators) 
            
        # update the new current node
        self.CURRENT = Node(next_action, parent, parent.DEPTH+1, new_state)
        
    
    # Calls create_node() continously until it reachs a goal node/state, then it returns the winning sequence.
    def form_plan(self):
        self.create_node()
        return "Dummy"
    # To be discussed
    
  
    
# Queue
class BreadthFirst(SearchStrategy):
    
    def get_next_move(self):
        pass
    # To be discussed
    

# Stack with increasing max size
class IterativeDeepening(SearchStrategy):
    
    def get_next_move(self):
        pass 
    # To be discussed
    

# ??
class UniformCost(SearchStrategy):
    
    def get_next_move(self):
        pass
    # To be discussed
    

# ??
class Greedy(SearchStrategy):
    
    def heutistic_one(self):
        pass
    
    def heuristic_two(self):
        pass
    
    def get_next_more(self):
        pass
    # To be discussed
    

# ??
class AStar(SearchStrategy):
    
    def heuristic_one(self):
        pass
    
    def heuristic_two(self):
        pass
    
    def get_next_move(self):
        pass
    # To be discussed