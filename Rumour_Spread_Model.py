# -*- coding: utf-8 -*-
"""Copy of sna.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uquWlOTmTJPsExYoUz-f4H_YZ8yZDArp
"""

import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
real_df = pd.read_csv('/content/drive/MyDrive/datasheet/Fake.csv')
fake_df = pd.read_csv('/content/drive/MyDrive/datasheet/True.csv')
# Add a new column 'Rumor' to the real and fake rumor datasets
real_df['Rumor'] = True
fake_df['Rumor'] = False
print(real_df.columns)
# Set up the SEIZ model
def run_SEIZ_model(G, p, beta, sigma, delta, t_max):
    # Set up the initial conditions
    N = G.number_of_nodes()
    infected_nodes = np.random.choice(G.nodes, size=int(N*p), replace=False)
    exposed_nodes = []

    # Simulate the model
    infected_count = []
    exposed_count = []
    for t in range(t_max):
        # Infect susceptible nodes
        for node in infected_nodes:
            neighbors = list(G.neighbors(node))
            susceptible_neighbors = [n for n in neighbors if n not in infected_nodes and n not in exposed_nodes]
            for neighbor in susceptible_neighbors:
                if np.random.random() < beta:
                    exposed_nodes.append(neighbor)

        # Move exposed nodes to infected state
        newly_infected = []
        for node in exposed_nodes:
            if np.random.random() < sigma:
                newly_infected.append(node)
        infected_nodes = np.concatenate([infected_nodes, newly_infected])
        exposed_nodes = [node for node in exposed_nodes if node not in newly_infected]

        # Create zombie nodes
        zombie_nodes = []
        for node in infected_nodes:
            if np.random.random() < delta:
                zombie_nodes.append(node)
        infected_nodes = [node for node in infected_nodes if node not in zombie_nodes]

        # Record the number of infected and exposed nodes
        infected_count.append(len(infected_nodes))
        exposed_count.append(len(exposed_nodes))

    return infected_count, exposed_count

# Set up the Barabasi-Albert model
def run_BA_model(N, m, p, beta, sigma, delta, t_max):
    G = nx.barabasi_albert_graph(N, m)
    return run_SEIZ_model(G, p, beta, sigma, delta, t_max)

# Set up the Small World model
def run_SW_model(N, k, p, beta, sigma, delta, t_max):
    G = nx.watts_strogatz_graph(N, k, p)
    return run_SEIZ_model(G, p, beta, sigma, delta, t_max)


# Set up the simulation parameters
N = 1000 # number of nodes
m = 3 # number of edges to attach from a new node for the Barabasi-Albert model
k = 10 # number of nearest neighbors for the Small World model
p = 0.1 # fraction of initially infected nodes
beta = 0.2 # infection rate
sigma = 0.1 # incubation rate
delta = 0.05 # zombie creation rate
t_max = 100 # number of time steps

# Load real and fake rumor datasets
real_rumors = nx.from_pandas_edgelist(real_df, source='title', target='text')
fake_rumors = nx.from_pandas_edgelist(fake_df, source='title', target='text')

# Run the simulations
infected_real_SEIZ, exposed_real_SEIZ = run_SEIZ_model(real_rumors, p, beta, sigma, delta, t_max)
infected_fake_SEIZ, exposed_fake_SEIZ = run_SEIZ_model(fake_rumors, p, beta, sigma, delta, t_max)
infected_BA, exposed_BA = run_BA_model(N, m,p, beta, sigma, delta, t_max)
infected_SW, exposed_SW = run_SW_model(N, k, p, beta, sigma, delta, t_max)

# Plot the results
fig, axs = plt.subplots(4, 1, figsize=(10, 20))
axs[0].plot(infected_real_SEIZ)
axs[0].set_title('Real SEIZ model')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Infected')

axs[1].plot(infected_fake_SEIZ)
axs[1].set_title('Fake SEIZ model')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Infected')

axs[2].plot(infected_BA)
axs[2].set_title('Barabasi-Albert model')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Infected')

axs[3].plot(infected_SW)
axs[3].set_title('Small World model')
axs[3].set_xlabel('Time')
axs[3].set_ylabel('Infected')

plt.tight_layout()
plt.show()

from google.colab import drive
drive.mount('/content/drive')