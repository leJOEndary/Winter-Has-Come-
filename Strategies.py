# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:09:19 2018

@author: Youssef
"""
import abc
from Node import Node
from queue import Queue, PriorityQueue
from random import shuffle
from State import State
from SavingWesteros import SaveWesteros

class SearchStrategy(abc.ABC):    
    # returns the next move suggested for the agent, which is the node chosen for expansion
    @abc.abstractmethod
    def form_plan(self):
        pass
    
    
    
# Stack
# Implemented by Marwan, Khatib and Youssef
class DepthFirst(SearchStrategy):
    
    
    def __init__(self, world, limit=None):
        self.WORLD = world
        root = Node(-1,"Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root        
        self.ACTION_STACK = world.operators(world.INITIAL_STATE, -1)
        self.LIMIT = limit
        
    
    
    # Computes the next node & state from the current ones
    def create_node(self, ID):                
        # Action is determined from the action_stack
        next_action, parent_id = self.ACTION_STACK.pop() # (next_action, parent_id)
        old_node = self.CURRENT             
        old_state = old_node.STATE
       
        parent = old_node
        
        # self.LIMIT is for the usability of this class with The IterativeDeepening,
        # so, we need to check that it's not none to avoid comparing Non with boolean.
        if self.LIMIT != None:
            limit_not_reached = self.LIMIT > old_node.DEPTH
        else:
            limit_not_reached = True
        # This block is responsible for finding the parent of our next move by matching the ID
        # of the parent/grandparent, with the ID associated with the next action in the ACTION_Stack
        if not old_state.ALIVE or not limit_not_reached: 
            parent = old_node 
            while parent.ID != parent_id:
                parent = parent.PARENT
         
        new_state = parent.STATE.get_new_state(next_action)
        

        if new_state.ALIVE and limit_not_reached:
            possible_operators = self.WORLD.operators(new_state, ID)
            # This will make the decisions of the dfs interesting (Less likely to be caught in infinite loops)
            shuffle(possible_operators)
            self.ACTION_STACK.extend(possible_operators) 
            
        # update the new current node
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
        self.WORLD = world
        init_state = world.INITIAL_STATE
        self.INIT_STATE = State(init_state.GRID, init_state.POS_ROW, init_state.POS_COLUMN, init_state.INVENTORY_MAX, init_state.INVENTORY_CURR)
        self.reset_df(1)                        
    
    
    def reset_df(self, depth_limit):
        self.DF = DepthFirst(self.WORLD, depth_limit)
        self.DEPTH_STACK = []
        for e in self.DF.ACTION_STACK:
            self.DEPTH_STACK.append(1) 
    
    
    def create_node(self, ID, depth_limit):
        
        current_depth = self.DEPTH_STACK.pop()
        if current_depth<=depth_limit:
            
            action_stack_len_before = len(self.DF.ACTION_STACK)
            self.DF.create_node(ID)
            action_stack_len_after = len(self.DF.ACTION_STACK)
            
            delta_stack_len = action_stack_len_after - action_stack_len_before
            new_depth = self.DF.CURRENT.DEPTH+1
            for _ in range(delta_stack_len+1):
                
                self.DEPTH_STACK.append(new_depth)        
        else:
            self.DF.ACTION_STACK.pop()
        
    
    def form_plan(self):
        depth_limit = 1
        goal_reached = False
        nodes_expanded = 0
        while not goal_reached:
            
            self.reset_df(depth_limit)
            node_id = 0
            
            while not goal_reached and len(self.DF.ACTION_STACK) > 0:
                node_id+=1
                self.create_node(node_id, depth_limit)
                current_state = self.DF.CURRENT.STATE
                goal_reached = self.WORLD.goal_test(current_state) 
            nodes_expanded += node_id
            depth_limit+=1
            
        self.DF.CURRENT.ID = nodes_expanded
        return self.DF.CURRENT
    

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