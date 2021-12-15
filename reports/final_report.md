## Agent-Based Ant Colony's Emigration Process
#### Authors: Maalvika Bhat, Hyunkyung Rho

### Abstract
Colonies of the ant (Temnothorax Albipennis) can collectively choose the best of several nest sites, even when many of the active ants who organize the move visit only one site. Previous studies have suggested that this ability stems from the ants’ strategy of graded commitment to a potential home. On finding a site, an ant proceeds from independent assessment, to recruiting fellow active ants via slow tandem runs, to bringing the passive bulk of the colony via rapid transports. Assessment duration varies inversely with site quality, and the switch from tandem runs to transports requires that a quorum of ants first be summoned to the site. These rules may generate a collective decision, by creating and amplifying differential population growth rates among sites. We have simulated the model laid out in the original paper and tested the importance of these and other known behavioural rules by incorporating them into an agent-based model. Additionaly, we have created a visualization which demonstrates how the ants move during the emigration process.

### Motivation 
Group living expands the behavioural complexity of animals, by making possible collective acts that arise from interactions among group members. These patterns emerge without central control by leaders, and each animal instead applies appropriate decision rules to purely local information! Additionally, agent-based models have seldom been usefully applied till the last few decades. Their main weakness has been the lack of adequate data to reliably estimate model parameters. The goal of our project was to understand the emigration process for ants and to understand, visually, how they choose their nests. Specifically, our extension of the project wanted to explore if the distances of the nests has any impact on which nest is most often chosen. 

### Experiment
We have modeled and visualized an ant colony's process of selecting a new nest after the destruction of its current nest. Every active ant that partakes in the colony emigration process is represented as a distinct agent. The decision-making of each agent is divided up into four major phases: exploration, assessment, canvassing, and commitment. In the first phase, the agent takes off to discover potential new homes. This is the exploration phase, and is referred to as such in the comments of our code. At encounter of a new potential nest, the agent alternates between staying at the site or searching areas in proximity. This is known as the second phase -- the assessment phase. At canvassing, the agent leads a tandem run from the old nest to the current nest and checks whether it is a successful run in terms of being able to bring other followers. The last phase is Commitment, when the agent returns to the old nest to transport a nestmate. 

Here is a diagram of the steps in our process for an easier visualization. <br /> <br />
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/Capture.PNG" width ="400" height="420"> 

### Results & Interpretation
Our first task was to visualize how ants' nests become populated over time. In the image below, you can see how different locations are being populated by ants at each timestep. At the start of the model, there are 100 ant agents that consider the "Start Nest" to be their home. As the timestep increases, we can see that the ants discover other potential nest sites through random exploration, evaluate them, and decide to settle down at new nest sites. </br>

<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/264377582_4662557863798652_8663788599411769727_n.png">

We modeled each of the four steps in the ants' emigration process -- exploration, assessment, canvassing, and commitment. In the exploration phase, the ant first looks for a nest. If a potential nest is found and accepted, the model moves to the next phase. Otherwise, we randomly make the ant move to a nearby square. The next phase is assessment. Here, if the ant temporarily accepts the nest, then it goes on a tandem run. The tandem run is the canvassing phase but is referred to as the tandem run in our model. Every time the ant reaches the assessment phase, it chooses between staying and exploring. If the ant chooses to stay, we simply increase the timestep of the model. If the ant chooses to explore, the ant moves to a nearby neighboring cell randomly. The nest phase is the tandem run phase, also known as canvassing. This is when the ant attempts to lead an exploration from its old nest to its new nest by leading other ants. If the ant leading the tandem run successfully reaches the new nest, its followers also become part of the new nest. Now from canvassing, ants may decide to commit to this new nest and which the probability of this committment is dependent on the nest's quality and the time it has been inhabited for. Once committed, ants may lead random tandem runs or explorations that start from its new nest.

Below are simulations of the emigration process with different nest locations. You can see that the potential nests closest to the original nest are the most frequented and the most likely to become the new nests. Even after we did a screen wrap, this still seems to be the case.

Additionally, for the sake of visualization, the black ants are ants which are exploring, assessing, or committing. The light-blue ants are ants on tandem runs. The dark-blue ants are follower ants of tandem runs.

The simulation below shows how, when the original nest is in a central location, the closest nest will be the most frequently visited. Therefore, it is most likely to become the chosen new nest. <br /> <br />
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/gif_1.gif" width="1000" height="500"> <br />

This simulation shows how frequent the closest nest is visited. The second most frequently visited is the furthest nest, but with screen wrap, it is the second closest. <br /> <br />
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/gif_3.gif" width="1000" height="500"> <br />

All the potential nests in this visualization are rather far from the original nest, so the model times out before the ants are able to choose a new nest. Still, the ants get to the closest two nests the fastest. <br /> <br />
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/gif_4.gif" width="1000" height="500"> <br />

The simulation below highlights how the nest which is the closest and easiest to access will have the most ants frequent the location. <br /> <br />
<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/pictures/gif_2.gif" width="1000" height="500"> <br />

### Limitation of the Model
One key limitation of the model is that an ant that has successfully led a tandem run cannot lead another tandem run or go on an exploration immediately. Tandem runs happen in a manner such that the follower ants move into cells that are closer to where the leading ant was placed in the previous timestep. This means that once a leading ant reaches the new nest site, it takes several extra timesteps for the follower ants to reach the new nest site as well (and the extra timesteps are dependent on how many follower ants there are). To ensure that all the follower ants can settle in for a successful tandem run, we impose this restriction that leading ants of a tandem run must rest in their new nest sites for *x* timesteps, with *x* being a variable that can be altered in our model.

### Areas of Concern
Our largest area of concern is the abundance of parameters in the project. We were aware that if we accidentally modeled a portion of the process incorrectly, our results would vary greatly. Also, missing any single parameter would change the model entirely. Nevertheless, we did our best to preserve the integrity of the model from the paper. We accomplished this by starting with the most significant parameters and translating the information presented in the graph into a precise finite state machine. Additionally, as we were translating parameters and coding, we were making sure to check each other's work to avoid missing anything. 
Another concern is that the paper itself acknowledges how the experiment fails to capture variance in colony performance. 

### Annotated Bibliography 
- An agent-based model of collective nest choice by the ant Temnothorax albipennis
http://www2.math.uu.se/~david/web/PrattSumpter05.pdf </br>
The ant Temnothorax albipennis is unique in that a group of these ants are good at collectively choosing the best nest site. When an ant finds a site, it goes through several stages of independent assessment, recruiting other ants to support its site, and bulking up the new colony via rapid transports to the site. The rules and strategy that the ants follow may results in collective decisions, despite how individual ants are responsible for assessments, by the growth rate of populations among these new sites. The authors of this paper set out to test this hypothesis with an agent-based model, where the agents abided by these rules. While the model is very complex, we hope to simulate it using a finite state machine. Additionally, we want to create a simulation of how the ants will move within the colony. 

- The ontogeny of the interaction structure in bumble bee colonies: A MIRROR model  
https://www.researchgate.net/publication/226134851_The_ontogeny_of_the_interaction_structure_in_bumble_bee_colonies_A_MIRROR_model </br>
The authors of this paper utilize a MIRROR agent-based model in order to achieve macro behavior of a beehive. The model looks at individual bee behavior by location, and from previous interactions with other bees. The model seeks to explore how beehives function and what micro behaviors could explain the beehive behavior. In addition, this model investigates the population of each individual type of bee given that each bee has a different behavior based on its role in the hive. We hope to use some of the insights from this paper in our own visualization of the ant colony.

### To expand further
To expand further, we want to explore the process of selecting new potential nest sites when there are more than one (ideally two) species of ants represented in the model. We believe that incorporating behaviors such as fights between ants of different colonies would result in very interesting results out of the model. Another area we wish to experiment with is the behavior of the ants when a phase of the emigration process is eliminated. For example, to see how the process changes without the tandem run portion of the canvassing phase. The process would most likely be faster, but it would be fascinating the compare how else the two models would act and other differences we could potentially perceive. 
