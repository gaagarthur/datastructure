# Main imports
import pandas as pd           # For data manipulation and reading tabular files
import networkx as nx         # For building and analyzing graphs
#import matplotlib.pyplot as plt  # For plotting graphs
import numpy as np            # For numerical operations

# Optional configurations

#plt.style.use("ggplot")       # Sets the plot style to 'ggplot' for better aesthetics

# Paths to the input files
nodes_file = "base/GraphTest_nodes.txt"
edges_file = "base/GraphTest_edges.txt"

# Load data into DataFrames
df_nodes = pd.read_csv(nodes_file, sep="\t")  # Reads the node table using tab as separator
df_edges = pd.read_csv(edges_file, sep="\t")  # Reads the edge table using tab as separator

G = nx.MultiGraph()

# Add all nodes with their attributes
for _, row in df_nodes.iterrows():
    node_id = row["NodeId"]                      # Extract the node identifier
    attributes = row.drop("NodeId").to_dict()    # Convert the remaining columns to a dictionary of attributes
    G.add_node(node_id, **attributes)   

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
"""
G_simple = nx.Graph(G)
core_numbers = nx.core_number(G_simple)

# Step 1: Get k_max (maximum core number)
k_max = max(core_numbers.values())
#print(k_max)
# Step 2: Identify core nodes
core_nodes = [n for n, k in core_numbers.items() if k == k_max]

# Step 3: Identify candidate shell nodes with core_number == k_max - 1
shell_k_minus_1 = [n for n, k in core_numbers.items() if k == k_max - 1]

# Step 4: Among shell_k_minus_1, keep only those connected to core
protecting_shell = set()
for node in shell_k_minus_1:
    neighbors = G_simple.neighbors(node)
    if any(neigh in core_nodes for neigh in neighbors):
        protecting_shell.add(node)

# Optional: annotate
for node in G.nodes():
    G.nodes[node]['core'] = 1 if node in core_nodes else 0
    #G.nodes[node]['protecting_shell'] = 1 if node in protecting_shell else 0
    if node in protecting_shell:
        G.nodes[node]['core'] =+ 1
"""

     
"""
G_simple = nx.Graph(G)
core_num = nx.core_number(G_simple)
#print(type(core_num))
k_max = max(core_num.values())   

Gc = nx.k_core(G_simple)
Gs = nx.k_shell(G_simple,k=k_max-1,core_number=core_num)
core_nodes=[]
for node in G.nodes():

    if (node in Gc):
        G.nodes[node]['core']=1
        if (node in Gs):
            G.nodes[node]['core']=+1
    else:
        G.nodes[node]['core']=0

"""

G_simple = nx.Graph(G)

if len(G_simple) == 0:
    raise ValueError("G_simple is empty.")

#core_num = nx.core_number(G_simple)
#k_max = max(core_num.values())

Gc = nx.k_shell(G_simple,3)
Gs = nx.k_shell(G_simple, k=2)
cc = nx.closeness_centrality(G)

core_nodes = []

for node in G.nodes():
    if node in Gc:
        G.nodes[node]['coshe'] = 1
        
    else:
        G.nodes[node]['coshe'] = 0
    if node in Gs:
        G.nodes[node]['coshe'] = 2

    G.nodes[node]['neig'] = G_simple.degree[node]
    G.nodes[node]['close'] = cc[node]

"""
commum =[]
G_simple = nx.Graph(G)
no = list(nx.k_shell(G_simple,3))
no2 = list(nx.k_shell(G_simple,2))
for node in no2:
    if(node in no):
        commum.append(node)


print(no)
print(len(no))
print(commum)
print(len(commum))
"""
#k_cores = set([v for k,v in nx.core_number(G_simple).items()])
#print(k_cores)

#core_numbers = nx.core_number(G_simple)
#print(core_numbers)
#max_k = max(core_numbers.values())
#print(max_k)



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



# Export the graph to a GEXF file, which can be opened in Gephi or reloaded in Python
nx.write_gexf(G, "base/netwokr.gexf",version="1.2draft")
#i = nx.diameter(G)
#print(i)