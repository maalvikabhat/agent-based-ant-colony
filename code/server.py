from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from model import AntWorld
from agent import Ant, Nest

def portrayal(agent):
    if agent is None:
        return

    # derived from sugarscape and schelling
    portrayal = {}
    if type(agent) is Ant:
        portrayal["Shape"] = "ant.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1
    # elif type(agent) is Home:
    #     portrayal["Shape"] = "circle"
    #     portrayal["r"] = math.log(1 + agent.amount)
    #     portrayal["Filled"] = "true"
    #     portrayal["Layer"] = 2
    #     portrayal["Color"] = "#00FF00BB"
    #     portrayal["text"] = agent.amount
    #     portrayal["text_color"] = "black"
    elif type(agent) is Nest:
        portrayal["Shape"] = "circle"
        portrayal["r"] = 2
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 3
        portrayal["Color"] = "#964B00BB"
        portrayal["text"] = len(agent.ants)
        portrayal["text_color"] = "white"

        # Calculate the amount of red we want
        # red = int(log_norm(agent.amount, agent.model.lowerbound, agent.model.initdrop) * 255)

        # # Scale this between red and white
        # # cite https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python
        # portrayal["Color"] = '#FF%02x%02x' % (255 - red, 255 - red)

    return portrayal

# Make a world that is 50x50, on a 500x500 display.
canvas_element = CanvasGrid(portrayal, 50, 50, 500, 500)

# derived from schelling
model_params = {
    "height": 50,
    "width": 50,
}

server = ModularServer(
    AntWorld, [canvas_element], "Ants", model_params
)
server.port = 8521 # The default
server.launch()