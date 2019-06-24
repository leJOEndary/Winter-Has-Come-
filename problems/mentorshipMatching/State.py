
class State():

    # State Constructor
    def __init__(self, sumOfSimilarities, remainingMentees, world):
        self.SUM_OF_SIMILARITIES = sumOfSimilarities
        self.REMAINING_MENTEES = remainingMentees
        self.WORLD = world


    def get_new_state(self, mentee, depth):
        parent_sum = self.SUM_OF_SIMILARITIES
        mentee_vec = self.WORLD.MENTEE_SKILL_VECTORS[mentee]

        mentor = self.WORLD.MENTORS[depth-1]
        mentor_vec = self.WORLD.MENTOR_SKILL_VECTORS[mentor]

        current_similarity = self.WORLD.euclidean(mentee_vec, mentor_vec)
        total_similarity = parent_sum + current_similarity
        #new_remainingMentees = self.REMAINING_MENTEES.copy(
        new_remainingMentees = []
        for i in self.REMAINING_MENTEES:
            if i != mentee:
                new_remainingMentees.append(i)
        print(new_remainingMentees)        
        
        return State(total_similarity, new_remainingMentees, self.WORLD)