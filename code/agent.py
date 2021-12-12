from mesa import Agent
import numpy as np
import math

# TODO: fix "AttributeError: 'NoneType' object has no attribute 'settle'"
'''
File "C:/Users/hrho/Desktop/OlinCourses/ComplexityScience/agent-based-ant-colony/code/agent.py", line 183, in step
    self.new_nest.settle(self)
AttributeError: 'NoneType' object has no attribute 'settle'


  File "C:\Users\hrho\Desktop\OlinCourses\ComplexityScience\agent-based-ant-colony\code\agent.py", line 127, in tandem_move
    self.model.grid.move_agent(self, final_candidates[0])
  File "C:\Miniconda3\lib\site-packages\mesa\space.py", line 414, in move_agent
    self._remove_agent(agent.pos, agent)
  File "C:\Miniconda3\lib\site-packages\mesa\space.py", line 560, in _remove_agent
    self.grid[x][y].remove(agent)
ValueError: list.remove(x): x not in list
'''

def get_distance(pos_1, pos_2):
    """ Get the distance between two point

    Args:
        pos_1, pos_2: Coordinate tuples for both points.

    """
    x1, y1 = pos_1
    x2, y2 = pos_2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx ** 2 + dy ** 2)

class Nest(Agent):
    def __init__(self, unique_id, pos, ants, reject, stay, accept, model):
        '''
        unique_id = calls self.next_id() on super
        model = AntWorld class object
        pos = position of the nest
        ants = number of ants that has this nest as its home
        reject = value of Ant rejecting the nest
        '''
        super().__init__(unique_id, model)

        self.pos = pos
        self.ants = ants
        self.reject = reject
        self.stay = stay
        self.quorum_met = (float)(len(self.ants)^2) / (0.000289) + (float)(len(self.ants)^2) # values taken from paper 
        self.transfer = 0.25 
        self.accept = accept
        self.settled = False
        self.time = 0
    
    def settle(self, Ant):
        '''
        Add the Ant object that identifies this nest as its home
        '''
        self.ants.append(Ant)
    
    def leave(self, Ant):
        '''
        Remove the Ant object that doesn't identify this nest as its home anymore
        '''
        self.ants.remove(Ant)
        return Ant

    def count_ants(self):
        '''
        Return the number of ants that identifies this nest as its home
        '''
        return len(self.ants)

    def increase_time(self):
        '''
        If an ant finds this nest, increment the time of the nest
        (the more time the nest is inhabited by ants, the more likely it is to be settled)
        '''
        self.time += 1

class Ant(Agent):
    def __init__(self, unique_id, nest, model, moore=True):
        '''
        nest = the nest that the ant identifies as its home
        model = the AntWorld object
        '''
        self.unique_id = unique_id 
        self.pos = nest.pos
        self.state = "Exploration"
        self.relocate = False
        self.model = model
        self.new_nest = None
        self.original_nest = nest
        self.leading_ant = None
        self.moore = moore

    def get_item(self, item):
        """
        Finds the Agent of type item at this location in the Grid
        """
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        for agent in this_cell:
            if type(agent) is item:
                return agent
    
    def flip(self, p):
        """Returns True with probability `p`."""
        return np.random.random() < p

    def random_move(self):
        """
        Step one cell in any allowable direction.
        """
        # Pick the next cell from the adjacent cells.
        next_moves = self.model.grid.get_neighborhood(self.pos, self.moore, True)
        next_move = self.random.choice(next_moves)
        # Now move:
        self.model.grid.move_agent(self, next_move)
        self.pos = next_move

    def tandem_move(self):
        """
        Step one cell toward self.new_nest.pos
        """
        # Get neighborhood within vision
        neighbors = self.model.grid.get_neighborhood(self.pos, self.moore, True)

        # Narrow down to the nearest ones to home
        min_dist = min([get_distance(self.new_nest.pos, pos) for pos in neighbors])
        final_candidates = [
            pos for pos in neighbors if get_distance(self.new_nest.pos, pos) == min_dist
        ]
        self.random.shuffle(final_candidates)

        if len(final_candidates) != 0:
            self.model.grid.move_agent(self, final_candidates[0])
            return self.pos == self.new_nest.pos
        
        else:
            self.state = "Exploration"
            self.random_move()
            return True

    def follow(self, Ant):
        '''
        Ant: ant that leads the tandem run
        '''
        # make move that moves in Ant's direction
        leading_ant = Ant.pos
        next_move = list(self.pos)
        if self.pos[0] < leading_ant[0]:
            next_move[0] += 1
        else:
            next_move[0] -= 1

        if self.pos[1] < leading_ant[1]:
            next_move[1] += 1
        else:
            next_move[1] -= 1
        
        self.model.grid.move_agent(self, tuple(next_move))

    def step(self):
        if self.state == "Exploration":
            # check nearby if there is a tandem run or committed ant
            neighbors = [n for n in self.model.grid.get_neighbors(self.pos, self.moore) if type(n) is Ant]

            # find every Ant that is in the Canvassing/Committed phase
            potential_leaders = [n for n in neighbors if self.state != "Canvassing" and self.state != "Committed" and (n.state == "Canvassing" or n.state == "Committed")]
            self.random.shuffle(potential_leaders)
            if len(potential_leaders) != 0:
                self.state = "Follow"
                self.leading_ant = potential_leaders[0]
                return 

            # Look for nest
            nest = self.get_item(Nest)

            # if potential nest is found
            if nest != self.original_nest and nest is not None and not nest.settled:  
                nest.increase_time()
                
                # if the nest is accepted
                if self.flip((1 - nest.reject) * nest.time):
                    self.state = "Assessment"
                    self.new_nest = nest

                # if the nest is not accepted keep searching
                else:
                    self.random_move()
                    return

            # No Home 
            else: 
                self.random_move()
                return

        elif self.state == "Follow":
            self.follow(self.leading_ant)
            nest = self.get_item(Nest)

            if nest != self.original_nest and nest is not None and not nest.settled:  
                self.state = "Committed"
                self.original_nest.leave(self)
                self.new_nest.settle(self)
                return

        elif self.state == "Assessment":
            ## every time, choose between staying / exploring

            # if you choose to stay, you might move to committed phase
            if self.flip(self.new_nest.stay):
                # increment time inhabited
                self.new_nest.increase_time()

                # you choose to temporarily accept this nest
                if self.flip((1 - self.new_nest.reject) * self.new_nest.time):
                    self.original_nest.leave(self)
                    self.new_nest.settle(self)

                    # you either go into committed or canvassing
                    if self.flip(self.new_nest.quorum_met):
                        self.state = "Committed"
                        return
                    else:
                        self.state = "Canvassing"
                        self.pos = self.original_nest
                        return 

            # if you choose to explore
            else: 
                self.state = "Exploration"
                self.random_move()
                return


        elif self.state == "Canvassing": 
            # conduct tandem move from original nest to new nest
            done = self.tandem_move()

            # if tandem run complete
            if done:

                # re-evaluate site
                if self.flip((1 - self.new_nest.reject) * self.new_nest.time):
                    # move to committed 
                    if self.flip(1 - self.new_nest.quorum_met):
                        self.state = "Committed"

                    # lead another tandem run
                    else:
                        self.pos = self.original_nest

                # or search nearby areas
                else: 
                    self.state = "Exploration"
                    self.random_move()
                    return
        

        elif self.state == "Committed":
            # given certain probabiity
            if self.flip(1 - self.new_nest.transfer):
                # recruit
                self.pos = self.original_nest.pos
                self.tandem_move()
     
            else: 
                # enter exploration phase
                # but the nest is the new nest this time
                self.state = "Exploration"
                self.original_nest = self.new_nest
                self.new_nest = None
                self.random_move()
