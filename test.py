import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)
# remove = [node for node,degree in G.degree().items() if degree > 2]
G.remove_node(1)
nx.draw_networkx(G)
plt.show()