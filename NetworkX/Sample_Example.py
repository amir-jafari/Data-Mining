import networkx as nx
import matplotlib.pyplot as plt

# creating an empty graph object
G = nx.Graph()

# adding nodes to the graph
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# adding edges to the graph
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (1, 3), (1,4), (1,1)])

# display the graph
nx.draw(G, with_labels = True)
plt.show()