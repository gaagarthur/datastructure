import networkx as nx  # Import NetworkX for graph analysis
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Define the file path components
file_beg = "basedados/anos/"
file_end = "_authors_network.gexf"

list_edges = []
list_nodes = []
list_density = []
list_neighbors = []
list_years = list(range(2010, 2026))
list_ppgeec = list(range(2012, 2025, 4))
#-----------------------------COLECT DATA-----------------------------------------------------------------
# Loop through the years from 2010 to 2025 (16 years)
for year in list_years:

    file_path = f"{file_beg}{year}{file_end}"  # Construct the full file path
    
    # Load the graph from the GEXF file
    G = nx.read_gexf(file_path)
    
    # Calculate basic graph statistics
    nodes = G.number_of_nodes()  # Total number of nodes (authors)
    edges = G.number_of_edges()  # Total number of edges (connections)
    density = round(100 * nx.density(G), 2)
    avg_neighbors = round((2*edges) / nodes, 2)

    list_nodes.append(nodes)
    list_edges.append(edges)
    list_density.append(density)
    list_neighbors.append(avg_neighbors)
    
    # Output the results for the current year
    print(f"Year: {year}\n")
    print(f"Density: {density}%")  # Graph density as a percentage
    print(f"Nodes: {nodes}")  # Number of nodes
    print(f"Edges: {edges}")  # Number of edges    
    print(f"Avg. degree: {avg_neighbors}\n\n")# Average degree
#-----------------------------OUTPUT CURVE GRAPH------------------------------------------------------------------
fig, y1 = plt.subplots(figsize=(10, 6))

# Primary y-axis
y1.plot(list_years, list_edges, label='Edges')
y1.plot(list_years, list_nodes, label='Nodes')


y1.set_xlabel("Year")
y1.set_ylabel("Edges / Nodes", color='black')
y1.tick_params(axis='y')

# Create secondary y-axis
y2 = y1.twinx()
y2.plot(list_years, list_neighbors, color='orange', label='Avg. Neighbors')
y2.plot(list_years, list_density, color='lightgreen', label='Density (%)')

y2.set_ylabel("Avg. Neighbors / Density (%)", color='black')
y2.tick_params(axis='y')

for test_year in list_ppgeec:
    plt.axvline(x=test_year, color='gray', linestyle='--')

# Combine legends from both axes
lines1, labels1 = y1.get_legend_handles_labels()
lines2, labels2 = y2.get_legend_handles_labels()
plt.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title("Graph Metrics Over Time")
plt.grid(True)

plt.savefig("images/curve_graph.svg")
plt.savefig("images/curve_graph.png")
#-----------------------------OUTPUT BAR GRAPH-----------------------------------------------------------------
norm = plt.Normalize(min(list_nodes),max(list_nodes))
clrs = cm.coolwarm(norm(list_nodes))
fig, ax = plt.subplots(figsize=(10, 6))  # Use this instead of plt.figure()
bars = ax.bar(list_years, list_density, width=1.0, edgecolor='grey', color=clrs)

# Create ScalarMappable
color_scale = plt.cm.ScalarMappable(cmap=cm.coolwarm, norm=norm)
color_scale.set_array([])

# Tie the colorbar to the existing axes (ax)
cbar = fig.colorbar(color_scale, ax=ax)
cbar.set_label('Number of nodes')

# Labels and layout
ax.set_xlabel("Year")
ax.set_ylabel("Density (%)")
ax.set_title("Density per Year")
ax.set_xticks(list_years)
fig.tight_layout()

plt.savefig("images/bar_chart.png")
plt.savefig("images/bar_chart.svg")  # Vector output

