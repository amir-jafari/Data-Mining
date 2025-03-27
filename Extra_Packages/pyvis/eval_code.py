
import networkx as nx
from pyvis.network import Network

# Create a social network graph
G = nx.Graph()


# Sample data: Social network connections (friendships)
people = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Fiona", "George", "Hannah", "Ian", "Julia"
]

# Adding nodes (people)
for person in people:
    G.add_node(person, title=f"Person: {person}")

# Adding edges (friendships)
friendships = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Alice", "David"),
    ("Bob", "Emma"), ("Charlie", "Fiona"), ("David", "George"),
    ("Emma", "Hannah"), ("Fiona", "Ian"), ("George", "Julia"),
    ("Hannah", "Alice"), ("Ian", "Charlie"), ("Julia", "Emma")
]

G.add_edges_from(friendships)

# Create a Pyvis Network object
net = Network(notebook=True, height="600px", width="100%", bgcolor="#222222", font_color="white")

# Convert the NetworkX graph to Pyvis
net.from_nx(G)

# Show the interactive graph
net.show("social_network.html")

print("Graph saved as social_network.html. Open it in a browser to view.")
