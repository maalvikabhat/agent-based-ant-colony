from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from agent import Ant, Nest

class AntWorld(Model):
    def __init__(self, height=100, width=100):
        super().__init__()

        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = SimultaneousActivation(self)

        # Use a simple grid, where edges wrap around.
        self.grid = MultiGrid(height, width, torus=True)
        
        # Define pos for the initial nest(home) 
        nestloc = (25, 25)
        nest_locs = ((22, 11), (35, 8), (18, 33)) # define nest locations

        self.startnest = Nest(self.next_id(), nestloc, [], 0.2, 0.7, 0.7, self)
        self.nests = [self.startnest]
        self.grid.place_agent(self.startnest, nestloc)
        self.schedule.add(self.startnest)

        # Add in the ants
        # Need to do this first, or it won't affect the cells, consequence of SimultaneousActivation
        for i in range(100):
            ant = Ant(self.next_id(), self.startnest, self)
            self.startnest.ants.append(ant)
            self.grid.place_agent(ant, self.startnest.pos)
            self.schedule.add(ant)

        # Add the other nest locations
        for loc in nest_locs:
            nest = Nest(self.next_id(), loc, [], 0.5, 0.5, 0.5, self) # TODO: replace this with randomizing the nest param values
            self.nests.append(nest)
            self.grid.place_agent(nest, loc)
            self.schedule.add(nest)

        self.running = True
        
        # Recording of the data
        # self.dc = DataCollector({"start_nest": lambda m: len(self.nests[0].ants),
        #                 "Nest 1": lambda m: len(self.nests[1].ants),
        #                 "Nest 2": lambda m: len(self.nests[2].ants),
        #                 "Nest 3": lambda m: len(self.nests[3].ants)
        #                 })
    
    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.schedule.step()
        # self.dc.collect(self)


        # TODO: stop when all the nests are visited
        if self.schedule.time > 100:
            self.running = False
