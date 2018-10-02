# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:26:16 2018

@author: Youssef
"""
import abc


class GeneralSearchProblem(abc.ABC):
    
    # The set of possible actions available to the agent
    @abc.abstractmethod
    def operators(self):
        pass

    # The initial state of our problem
    @abc.abstractmethod
    def initial_state(self):
        pass
    
    # The set of states reachable from the initial state by any sequence of actions.
    @abc.abstractmethod
    def state_space(self):
        pass
    
    # This function is used by the agent to test if a Goal State is reached
    @abc.abstractmethod
    def goal_test(self):
        pass

    # This function assigns cost to a sequence of actions. 
    # Typically, it is the sum of the costs of individual actions
    # in the sequence.
    @abc.abstractmethod
    def path_cost(self):
        pass
      