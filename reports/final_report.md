## Agent-Based Ant Colony's Emigration Process
#### Authors: Maalvika Bhat, Hyunkyung Rho

### Abstract
Colonies of the ant (Temnothorax Albipennis) can collectively choose the best of several nest sites, even when many of the active ants who organize the move visit only one site. Previous studies have suggested that this ability stems from the ants’ strategy of graded commitment to a potential home. On finding a site, an ant proceeds from independent assessment, to recruiting fellow active ants via slow tandem runs, to bringing the passive bulk of the colony via rapid transports. Assessment duration varies inversely with site quality, and the switch from tandem runs to transports requires that a quorum of ants first be summoned to the site. These rules may generate a collective decision, by creating and amplifying differential population growth rates among sites. We have simulated the model laid out in the original paper and tested the importance of these and other known behavioural rules by incorporating them into an agent-based model. Additionaly, we have created a visualization which demonstrates how the ants move during the emigration process.

### Experiment
We have modeled and visualized an ant colony's process of selecting a new nest after the destruction of its current nest. Every active ant that partakes in the colony emigration process is represented as a distinct agent. The decision-making of each agent is divided up into four major phases: exploration, assessment, canvassing, and commitment. In the first phase, the agent takes off to discover potential new homes. This is the exploration phase, and is referred to as such in the comments of our code. At encounter of a new potential nest, the agent alternates between staying at the site or searching areas in proximity. This is known as the second phase -- the assessment phase. At canvassing, the agent leads a tandem run from the old nest to the current nest and checks whether it is a successful run in terms of being able to bring other followers. The last phase is Commitment, when the agent returns to the old nest to transport a nestmate. 

We find that this  project is difficult to achieve in small incremental steps -- rather, a big step that would be the implementation of the entirety of the model works better. However, the additional variation and extension of the model once after completing implementation should be the ideal smaller steps we want to take. Our variation and extension is the inclusion and/or exclusion of some model parameters. 


### Results & Interpretation
Our first task was to visualize how ants' nests become populated over time. In the image below, you can see how different locations are being populated by the ants at different rates. The red line identifies the growing colony that the ant has identified as a good future home. The other locations are shown to lessen in population as the ants are emigrating.

<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/nest_population_over_time.png">

We modeled each of the four steps in the ants' emigration process -- exploration, assessment, canvassing, and commitment. In the exploration phase, the ant first looks for a nest. If a potential nest is found and accepted, the model moves to the next phase. Otherwise, we use self.random_move() to make the ant move to a nearby square. The next phase is assessment. Here, if the ant temporarily accepts the nest, then is moved to a tandem run. The tandem run is the canvassing phase but is referred to as the tandem run in our model. Every time the ant reaches the assessment phase, it chooses between staying and exploring. If the ant chooses to stay, our algorithm increases the time. If the ant chooses to explore, the algorithm makes the ant move to a nearby square. The nest phase is the tandem run phase, also known as canvassing. This is when the ant explores the potential nest with another ant. If the second ant also agrees to the new nest, then we move to the next phase: committment. If the second ant does not accept the nest, then the first ant moves back to a new square. The second ant disappears in our current model. If the second ant also accepts this new nest, the ants move into the nest. 

Finally, we created a simulation with ants moving around a square to demonstrate the emigration process visually. Below are gifs of the emigration process with different nest locations.  

Nest locations (): 
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/.png">

Nest locations (): 
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/.png">

Nest locations (): 
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/.png">

Nest locations (): 
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/.png">


### Areas of Concern
Our largest area of concern is the abundance of parameters in the project. We were aware that if we accidentally modeled a portion of the process incorrectly, our results would vary greatly. Also, missing any single parameter would change the model entirely. Nevertheless, we did our best to preserve the integrity of the model from the paper. We accomplished this by starting with the most significant parameters and translating the information presented in the graph into a precise finite state machine. Additionally, as we were translating parameters and coding, we were making sure to check each other's work to avoid missing anything. 
Another concern is that the paper itself acknowledges how the experiment fails to capture variance in colony performance. We are unsure of how this will affect our experiment and the results we hope to see. 

### Annotated Bibliography 
- An agent-based model of collective nest choice by the ant Temnothorax albipennis
http://www2.math.uu.se/~david/web/PrattSumpter05.pdf </br>
The ant Temnothorax albipennis is unique in that a group of these ants are good at collectively choosing the best nest site. When an ant finds a site, it goes through several stages of independent assessment, recruiting other ants to support its site, and bulking up the new colony via rapid transports to the site. The rules and strategy that the ants follow may results in collective decisions, despite how individual ants are responsible for assessments, by the growth rate of populations among these new sites. The authors of this paper set out to test this hypothesis with an agent-based model, where the agents abided by these rules. While the model is very complex, we hope to simulate it using a finite state machine. Additionally, we want to create a simulation of how the ants will move within the colony. 

- The ontogeny of the interaction structure in bumble bee colonies: A MIRROR model  
https://www.researchgate.net/publication/226134851_The_ontogeny_of_the_interaction_structure_in_bumble_bee_colonies_A_MIRROR_model </br>
The authors of this paper utilize a MIRROR agent-based model in order to achieve macro behavior of a beehive. The model looks at individual bee behavior by location, and from previous interactions with other bees. The model seeks to explore how beehives function and what micro behaviors could explain the beehive behavior. In addition, this model investigates the population of each individual type of bee given that each bee has a different behavior based on its role in the hive. We hope to use some of the insights from this paper in our own visualization of the ant colony.
