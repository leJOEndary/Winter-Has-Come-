# Winter-Has-Come-
A project applying multiple search algorithms to make an AI Agent that can make decisions with various wisdom levels in a mini game.

## Project Description
More than eight thousand years ago, the longest winter in history fell on the continent
of Westeros. During this dark time, humanoid ice creatures known as the white walkers
swept through Westeros riding on their dead horses and hunting everything living.
Eventually, the people of Westeros rallied against the white walkers and forced them
to the north. A great wall was built to bar the return of the white walkers ever again.
The wall stood tall for thousands of years protecting all living things until the white
walkers finally succeeded in bringing it down. Now a long and deadly winter has come
to Westeros once again.
As a last strive for survival, the King in the North Jon Snow gathered all remaining
magic in Westeros to freeze the white walkers in their places in a big field right after
they crossed the fallen wall. The white walkers must be exterminated before they find
a way to unfreeze bringing unstoppable doom to Westeros. In order not to provoke the
white walkers causing them to break free, only Jon Snow must enter the field where they
are frozen in place to kill them. White walkers can be killed by stabbing them with a
form of volcanic glass commonly known as dragonglass which can be obtained from a
special stone called the dragonstone.
In this project, you will use search to help Jon Snow save Westeros. The field where
the white walkers are frozen in place can be thought of as an m × n grid of cells where
m, n ≥ 4 . A grid cell is either free or contains one of the following: a white walker,
Jon Snow, the dragonstone, or an obstacle. Jon Snow can move in the four directions
as long as the cell in the direction of movement does not contain an obstacle or a living
white walker. To obtain the dragonglass by which the white walkers can be killed, Jon
has to go to the cell where the dragonstone lies to pick up a fixed number of pieces
of dragonglass that he can carry. In order to kill a white walker, Jon has to be in an
adjacent cell. An adjacent cell is a cell that lies one step to the north, south, east, or west.
With a single move using the same piece of dragonglass, Jon can kill all adjacent white
walkers. If Jon steps out of a cell where he used a piece of dragonglass to kill adjacent
walkers, that piece of dragonglass becomes unusable. Once a white walker is killed, Jon
can move through the cell where the walker was. If Jon runs out of dragonglass before
all the white walkers are killed, he has to go back to the dragonstone to pick up more
pieces of dragonglass. Using search you should formulate a plan that Jon can follow to
kill all the white walkers. An optimal plan is one where Jon uses the least number of
pieces of dragonglass to kill all the white walkers.


## Wisdom-Levels / Agent-Strategies that will move Jon
a) Breadth-first search.
b) Depth-first search.
c) Iterative deepening search.
d) Uniform-cost search.
e) Greedy with two heuristics.
f) A∗ search with two admissible heuristics.

