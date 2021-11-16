
# Visualizing an Agent-Based Model of Collective Nest Choice by the Ant 
#### Maalvika Bhat, Hyunkyung Rho

### Abstract
Colonies of the ant (Temnothorax Albipennis) can collectively choose the best of several nest sites, even when many of the active ants who organize the move visit only one site. Previous studies have suggested that this ability stems from the ants’ strategy of graded commitment to a potential home. On finding a site, an ant proceeds from independent assessment, to recruiting fellow active ants via slow tandem runs, to bringing the passive bulk of the colony via rapid transports. Assessment duration varies inversely with site quality, and the switch from tandem runs to transports requires that a quorum of ants first be summoned to the site. These rules may generate a collective decision, by creating and amplifying differential population growth rates among sites. We plan to simulate the model laid out in the paper and test the importance of these and other known behavioural rules by incorporating them into an agent-based model. Additionaly, our goal is to create a visualization which demonstrates how the ants move during the emigration process. 

### Areas of Concern
Our largest area of concern is the scope of the project. With the abundance of parameters presented in the original paper, we are concerned we will accidentally model a portion of the process incorrectly which would cause our results to vary greatly. Also, missing any single parameter would change the model entirely. Nevertheless, we hope to preserve the integrity of the model from the paper. We will accomplish this by accurately capturing each parameter and translating the information presented in the graph into a precise finite state machine. To check, we want to see the results we produce aligning up with the graphs presented in the paper. 

### Annotated Bibliography 

- An agent-based model of collective nest choice by the ant Temnothorax albipennis
http://www2.math.uu.se/~david/web/PrattSumpter05.pdf
The ant Temnothorax albipennis is unique in that a group of these ants are good at collectively choosing the best nest site. When an ant finds a site, it goes through several stages of independent assessment, recruiting other ants to support its site, and bulking up the new colony via rapid transports to the site. The rules and strategy that the ants follow may results in collective decisions, despite how individual ants are responsible for assessments, by the growth rate of populations among these new sites. The authors of this paper set out to test this hypothesis with an agent-based model, where the agents abided by these rules. While the model is very complex, we hope to simulate it using a finite state machine. Additionally, we want to create a simulation of how the ants will move within the colony. 

- The ontogeny of the interaction structure in bumble bee colonies: A MIRROR model  
https://www.researchgate.net/publication/226134851_The_ontogeny_of_the_interaction_structure_in_bumble_bee_colonies_A_MIRROR_model
The authors of this paper utilize a MIRROR agent-based model in order to achieve macro behavior of a beehive. The model looks at individual bee behavior by location, and from previous interactions with other bees. The model seeks to explore how beehives function and what micro behaviors could explain the beehive behavior. In addition, this model investigates the population of each individual type of bee given that each bee has a different behavior based on its role in the hive. We hope to use some of the insights from this paper in our own visualization of the ant colony.
 
### Experiment Plan


#### This might look like the following: 

We will create a similar graph of estimates of the mean and standard deviation of recruitment time, the duration of a round-trip recruitment journey, as a function of the
number of recruitment journeys so far undertaken. This will help us ensure we are on the correct track and translating the parameters accurately.

![image](https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/normalizednest.PNG)

Next, we will plot the probability of a recruiter performing a transport rather than a tandem run, as a function of the number of workers at the new site on her immediately previous visit there. The worker numbers are normalized by dividing by total colony population. 

![image](https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/recnumber.PNG)

We will create a plot that identifies the different stages the ants are at with different symbols and a legend. It should look something like this.

<img src="https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/253176697_2983341461929021_3787379295825093977_n.jpg" width="400" height="550">

Finally, we will create a simulation with ants moving around a square to demonstrate the emigration process visually. 

![image](https://github.com/maalvikabhat/agent-based-ant-colony/blob/main/256168034_956707494925267_2335244230622024383_n.jpg)


### Next Steps
Plus, we have a task board up and running under the *Projects* bar in this repository!
