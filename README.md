# Rumor-Spreading-Simulation-Using-SEIZ-Model


This project simulates the spread of rumors in different types of networks using a Susceptible-Exposed-Infected-Zombie (SEIZ) model. 

## Description

The SEIZ model is a type of compartmental model used in epidemiology to simulate how diseases spread. In this case, it's being used to simulate how rumors spread. The model has four states: 
- **Susceptible**: individuals who have not heard the rumor.
- **Exposed**: individuals who have heard the rumor but have not yet spread it.
- **Infected**: individuals who are actively spreading the rumor.
- **Zombie**: individuals who were spreading the rumor but have stopped.

The code first loads two datasets containing real and fake rumors, adds them to the networks, and then runs the SEIZ model on these networks. It also runs the SEIZ model on Barabasi-Albert (BA) and Small World (SW) networks for comparison. The number of infected and exposed individuals over time is recorded and plotted for each network.

### Barabasi-Albert Model

The Barabasi-Albert (BA) model is a network growth model that generates random scale-free networks using a preferential attachment mechanism. It's often used to model social networks. In this model, new nodes are added to the network one at a time. Each new node is connected to existing nodes with a probability that linearly depends on their degree.

### Small World Model

The Small World (SW) model is a type of graph where most nodes are not neighbors but can be reached from every other node by a small number of steps. It's often used to model networks where connections between nodes have a strong geographical component. In this model, a regular lattice is initialized, and then each edge is rewired with probability `p`.

## Installation

The code requires Python along with several packages: NetworkX, Pandas, NumPy, and Matplotlib. You can install these packages using pip:

```bash
pip install networkx pandas numpy matplotlib
