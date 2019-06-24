#import pandas as pd
import numpy as np
from MentorshipMatching import MentorMatching
from Strategies import AStar
from State import State

Skills = {
    "Web development":np.array(),
    "Web Design": np.array([4,2,0,2]),
    "Database Design": np.array([0,4,0,5]),
    "Database managment": np.array([0, 2,1 , 3]),
    "Software Engineering": np.array([1, 2, 1, 3 ]),
    "Datascience": np.array([0, 5, 1, 4]),
    "Data Analaysis": np.array([2,3,1,0]),
    "Machine Learning": np.array([0, 0, 4, 3]),
    "AI": np.array([0,4,5,0]),
    "Reinforcement Learing": np.array([0, 2, 4, 0]),
    "Computer Vision": np.array([1,1,1,0]),
    "OOP": np.array([0,4,5,0]),
    "Microservices": np.array([0,2,0,5]),
    "UX Design": np.array([4, 2, 1, 2])
}

Mentees = {
    # "Hamada":["Datascience", "Database Design", "OOP"],
    # "Ahmed":["Web development", "Web Design"],
    # "Henna":["Machine Learning", "Reinforcement Learing", "AI", "Computer Vision"]
    "Hamada":Skills["AI"],
    "Ahmed":Skills["Database Design"],
    "Henna":Skills["UX Design"]
}
Mentors = {
    "Youssef":Skills["OOP"],
    "Yasser":Skills["Datascience"],
    "Nada":Skills["Web Design"]
}


World = MentorMatching(Mentors, Mentees)
init_state = State(0, list(Mentees.keys()), World)
Engine = AStar(World, init_state)
final_node = Engine.form_plan()
print(World.parse_matches(final_node))