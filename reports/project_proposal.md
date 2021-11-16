
# Visualizing an Agent-Based Model of Collective Nest Choice by the Ant 
#### Maalvika Bhat, Hyunkyung Rho

### Abstract

### Areas of Concern

### Annotated Bibliography 

- An agent-based model of collective nest choice by the ant Temnothorax albipennis
http://www2.math.uu.se/~david/web/PrattSumpter05.pdf
The ant Temnothorax albipennis is unique in that a group of these ants are good at collectively choosing the best nest site. When an ant finds a site, it goes through several stages of independent assessment, recruiting other ants to support its site, and bulking up the new colony via rapid transports to the site. The rules and strategy that the ants follow may results in collective decisions, despite how individual ants are responsible for assessments, by the growth rate of populations among these new sites. The authors of this paper set out to test this hypothesis with an agent-based model, where the agents abided by these rules. While the model is very complex, we hope to simulate it using a finite state machine. Additionally, we want to create a simulation of how the ants will move within the colony. 

- Preferential attachment in the growth of social networks: the internet encyclopedia Wikipedia 
https://arxiv.org/pdf/physics/0602026.pdf
The authors present an analysis of the statistical properties and growth of Wikipedia. The topological properties of this graph are in close analogy with those of the World Wide Web, but they point out that there is a very different growth mechanism. We plan to identify a growth mechanism in our experiment. Wikipedia growth can be described by local rules such as the preferential attachment mechanism, though users can act globally on the network. This paper concludes that being able to observe preferential attachment in the Wikipedia network is due to the difficulty of identifying the optimal information to refer to from a node, which results in favoring the "rich-get-richer" behavior.
 
- Improving the Robustness of Online Social Networks: A Simulation Approach of Network Interventions 
https://doi.org/10.3389/frobt.2020.00057 
This paper explores methods of controlling how robust an online social network is. They define robustness as the average coreness of each node, or how much effect removing that node would have on the system. Our end goal in the experiment is to identify coreness of different nodes (words) in the Wikipedia ecosystem. Their model incorporates benefit and cost functions to model whether a node will remain in the network. Their analysis explores ways to keep users in the network. They conclude that keeping a few core nodes in the network is more effective than keeping many outer nodes in the network at improving the robustness of the network. 

### Experiment Plan

We plan to implement k-core analysis in our initial experiment to help identify small interlinked core areas on a network. Additionally, we hope to identify a specific growth mechanism. Our final report will also inculde robustness, or the average coreness of each node. We are looking to understand how much effect removing one node would have on the Wikipedia system in its entirety. 

#### This might look like the following: 

![image](https://user-images.githubusercontent.com/42943695/135956178-7be28d2a-271f-4671-aac8-302259e1a3d1.png)
![image](https://user-images.githubusercontent.com/42943695/135956215-19eee954-1169-4363-a9cb-19e8463c47d7.png)
![image](https://user-images.githubusercontent.com/42943695/135956190-6796ebc6-929d-44a6-9b9c-ffba262a9b7d.png)
![image](https://user-images.githubusercontent.com/42943695/135956199-d2c1c30f-b044-4708-8633-9c61139cd3d8.png)
An example of the interpretation of the k-core analysis results would be for us to distinguish the nodes that still remain after the analysis versus the nodes that disappear after the analysis; this enables us to take a look at the nodes that are weakly linked to the rest of the network and also to use this to measure the coreness of our network.

### Next Steps
The immediate individual goals in front of us is to thoroughly go over the three annotated bibliography on our own first so that we start off with some level of understanding and come up with questions for discussion (e.g. what components to implement to our model). For our group goal for the first week, we aim to implement the BA model with preferential attachment with (hopefully) the Wikipedia dataset and get it working. Even better, we would have made little explorations of incorporating parts from the two other papers.
Plus, we have a task board up and running under the *Projects* bar in this repository!
