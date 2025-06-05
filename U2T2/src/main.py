import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox
import time
import os 
#--------------------- getting map --------------------------------------
if(os.path.exists("../db/natal_drive.graphml")):
  G = ox.load_graphml("../db/natal_drive.graphml")
else:
  G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")
  ox.save_graphml(G, filepath="../db/natal_drive.graphml")
  ox.add_edge_speeds(G)
  ox.add_edge_travel_times(G) 
  node1 = ox.distance.nearest_nodes(G, X=-35.2477214, Y=-5.7820319) #-5.7820319, -35.2477214
  node2 = ox.distance.nearest_nodes(G, X=-35.2482685, Y=-5.7806469) #-5.7806469, -35.2482685
  G.add_edge(node1, node2, key=0, length=200, highway='residential', bridge='yes', name='Restored Bridge')

fig, ax = ox.plot_graph(G, show=False, close=False, node_size = 2)
fig.savefig("../images/piedmont_map.svg", dpi=300, bbox_inches="tight")


#nodes = nx.number_of_nodes(G)
#walfredo_gurgel = (ox.geocode("Complexo Hospitalar Mosenhor Walfredo Gurgel, natal RN, Brazil"))
#node_walfredo_gurgel = ox.distance.nearest_nodes(G,walfredo_gurgel[1],walfredo_gurgel[0])
#neighborhoods = {"Lagoa Nova", "Candelaria"}#, "Capim Macio", "Neopolis", "Nova Descoberta", "Pitimbu", "Ponta Negra", "Petropolis", "Alecrim", "Mae Luiza", "Quintas", "Redinha"}
#G = ox.add_edge_speeds(G) #add speed to edges
#G = ox.routing.add_edge_travel_times(G) #add traveltime to edges