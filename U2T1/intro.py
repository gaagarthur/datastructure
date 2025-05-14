import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import osmnx as ox

G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")
nodes = nx.number_of_nodes(G)
walfredo_gurgel = (ox.geocode("Complexo Hospitalar Mosenhor Walfredo Gurgel, natal RN, Brazil"))
node_walfredo_gurgel = ox.distance.nearest_nodes(G,walfredo_gurgel[1],walfredo_gurgel[0])
neighborhoods = {"Lagoa Nova", "Candelaria", "Capim Macio", "Neopolis", "Nova Descoberta", "Pitimbu", "Ponta Negra", "Petropolis", "Alecrim", "Mae Luiza", "Quintas", "Redinha"}
G = ox.add_edge_speeds(G) #add speed to edges
G = ox.routing.add_edge_travel_times(G) #add traveltime to edges
with open("routes.txt", "w") as file:
        print("", file=file)

for nh in neighborhoods:
    destin = (ox.geocode(f"{nh}, natal, RN, Brazil"))
    node_destin = ox.distance.nearest_nodes(G,destin[1],destin[0])
    route = nx.shortest_path(G,node_walfredo_gurgel, node_destin, weight="length", method="dijkstra")
    total_travel_time = 0
    for i in range(len(route) - 1):
        edge_data = G.get_edge_data(route[i], route[i+1])
        edge = list(edge_data.values())[0]
        total_travel_time += edge["travel_time"]

    with open("routes.txt", "a") as file:
        print(f"{nh}:", file=file)
        print(f"Travel time: {total_travel_time}",file=file)
        print(f"path: {route}\n", file=file)

    

for u, v, attrs in G.edges(data=True):
    print(f"Edge ({u}, {v}) has attributes: {attrs}")
    exit()

#print(walfredo_gurgel)
#print(nx.is_directed(G))

