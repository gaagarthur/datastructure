import pandas as pd           # For data manipulation and reading tabular files
import networkx as nx         # For building and analyzing graphs
#import matplotlib.pyplot as plt  # For plotting graphs
import numpy as np

nodes = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
edges = [('A','B'),('A','C'),('A','D'),('A','F'),('F','G'),('D','E'),
         ('G','H'),('H','I'),('I','J'),('I','K'),('J','L'),('K','M')]
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)


# Export the graph to a GEXF file, which can be opened in Gephi or reloaded in Python
nx.write_gexf(G, "closeness.gexf")
print("Export completed successfully.")

