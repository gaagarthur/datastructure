# Main imports
import pandas as pd           # For data manipulation and reading tabular files
import networkx as nx         # For building and analyzing graphs
#MOD.: commnet import
#import matplotlib.pyplot as plt  # For plotting graphs
import numpy as np            # For numerical operations

# Optional configurations

#plt.style.use("ggplot")       # Sets the plot style to 'ggplot' for better aesthetics

#MOD.: Paths
# Paths to the input files
nodes_file = "base/GraphTest_nodes.txt"
edges_file = "base/GraphTest_edges.txt"

# Load data into DataFrames
df_nodes = pd.read_csv(nodes_file, sep="\t")  # Reads the node table using tab as separator
df_edges = pd.read_csv(edges_file, sep="\t")  # Reads the edge table using tab as separator

#MOD.: Removed preview data section

# Initialize as a MultiDiGraph to support multiple directed edges between the same pair of nodes
# G = nx.MultiDiGraph()

# Use MultiGraph() instead of MultiDiGraph() if directionality is not important.
# This allows multiple undirected edges between the same node pairs, useful for modeling
# symmetric or bidirectional interactions like Van der Waals forces.

G = nx.MultiGraph()

# Add all nodes with their attributes
for _, row in df_nodes.iterrows():
    node_id = row["NodeId"]                      # Extract the node identifier
    attributes = row.drop("NodeId").to_dict()    # Convert the remaining columns to a dictionary of attributes
    G.add_node(node_id, **attributes)   
#MOD.: Print and node's metadata explanation removed

for _, row in df_edges.iterrows():
    source = row["NodeId1"]                  # Source node identifier
    target = row["NodeId2"]                  # Target node identifier
    attributes = row.drop(["NodeId1", "NodeId2"]).to_dict()  # All remaining columns become edge attributes

    # Safe conversion of numeric values (e.g., distance, angle, etc.)
    for key in attributes:
        val = attributes[key]
        if pd.isna(val) or val == "nan":     # Handle missing or non-numeric values
            attributes[key] = None
        else:
            try:
                attributes[key] = float(val)  # Convert strings to float when possible
            except (ValueError, TypeError):
                pass  # Leave as string if conversion fails
    G.add_edge(source, target, **attributes)

#MOD.: Print and edge's metadata explanation removed

#MOD.: data access example removed

#MOD.: calculate attributes
#=============================================================
G_simple = nx.Graph(G) #convert to simple graph

if len(G_simple) == 0:
    raise ValueError("G_simple is empty.")


Gc = nx.k_shell(G_simple,3) #calculate 3-core
Gs = nx.k_shell(G_simple, k=2) # calculate the 2-shell
cc = nx.closeness_centrality(G) #calculate closeness

# Add new attributes
for node in G.nodes():
    if node in Gc:
        G.nodes[node]['coshe'] = 1
        
    else:
        G.nodes[node]['coshe'] = 0
    if node in Gs:
        G.nodes[node]['coshe'] = 2

    G.nodes[node]['neig'] = G_simple.degree[node] #calculate # neighbors
    G.nodes[node]['close'] = cc[node]
#======================================================================

def sanitize_attributes(G):
    # Fix node attributes: replace None or NaN values with empty strings
    for node, attrs in G.nodes(data=True):
        for k, v in attrs.items():
            if v is None or (isinstance(v, float) and pd.isna(v)):
                G.nodes[node][k] = ""

    # Fix edge attributes: replace None or NaN values with empty strings
    for u, v, key, attrs in G.edges(keys=True, data=True):
        for k, v_attr in attrs.items():
            if v_attr is None or (isinstance(v_attr, float) and pd.isna(v_attr)):
                G.edges[u, v, key][k] = ""

# Apply attribute sanitization to make the graph exportable to GEXF format
sanitize_attributes(G)


#MOD.: Path, commented print
# Export the graph to a GEXF file, which can be opened in Gephi or reloaded in Python
nx.write_gexf(G, "base/netwokr.gexf",version="1.2draft")
#i = nx.diameter(G)
#print(i)

#MOD.:Removed Plotting section