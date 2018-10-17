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
from Heuristics import Heuristics


class SearchStrategy(abc.ABC):
    # returns the next move suggested for the agent, which is the node chosen for expansion
    @abc.abstractmethod
    def create_node(self, ID):
        pass
    
    @abc.abstractmethod
    def form_plan(self):
        pass

      
      
# Stack
class DepthFirst(SearchStrategy):

    def __init__(self, world, limit=None, random=True):
        self.WORLD = world
        root = Node(-1,"Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root
        self.ACTION_STACK = world.operators(world.INITIAL_STATE, -1)
        self.LIMIT = limit
        self.RANDOM = random



    # Computes the next node & state from the current ones
    def create_node(self, ID):
        # Action is determined from the action_stack
        next_action, parent_id = self.ACTION_STACK.pop() # (next_action, parent_id)
        parent = self.CURRENT

        # self.LIMIT is for the usability of this class with The IterativeDeepening,
        # so, we need to check that it's not none to avoid comparing Non with boolean.
        if self.LIMIT != None:
            limit_not_reached = self.LIMIT > parent.DEPTH
        else:
            limit_not_reached = True

        # This block is responsible for finding the parent of our next move by matching the ID
        # of the parent/grandparent, with the ID associated with the next action in the ACTION_Stack
        if not limit_not_reached: 
            while parent.ID != parent_id:
                parent = parent.PARENT
        new_state = parent.STATE.get_new_state(next_action)
        if limit_not_reached:
            possible_operators = self.WORLD.operators(new_state, ID)

            # This will make the decisions of the dfs interestingly random (Less likely to be caught in infinite loops)
            if self.RANDOM:
                shuffle(possible_operators)
            self.ACTION_STACK.extend(possible_operators)

        # update the new current node
        self.CURRENT = Node(ID, next_action, parent, parent.DEPTH+1, new_state)

    
    

    # Calls create_node() continously until it reachs a goal node/state, then it returns the winning sequence.
    def form_plan(self):
        node_id = 0
        goal_reached = False
        while not goal_reached:
            if len(self.ACTION_STACK) == 0:
                return None
            self.create_node(node_id)
            current_state = self.CURRENT.STATE
            if self.CURRENT.ACTION == "Attack":  
                goal_reached = self.WORLD.goal_test(current_state) 
            node_id+=1 
        return self.CURRENT
    



##################################################################################################

class BreadthFirst(SearchStrategy):

      def __init__(self, world):
          self.WORLD = world
          root = Node(-1, "Initial", None, 0, world.INITIAL_STATE)
          self.ROOT = root
          self.CURRENT = root
          self.ACTION_QUEUE = Queue()
          possible_operators = world.operators(world.INITIAL_STATE, -1)
          
          # All the nodes with unexplored children
          self.PARENTS = {
              -1: {
                  "node": root,
                  "remaining_children": len(possible_operators)
              }
          }
          # queuing possible operator(actions) of the intial state
          for operator in possible_operators:
              self.ACTION_QUEUE.put(operator)



      def create_node(self, ID):
          # DEQUEUE the next action
          next_action, parent_id = self.ACTION_QUEUE.get()  # (next_action, parent_id)

          parent = self.PARENTS[parent_id]["node"]

          # Expand the state(node) and get the new list of possible operators of the next level
          new_state = parent.STATE.get_new_state(next_action)
         
          new_possible_operators_toQueue = self.WORLD.operators(new_state, ID)  # List of the form (action, id)
          # Queue the new possible operators
          for operator in new_possible_operators_toQueue:
              self.ACTION_QUEUE.put(operator)

          # To save memory, Decrement remaining_children & remove
          # parent from self.PARENTS when remaining_children reaches 0. (We no more need it)
          self.PARENTS[parent_id]["remaining_children"] -= 1
          if self.PARENTS[parent_id]["remaining_children"] == 0:
              del self.PARENTS[parent_id]

          # Update the self.CURRENT & add it as a new parent
          self.CURRENT = Node(ID, next_action, parent, parent.DEPTH + 1, new_state)
          if len(new_possible_operators_toQueue) > 0:
              self.PARENTS[ID] = {"node": self.CURRENT,
                                  "remaining_children": len(new_possible_operators_toQueue)}



      def form_plan(self):
          node_id = 0
          goal_reached = False
          while not goal_reached:
              if self.ACTION_QUEUE.empty():
                return None
              self.create_node(node_id)
              current_state = self.CURRENT.STATE
              goal_reached = self.WORLD.goal_test(current_state)
              node_id += 1
          return self.CURRENT


##################################################################################################


# DepthFirst() With increasing limit
# Utilizes our DepthFirst implementation in order to avoid redundunt code
class IterativeDeepening(SearchStrategy):
    def __init__(self, world):
        self.WORLD = world
        init_state = world.INITIAL_STATE
        self.INIT_STATE = State(init_state.GRID, init_state.POS_ROW, init_state.POS_COLUMN,
                                init_state.INVENTORY_MAX, init_state.INVENTORY_CURR)
        self.reset_df(1)                        
    
        
        
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

                if self.DF.CURRENT.ACTION == "Attack":
                    goal_reached = self.WORLD.goal_test(current_state) 
            nodes_expanded += node_id
            depth_limit+=1
        self.DF.CURRENT.ID = nodes_expanded
        return self.DF.CURRENT

    
           
                ##############################
                        # Helpers #
                ##############################   
    
    
    
    # Resets the DepthFirst Instance with a new limit
    def reset_df(self, depth_limit):
        self.DF = DepthFirst(self.WORLD, depth_limit)
        self.DEPTH_STACK = []
        for e in self.DF.ACTION_STACK:
            self.DEPTH_STACK.append(1) 
    
    
##################################################################################################

# Need Optimizations if possible
# PriorityQueue
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
    
        # Update the priority_Queue with the new node's children & costs
        possible_operators = self.WORLD.operators(new_state, ID)
        pq_entries = self.format_for_PQ(possible_operators, cost) # format it to (cost, (action, parent_id))
        for e in pq_entries:
            self.ACTION_PRIO_QUEUE.put(e)
                    
        # To save memory, Decrement remaining_children & remove 
        # parent from self.PARENTS when remaining_children reaches 0. (We no more need it)
        self.PARENTS[parentID]["remaining_children"]-=1
        if self.PARENTS[parentID]["remaining_children"] == 0:
            del self.PARENTS[parentID]
            
        # Update the self.CURRENT & add it as a new parent
        self.CURRENT = Node(ID, next_action, parent, parent.DEPTH+1, new_state)
        if len(possible_operators)>0:
            self.PARENTS[ID] = {"node":self.CURRENT,
                                "remaining_children":len(possible_operators)}        
                
        
        
    def form_plan(self):  
        node_id = 0
        goal_reached = False
        while not goal_reached:
            if self.ACTION_PRIO_QUEUE.empty():
                return None
            self.create_node(node_id)
            current_state = self.CURRENT.STATE
            if self.CURRENT.ACTION == "Attack":    
                goal_reached = self.WORLD.goal_test(current_state)
            node_id+=1      
        return self.CURRENT
    
    
                        ###############################
                                # Helpers #
                        ###############################
                        
                        

    # Concatinates the cost to each element in the given list of (action, parent_id) pairs
    def format_for_PQ(self, operators, parent_cost):
        res = []
        for o in operators:
            action = o[0]
            cost = self.WORLD.COST_DIC[action] + parent_cost
            res.append((cost,o))
        return res
    
    
##################################################################################################


# Doesn't look back
class Greedy(SearchStrategy):

    
    def __init__(self, world, heuristic_mode="2"):     
        self.WORLD = world
        root = Node(-1,"Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root
        self.HEURISTICS = Heuristics(heuristic_mode)
        self.ACTION_STACK = []     
        possible_operators = world.operators(root.STATE, -1) 
        stack_entries = self.format_for_Stack(possible_operators, self.CURRENT.STATE)      
        self.ACTION_STACK.extend(stack_entries)
    
    
    
    def create_node(self,ID):           
        next_action, parentID = self.ACTION_STACK.pop()   
        
        # This block is responsible for finding the parent of our next move by matching the ID
        # of the parent/grandparent, with the ID associated with the next action in the ACTION_Stack
        parent = self.CURRENT
        while parent.ID != parentID:
            parent = parent.PARENT              
        current_state = parent.STATE   
        new_state = current_state.get_new_state(next_action)        
        possible_operators = self.WORLD.operators(new_state, ID)
        stack_entries = self.format_for_Stack(possible_operators,current_state)  
        self.ACTION_STACK.append(stack_entries[0])
        self.CURRENT = Node(ID, next_action, parent, parent.DEPTH+1, new_state)
        
      
    
    
    def form_plan(self):
        node_id = 0
        goal_reached = False
        while not goal_reached:     
            if len(self.ACTION_STACK)==0:
                return None
            self.create_node(node_id)
            current_state = self.CURRENT.STATE
            if self.CURRENT.ACTION == "Attack":  
                goal_reached = self.WORLD.goal_test(current_state)        
            node_id+=1   
        
        return self.CURRENT
    
    
                ##################################
                        # Helpers #
                ################################
        
        
    def format_for_Stack(self,possible_operators,state):
        new_operators=PriorityQueue()
        for operator in possible_operators :
            action=operator[0]       
            h_value = self.HEURISTICS.heuristic(action, state)      
            new_operator=(h_value,operator)
            new_operators.put(new_operator)  
            
        result = []
        for o in new_operators.queue:
            result.append(o[1])        
        return result


##################################################################################################


# PrioQueue
class AStar(SearchStrategy):
    def __init__(self, world, heuristic_mode="2"):
        self.WORLD = world
        root = Node(-1,"Initial", None, 0, world.INITIAL_STATE)
        self.ROOT = root
        self.CURRENT = root
        self.CURR_COST = 1
        self.HEURISTICS = Heuristics(heuristic_mode)
        
        # Should contain format (h+c , (action, parentID))
        self.ACTION_PRIO_QUEUE = PriorityQueue()
        
        # returns format (action, parentID)
        possible_operators = world.operators(root.STATE, -1)
        
        # All the nodes with unexplored children
        self.PARENTS = {
                    -1:{
                        "node":root,
                        "remaining_children":len(possible_operators),
                        "cost":0
                        }
                    }
        # Initialize the PRIORITY_QUEUE by filling it with the initially available actions
        pq_entries = self.format_for_PQ(possible_operators, self.CURRENT,0)
        for e in pq_entries:
            self.ACTION_PRIO_QUEUE.put(e)




    def create_node(self,ID):
        f_value, data = self.ACTION_PRIO_QUEUE.get()
        next_action, parentID = data
        parent = self.PARENTS[parentID]["node"]
        parent_cost = self.PARENTS[parentID]["cost"]
        new_state = parent.STATE.get_new_state(next_action)
        
        # Update the priority_Queue with the new node's children & costs + heuristics
        possible_operators = self.WORLD.operators(new_state, ID)
        pq_entries = self.format_for_PQ(possible_operators, parent, parent_cost) # format it to (c+h, (action, parent_id))  
        for e in pq_entries:
            self.ACTION_PRIO_QUEUE.put(e) 
                
        # To save memory, Decrement remaining_children & remove 
        # parent from self.PARENTS when remaining_children reaches 0. (We no more need it)
        self.PARENTS[parentID]["remaining_children"]-=1
        if self.PARENTS[parentID]["remaining_children"] == 0:
            del self.PARENTS[parentID]
        
        # Update the self.CURRENT & add it as a new parent
        self.CURRENT = Node(ID, next_action, parent, parent.DEPTH+1, new_state)
        if len(possible_operators)>0:
            self.PARENTS[ID] = {"node":self.CURRENT,
                                "remaining_children":len(possible_operators),
                                "cost":self.CURR_COST}




    def format_for_PQ(self,possible_operators, parent, parent_cost):
        state = parent.STATE
        new_operators=[]
        for operator in possible_operators :
            action=operator[0]         
            h_value = self.HEURISTICS.heuristic(action, state)                
            self.CURR_COST = parent_cost + self.WORLD.COST_DIC[action]
            f_value = h_value + self.CURR_COST                    
            new_operator=(f_value,operator)
            new_operators.append(new_operator)

        return new_operators




    def form_plan(self):
        node_id = 0
        goal_reached = False
        while not goal_reached:
            if self.ACTION_PRIO_QUEUE.empty():
                return None
            self.create_node(node_id)
            current_state = self.CURRENT.STATE
            if self.CURRENT.ACTION == "Attack":
                goal_reached = self.WORLD.goal_test(current_state)        
            node_id+=1           
        return self.CURRENT
