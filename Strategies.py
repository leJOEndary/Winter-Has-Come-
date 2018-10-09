# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:09:19 2018

@author: Youssef
"""
import abc
from Node import Node
from queue import Queue, PriorityQueue
from random import shuffle

class SearchStrategy(abc.ABC):    
    # returns the next move suggested for the agent, which is the node chosen for expansion
    @abc.abstractmethod
    def form_plan(self):
        pass
    
    
    
# Stack
# Implemented by Marwan, Khatib and Youssef
class DepthFirst(SearchStrategy):
    
    
    def __init__(self, world):
        self.WORLD = world
        root = Node(-1,"Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root        
        self.ACTION_STACK = world.operators(world.INITIAL_STATE, -1)
        
    
    
    # Computes the next node & state from the current ones
    def create_node(self, ID):                
        # Action is determined from the action_stack
        next_action, parent_id = self.ACTION_STACK.pop() # (next_action, parent_id)
        old_node = self.CURRENT             
        old_state = old_node.STATE
       
        parent = old_node
        
        # This block is responsible for finding the parent of our next move by matching the ID
        # of the parent/grandparent, with the ID associated with the next action in the ACTION_Stack
        if not old_state.ALIVE: 
            parent = old_node 
            while parent.ID != parent_id:
                parent = parent.PARENT
         
        new_state = parent.STATE.get_new_state(next_action)
        if new_state.ALIVE:
            possible_operators = self.WORLD.operators(new_state, ID)
            # This will make the decisions of the dfs interesting (Less likely to be caught in infinite loops)
            shuffle(possible_operators)
            self.ACTION_STACK.extend(possible_operators) 
            
        # update the new current node
        #print(next_action,new_state.ALIVE, parent.DEPTH+1, new_state.POS_ROW, new_state.POS_COLUMN)
        self.CURRENT = Node(ID, next_action, parent, parent.DEPTH+1, new_state)
        
    
    # Calls create_node() continously until it reachs a goal node/state, then it returns the winning sequence.
    def form_plan(self):
        node_id = 0
        goal_reached = False
        while not goal_reached:
            node_id+=1
            self.create_node(node_id)
            current_state = self.CURRENT.STATE
            goal_reached = self.WORLD.goal_test(current_state) 
        
        return self.CURRENT

################################################################################################## 
    
# Queue
# Implemented by khatib
class BreadthFirst(SearchStrategy):
    
    def __init__(self, world):
        pass
    
    def create_node(self):
        pass
    
    def form_plan(self):
        pass
    # To be discussed
    
##################################################################################################    

# Stack with increasing max size
class IterativeDeepening(SearchStrategy):
    def __init__(self, world):
        pass
    
    def create_node(self):
        pass
    
    def form_plan(self):
        pass 
    # To be discussed
    

##################################################################################################


# PriorityQueue
# Implemented by Youssef
class UniformCost(SearchStrategy):
    
    def __init__(self, world):
        self.WORLD = world
        root = Node(-1,"Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root      
        possible_operators = world.operators(root.STATE, -1)
        
        # All the nodes with unexplored children
        self.PARENTS = {
                    -1:{
                        "node":root,
                        "remaining_children":len(possible_operators)
                        }
                    } 
        
        # PriorityQueue is a predefind datatype in python that takes in tuples (cost, data)
        self.ACTION_PRIO_QUEUE = PriorityQueue()
        # Initialize the PRIORITY_QUEUE by filling it with the initially available actions
        pq_entries = self.format_for_PQ(possible_operators, 0)
        for e in pq_entries:
            self.ACTION_PRIO_QUEUE.put(e)
        
    
    
    def create_node(self, ID):
        cost, data = self.ACTION_PRIO_QUEUE.get() # (cost, (action, parent_id))
        next_action, parentID = data
        
        # getting parent & computing the new_state
        parent = self.PARENTS[parentID]["node"]
        new_state = parent.STATE.get_new_state(next_action)
        
        if new_state.ALIVE:
            # Update the priority_Queue with the new node's children & costs
            possible_operators = self.WORLD.operators(new_state, ID)
            pq_entries = self.format_for_PQ(possible_operators, cost)
            for e in pq_entries:
                self.ACTION_PRIO_QUEUE.put(e)
        
        # To save memory, Decrement remaining_children & remove 
        # parent from self.PARENTS if remaining_children is now 0. (We no more need it)
        self.PARENTS[parentID]["remaining_children"]-=1
        if self.PARENTS[parentID]["remaining_children"] == 0:
            del self.PARENTS[parentID]
            
        # Update the self.CURRENT & add it as a new parent
        self.CURRENT = Node(ID, next_action, parent, parent.DEPTH+1, new_state)
        self.PARENTS[ID] = {"node":self.CURRENT,
                            "remaining_children":len(possible_operators)}
        
            
        
        
    def form_plan(self):  
        node_id = 0
        goal_reached = False
        while not goal_reached:
            node_id+=1
            self.create_node(node_id)
            current_state = self.CURRENT.STATE
            goal_reached = self.WORLD.goal_test(current_state) 
        return self.CURRENT
    


    # Concatinates the cost to each element in the given list of (action, parent_id) pairs
    def format_for_PQ(self, operators, parent_cost):
        res = []
        for o in operators:
            action = o[0]
            cost = self.WORLD.COST_DIC[action]
            res.append((cost,o))   
        return res
##################################################################################################


# ??
class Greedy(SearchStrategy):
    def __init__(self, world):
        pass
    
    def create_node(self):
        pass
        
    def heutistic_one(self):
        pass
    
    def heuristic_two(self):
        pass
    
    def form_plan(self):
        pass
    # To be discussed
    

##################################################################################################


# ??
class AStar(SearchStrategy):
    def __init__(self, world):
        pass
    
    def create_node(self):
        pass
        
    def heuristic_one(self):
        pass
    
    def heuristic_two(self):
        pass
    
    def form_plan(self):
        pass
    # To be discussed