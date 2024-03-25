import networkx as nx
import matplotlib.pyplot as plt
# Create a graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Add edges
G.add_edge(1, 2, weight=2)
G.add_edge(1, 3, weight=10)
G.add_edge(2, 4, weight=1)
G.add_edge(3, 4, weight=2)

# display the graph
nx.draw(G, with_labels = True)
plt.show()

# Use Dijkstra's algorithm to find the shortest path
path = nx.dijkstra_path(G, 1, 4, weight='weight')

print(path)