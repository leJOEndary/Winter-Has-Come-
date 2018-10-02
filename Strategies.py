# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:09:19 2018

@author: Youssef
"""
import abc

class SearchStrategy(abc.ABC):    
    # returns the next move suggested for the agent, which is the node chosen for expansion
    @abc.abstractmethod
    def get_next_move(self):
        pass
    
    
    

class DepthFirst(SearchStrategy):
    
    def get_next_move(self):
        pass   
    # To be discussed
    

class BreadthFirst(SearchStrategy):
    
    def get_next_move(self):
        pass
    # To be discussed
    

class IterativeDeepening(SearchStrategy):
    
    def get_next_move(self):
        pass 
    # To be discussed
    

class UniformCost(SearchStrategy):
    
    def get_next_move(self):
        pass
    # To be discussed
    

class Greedy(SearchStrategy):
    
    def heutistic_one(self):
        pass
    
    def heuristic_two(self):
        pass
    
    def get_next_more(self):
        pass
    # To be discussed
    

class AStar(SearchStrategy):
    
    def heuristic_one(self):
        pass
    
    def heuristic_two(self):
        pass
    
    def get_next_move(self):
        pass
    # To be discussed