import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from(["A","B","C","D"])

G.add_edges_from([("A","B"),("B","C"),("A","C")])

nx.draw(G, with_labels=True)
plt.show()