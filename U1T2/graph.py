import networkx as nx
#import nxviz as nv
import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler os arquivos CSV
edges_df = pd.read_csv('database/edges.csv')
nodes_df = pd.read_csv('database/nodes.csv')

# 2. Criar o grafo
G = nx.from_pandas_edgelist(edges_df, source='source', target='target', edge_attr=True)


for idx, row in nodes_df.iterrows():
    G.nodes[row['node']]['ing_type'] = row['ing_type']
    G.nodes[row['node']]['instances'] = row['instances']

sizes = [(G.nodes[node]['instances']**2)*100 for node in G.nodes]  # multiplica pra ficar mais visível
sizes_edges = [G.edges[edge]['instances']*3 for edge in G.edges]
colors = [G.nodes[node]['ing_type'] for node in G.nodes]
for i in range(G.number_of_nodes()):
    if colors[i] == "carbohydrate":
        colors[i]="lightblue"
    elif colors[i] == "protein":
        colors[i]="lightpink"
    elif colors[i] == "fat":
        colors[i]="gold"
    elif colors[i] == "vegetable":
        colors[i]="lightgreen"
    elif colors[i] == "fruit":
        colors[i]="firebrick"
    elif colors[i] == "dairy":
        colors[i]="violet"
    elif colors[i] == "condiment":
        colors[i]="black"
    elif colors[i] == "other":
        colors[i]="gray"

a = nx.attribute_assortativity_coefficient(G, "ing_type")
print(a)

# Desenhar

plt.figure(figsize=(20, 15))

nx.draw_kamada_kawai(
                     G,
                     with_labels=True,
                     node_color=colors,
                     node_size=sizes,
                     alpha=.8,
                     edge_color='black',
                     width=sizes_edges
                     )
#edge_labels = nx.get_edge_attributes(G, 'weight')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.savefig("images/graph.png")
plt.savefig("images/graph.svg")  # Vector output