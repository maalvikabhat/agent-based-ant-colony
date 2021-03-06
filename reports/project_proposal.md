
# Visualizing an Agent-Based Model of Collective Nest Choice by the Ant 
#### Maalvika Bhat, Hyunkyung Rho

### Abstract
Colonies of the ant (Temnothorax Albipennis) can collectively choose the best of several nest sites, even when many of the active ants who organize the move visit only one site. Previous studies have suggested that this ability stems from the ants’ strategy of graded commitment to a potential home. On finding a site, an ant proceeds from independent assessment, to recruiting fellow active ants via slow tandem runs, to bringing the passive bulk of the colony via rapid transports. Assessment duration varies inversely with site quality, and the switch from tandem runs to transports requires that a quorum of ants first be summoned to the site. These rules may generate a collective decision, by creating and amplifying differential population growth rates among sites. We plan to simulate the model laid out in the paper and test the importance of these and other known behavioural rules by incorporating them into an agent-based model. Additionaly, our goal is to create a visualization which demonstrates how the ants move during the emigration process. 

### Areas of Concern
Our largest area of concern is the scope of the project. With the abundance of parameters presented in the original paper, we are concerned we will accidentally model a portion of the process incorrectly which would cause our results to vary greatly. Also, missing any single parameter would change the model entirely. Nevertheless, we hope to preserve the integrity of the model from the paper. We will accomplish this by starting with the most significant parameters and translating the information presented in the graph into a precise finite state machine. To check, we want to see the results we produce aligning up with the graphs presented in the paper. 

### Annotated Bibliography 

- An agent-based model of collective nest choice by the ant Temnothorax albipennis
http://www2.math.uu.se/~david/web/PrattSumpter05.pdf </br>
The ant Temnothorax albipennis is unique in that a group of these ants are good at collectively choosing the best nest site. When an ant finds a site, it goes through several stages of independent assessment, recruiting other ants to support its site, and bulking up the new colony via rapid transports to the site. The rules and strategy that the ants follow may results in collective decisions, despite how individual ants are responsible for assessments, by the growth rate of populations among these new sites. The authors of this paper set out to test this hypothesis with an agent-based model, where the agents abided by these rules. While the model is very complex, we hope to simulate it using a finite state machine. Additionally, we want to create a simulation of how the ants will move within the colony. 

- The ontogeny of the interaction structure in bumble bee colonies: A MIRROR model  
https://www.researchgate.net/publication/226134851_The_ontogeny_of_the_interaction_structure_in_bumble_bee_colonies_A_MIRROR_model </br>
The authors of this paper utilize a MIRROR agent-based model in order to achieve macro behavior of a beehive. The model looks at individual bee behavior by location, and from previous interactions with other bees. The model seeks to explore how beehives function and what micro behaviors could explain the beehive behavior. In addition, this model investigates the population of each individual type of bee given that each bee has a different behavior based on its role in the hive. We hope to use some of the insights from this paper in our own visualization of the ant colony.
 
### Experiment Plan
We will model and visualize an ant colony's process of selecting a new nest after the destruction of its current nest. Every active ant that partakes in the colony emigration process is represented as a distinct agent. The decision-making of each agent is divided up into four major phases: exploration, assessment, canvassing and committed. In the first phase, the agent takes off to discover potential new homes. At encounter of a new potential nest, the agent alternates between staying at the site or searching areas in proximity. At canvassing, the agent leads a tandem run from the old nest to the current nest and checks whether it is a successful run in terms of being able to bring other followers. The last committed phase is when the agent returns to the old nest to transport a nestmate. The many states of this model all fall under the aforementioned four major categories and their diagram are shown below. 

<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/ant_states.png" width="400" height="550">

We find that the project is difficult to achieve in small incremental steps--rather, a big step that would be the implementation of the entirety of the model. However, the additional variation and extension of the model once after completing implementation should be the ideal smaller steps we want to take. There are two areas of variation and extension that we are considering: the inclusion and/or exclusion of some model parameters and the introduction of new environmental events such as blockades in the path. 

#### This might look like the following: 

We will create a similar graph of estimates of the mean and standard deviation of recruitment time, the duration of a round-trip recruitment journey, as a function of the
number of recruitment journeys so far undertaken. This will help us ensure we are on the correct track and translating the parameters accurately.

![image](https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/normalizednest.PNG)

Next, we will plot the probability of a recruiter performing a transport rather than a tandem run, as a function of the number of workers at the new site on her immediately previous visit there. The worker numbers are normalized by dividing by total colony population. 

![image](https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/recnumber.PNG)

We will create a plot that identifies the different stages the ants are at with different symbols and a legend. It should look something like this.

<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/ant_colony_over_time.jpg" width="400" height="550">

Finally, we will create a simulation with ants moving around a square to demonstrate the emigration process visually. 

<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/ant_simulation.jpg" width="400" height="550">

#### Related Implementations By Others
- **A port of the ants simulation to Mesa agent-based modeling framework in Python** </br>
https://github.com/mgoadric/ants-mesa
- **Building An Agent-Based Model with Python for Ant-Foraging** </br>
https://medium.com/mlearning-ai/building-an-agent-based-model-with-python-streamlit-for-ant-foraging-a74a41605d2c

### Next Steps
Before next class, both team members mainly have three tasks to work on: digesting the papers mentioned in the bibliography, understanding the approaches taken in other's implementations, and learning the pattern behind nondeterministic finite state machine implementations. Once this is done, we will go about deciding on which approach to take for model implementation: code-centered, data-centered, or both. Plus, we have a task board up and running under the *Projects* bar in this repository!
