import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox
import time
import pandas as pd
import auxfuncs as aux

G = aux.import_graph()

df = pd.read_csv("../db/centroid_filtered.csv")

max_lat,min_lat,max_lon,min_lon = aux.limit_coods(df)
print("\n1")
step_lat = (max_lat+min_lat)/2
step_lon = (min_lon-max_lon)/5

print(max_lat,min_lat,max_lon,min_lon)
print(step_lat,step_lon)

all_nodes, all_agents, hq = aux.assign_nodes(G, df, min_lon,step_lat,step_lon)
print("\n2")

print(all_agents)


routes_a, routes_d, routes_dc, time_a, dist_a, time_d, dist_d, time_dc, dist_dc = aux.path_f(G,hq,all_agents)

routes_colors = ['red','blue', 'green', 'orange',
                 'purple', 'cyan', 'magenta', 'yellow',
                 'brown', 'orangered']
print ("\n\n",len(routes_a))
print (len(routes_d))
print (len(routes_dc),"\n\n")
node_sizes, node_colors = aux.node_sizes_colors(G, all_nodes)

#fig2, ax2 = ox.plot_graph_routes(G,routes=routes_a,
                                 #route_colors=['red','blue', 'green', 'orange','purple', 'cyan', 'magenta', 'yellow','brown', 'orangered'], 
                                 #show=False, close=False, node_size=node_sizes, node_color=node_colors)

#fig2.savefig(f"../images/map_routeA.svg", dpi=150, bbox_inches="tight")

print((dist_a))
print(sum(dist_d))
print(sum(dist_dc))

print(sum(dist_a)/10)
print(sum(dist_d)/10)
print(sum(dist_dc)/10)


"""
print("\n3")
aux.plot_routes_A(G, routes_a,node_sizes, node_colors, routes_colors,save="Astar")
print("\n4")
aux.plot_routes_A(G, routes_d,node_sizes, node_colors, routes_colors,save="Dijk")
print("\n5")
aux.plot_routes_A(G, routes_dc,node_sizes, node_colors, routes_colors,save="DijkClass")
"""
