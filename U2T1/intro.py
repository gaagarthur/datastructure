import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox
import time
from dijkstra import classic_dijkstra_path


G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")
#nodes = nx.number_of_nodes(G)
walfredo_gurgel = (ox.geocode("Complexo Hospitalar Mosenhor Walfredo Gurgel, natal RN, Brazil"))
node_walfredo_gurgel = ox.distance.nearest_nodes(G,walfredo_gurgel[1],walfredo_gurgel[0])
neighborhoods = {"Lagoa Nova", "Candelaria"}#, "Capim Macio", "Neopolis", "Nova Descoberta", "Pitimbu", "Ponta Negra", "Petropolis", "Alecrim", "Mae Luiza", "Quintas", "Redinha"}
G = ox.add_edge_speeds(G) #add speed to edges
G = ox.routing.add_edge_travel_times(G) #add traveltime to edges

searches = ["Dijkstra miniheap","Dijkstra O(n^2)","OSMnx"]

with open("routes.txt", "w") as file:
        print("", file=file)

for nh in neighborhoods:
    taget = (ox.geocode(f"{nh}, natal, RN, Brazil"))
    taget_node = ox.distance.nearest_nodes(G,taget[1],taget[0])
    
#=========================== DIJKSTRA MINIHEAP ==================================
    start_time = time.perf_counter()
    route = nx.shortest_path(G,node_walfredo_gurgel, taget_node, weight="length", method="dijkstra")
    end_time = time.perf_counter()
    print(f"dijkstra miniheap for {nh}: {(end_time - start_time):.4f} seconds")
#=========================== DIJKSTRA O(N^2) =====================================
    start_time = time.perf_counter()
    route_dk = classic_dijkstra_path(G,node_walfredo_gurgel,taget_node,weight="length")
    end_time = time.perf_counter()
    print(f"dijkstra o(n^2) for {nh}: {(end_time - start_time):.4f} seconds")
#================================ OSMNX ==========================================
    start_time = time.perf_counter()
    path = list( ox.routing.k_shortest_paths(G, node_walfredo_gurgel, taget_node, 1, weight='length'))
    route_osm =path[0]
    end_time = time.perf_counter()
    #print(f"dijkstra osmnx for {nh}: {(end_time - start_time):.4f} seconds\n")

#=================================== PLOT =========================================
    
    #plt.figure(figsize=(70, 70))
    #fig, ax = ox.plot_graph_route(G, route, node_size=0, show=False)
    #plt.savefig(f"{nh}_dijkstra_miniheap.png")
    #plt.close(fig)
    #fig, ax = ox.plot_graph_route(G, route_dk, node_size=0, show=False, save=False)
    #plt.savefig(f"{nh}_dijkstra_n2.svg")
    #plt.close(fig)
    #fig, ax = ox.plot_graph_route(G, route_osm, node_size=0, show=False, save=False)
    #plt.savefig(f"{nh}_osmnx.svg")
    #plt.close(fig)

#=========================== DIJKSTRA MINIHEAP ==================================
    total_travel_time = [0,0,0]
    total_distance = [0,0,0]
    for i in range(len(route) - 1):
        edge_data = G.get_edge_data(route[i], route[i+1])
        edge = list(edge_data.values())[0]
        total_travel_time[0] += edge["travel_time"]
        total_distance[0] += edge["length"]

#=========================== DIJKSTRA O(N^2) ==================================
    #total_travel_time_dk = 0
    #total_distance_dk = 0
    for i in range(len(route_dk) - 1):
        edge_data = G.get_edge_data(route_dk[i], route_dk[i+1])
        edge = list(edge_data.values())[0]
        total_travel_time[1] += edge["travel_time"]
        total_distance[1] += edge["length"]
        
#=========================== OSMNX ==================================
    #total_travel_time_osm = 0
    #total_distance_osm = 0
    for i in range(len(route_osm) - 1):
        edge_data = G.get_edge_data(route_osm[i], route_osm[i+1])
        edge = list(edge_data.values())[0]
        total_travel_time[2] += edge["travel_time"]
        total_distance[2] += edge["length"]



    with open("routes.txt", "a") as file:
        print(f"{nh}:", file=file)
        for i in range(0,3,1):
            print(f"Travel time {searches[i]}: {total_travel_time[i]:.4f}",file=file)
            print(f"Total Distance {searches[i]}: {total_distance[i]:.4f}",file=file)
        print("\n",file=file)

        #print(f"path: {route}\n", file=file)

    

#for u, v, attrs in G.edges(data=True):
    #print(f"Edge ({u}, {v}) has attributes: {attrs}")
    #exit()

#print(walfredo_gurgel)
#print(nx.is_directed(G))

