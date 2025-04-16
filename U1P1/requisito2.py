import networkx as nx  # Network analysis
import matplotlib.pyplot as plt  # Plotting
import math as mt  # For logarithmic scaling

# File path components for loading graphs
file_beg = "basedados/avaliacao_geral/"
file_end = ".gexf"

# Define PPgEEC evaluation periods
list_ppgeec = list(range(2012, 2025, 4))

# Process each evaluation year
for year in list_ppgeec:

    # Special file name for the first interval
    if year == 2012:
        file_path = f"{file_beg}2010-2012{file_end}"
    else:
        file_path = f"{file_beg}{year-3}-{year}{file_end}"

    # Try loading the graph
    try:
        G = nx.read_gexf(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        continue

    # Compute node sizes proportional to degree
    degrees = list(G.degree())
    node_sizes = [deg * 150 for node, deg in degrees]

    # Set edge colors and weights based on attributes
    edge_colors = []
    new_weights = []
    for node_1, node_2 in G.edges():
        if G.nodes[node_1].get("is_permanent") and G.nodes[node_2].get("is_permanent"):
            edge_colors.append("red")
        else:
            edge_colors.append("black")

        value = (G.edges[node_1, node_2].get("citation_num", 0)) + 1  # +1 to avoid log(0)
        new_weights.append(1 + mt.log(value))

    # get 5 nodes w/ highest degree
    sorted_degrees = sorted(degrees, key=lambda x: x[1], reverse=True)
    top_nodes = {node for node, deg in sorted_degrees[:5]}

    # Highlight top nodes in red
    node_colors = ['red' if node in top_nodes else 'lightblue' for node in G.nodes()]

    # Create figure and draw graph
    plt.figure(figsize=(70, 70))

    if year == 2012:
        plt.title("2010-2012", fontsize=300)
    else:
        plt.title(f"{year-3}-{year}", fontsize=300)

    nx.draw_kamada_kawai(
        G,
        with_labels=False,
        node_color=node_colors,
        node_size=node_sizes,
        alpha=0.8,
        edge_color=edge_colors,
        width=new_weights
    )
    

    # Save the figure
    plt.savefig(f"images/graphPPgEEC{year}.svg")
    plt.clf()