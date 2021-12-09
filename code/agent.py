from mesa import Agent

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
        self.accept = accept
        self.settled = False
        self.time = 0
    
    def settle(self, Ant):
        '''
        Add the Ant object that identifies this nest as its home
        '''
        self.ants.append(Ant)
    
    def native_ants(self):
        '''
        Return the number of ants that identifies this nest as its home
        '''
        return len(self.ants)

    def found(self):
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
        self.pos = nest.pos
        self.state = "Exploration"
        self.relocate = False
        self.model = model
        self.nest = nest
        self.potential_nest = None
        self.unique_id = unique_id # Q: do ants need uniqe ids?
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

    def step(self):
        # TODO: check surrounding cells for neighboring Ants where state == "committed"

        if self.state == "Exploration":
            # Look for nest
            nest = self.get_item(Nest)

            # if potential nest is found
            if nest is not None and not nest.settled:  
                nest.found()
                
                # if the nest is accepted
                if self.flip(1 - nest.reject * nest.time):
                    self.state = "Assessment"
                    self.potential_nest = nest

                # if the nest is not accepted keep searching
                else:
                    self.random_move()

            # No Home 
            else: 
                self.random_move()

        # elif self.state == "Assessment":
        #     if self.flip(1 - nest.reject * nest.time):
        #         self.state = "Tandem Run"
        #         self.potential_colony = self.model.potential_colony

        #     # every time, choose between staying / exploring
        #     if self.flip(1 - nest.stay):
        #         # do random moves & nest checking for n steps
            
        #     else:
        #         # increment time spent in the nest

        '''
        elif self.state == "Canvassing":
            # fill in
        
        elif self.state == "Committed":
            # fill in
        '''