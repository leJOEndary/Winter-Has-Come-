import numpy as np
from scipy.spatial import distance

class Heuristics():
    def __init__(self, Mode, world):
        self.MODE = Mode
        self.WORLD = world

    def heuristic(self, action, parent_node):
        if self.MODE == "similarity_avrg":
            print("cosine")
            return self.heuristic_similarity_avrg_remaining(action, parent_node)
        elif self.MODE == "euclidean_avg_dist":
            print("euclidean")
            return self.heuristic_similarity_avrg_remaining(action, parent_node)


    def get_mentees_mentors_avg(self, mentee, parent_node):
        depth = parent_node.DEPTH
        state = parent_node.STATE

        remaining_mentees = state.REMAINING_MENTEES
        
        mentee_vecs = []
        for ment in remaining_mentees:
            if ment != mentee:
                mentee_vecs.append(self.WORLD.MENTEE_SKILL_VECTORS[ment])

        #print("This is remaining mentees", mentee_vecs)
        #remaining_mentors = [mentor for i,mentor in enumerate(self.WORLD.MENTORS) if depth-1 < i]
        mentor_vecs = []
        for i,mentor in enumerate(self.WORLD.MENTORS):
            if depth < i:
                mentor_vecs.append(self.WORLD.MENTOR_SKILL_VECTORS[mentor])
        #print("This is remaining mentors", mentor_vecs)


        mentee_avg_vec = np.average(np.array(mentee_vecs), axis=0)
        mentor_avg_vec = np.average(np.array(mentor_vecs), axis=0)

        return mentee_avg_vec, mentor_avg_vec

    def heuristic_similarity_avrg_remaining(self, mentee, parent_node):
        
        mentee_avg_vec, mentor_avg_vec = self.get_mentees_mentors_avg( mentee, parent_node)
        return self.WORLD.cosine_similarity(mentee_avg_vec, mentor_avg_vec)


    def heuristic_euclidean_dist(self, mentee, parent_node):
        mentee_avg_vec, mentor_avg_vec = self.get_mentees_mentors_avg( mentee, parent_node)
        return distance.euclidean(mentee_avg_vec, mentor_avg_vec)
