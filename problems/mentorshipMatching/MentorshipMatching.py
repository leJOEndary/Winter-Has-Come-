from SearchProblem import GeneralSearchProblem
from Node import Node
import numpy as np
from scipy.spatial import distance

class MentorMatching(GeneralSearchProblem):
    
    def __init__(self, MentorSkills, MenteeSkills):
        self.MENTORS = list(MentorSkills.keys())
        self.MENTOR_SKILL_VECTORS = MentorSkills
        self.MENTEE_SKILL_VECTORS = MenteeSkills
        print(self.MENTORS)

    def goal_test(self, depth):
        if len(self.MENTORS) == depth:
            return True
        else:
            return False

    def path_cost(self, curr_node):
        parent_sum = curr_node.PARENT.STATE.SUM_OF_SIMILARITIES

        mentee_vec = self.MENTEE_SKILL_VECTORS[curr_node.ACTION]
        mentor_vec = self.MENTORS[curr_node.DEPTH-1]
        current_similarity = self.euclidean(mentee_vec, mentor_vec)

        return parent_sum + current_similarity


    def operators(self, state, parent_id):
        operators = []
        for mentee in list(state.REMAINING_MENTEES):
            operators.append((mentee, parent_id))
        return operators


    def parse_matches(self, node):
        c = node
        matches = []
        while c.PARENT != None:
            mentee = c.ACTION
            mentor = self.MENTORS[c.DEPTH-1]
            match = (mentee, mentor)
            matches.append(match)
            c = c.PARENT  
        matches.reverse()
        return matches

    def cosine_similarity(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        mags = np.linalg.norm(vec1) * np.linalg.norm(vec2)
        return dot_product / mags

    def euclidean(self, vec1, vec2):
        return distance.euclidean(vec1, vec2)

    def initial_state(self):
        pass
    
    def state_space(self):
        pass
