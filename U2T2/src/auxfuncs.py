import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as approx
import osmnx as ox
import math
import pandas as pd
import os
from dijkstra import classic_dijkstra_path
import json

def import_graph():

#--------------------- getting map --------------------------------------
    if(os.path.exists("../db/natal_drive.graphml")):
        G = ox.load_graphml("../db/natal_drive.graphml")
    else:
        G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")
        bridge =(-5.781578, -35.247751)
        G_bridge = ox.graph_from_point(bridge, dist=800, network_type="drive")#-5.781578, -35.247751
        G = nx.compose(G, G_bridge)
        ox.distance.add_edge_lengths(G)
        ox.add_edge_speeds(G)
        ox.add_edge_travel_times(G)
        ox.save_graphml(G, filepath="../db/natal_drive.graphml")
    return G

def limit_coods(df):
    max_lat = -40.0
    min_lat = 0
    max_lon = -7.0
    min_lon = 0

    for row in df.itertuples(index=False):
        lat = row.Lat
        lon = row.Lon
    if(lat<min_lat):
        min_lat = lat
    elif(lat>max_lat):
        max_lat = lat

    if(lon<min_lon):
        min_lon = lon
    elif(lon>max_lon):
        max_lon = lon

    
    return max_lat,min_lat,max_lon,min_lon

def assign_nodes(G, df, min_lon,step_lat,step_lon):
    collec_stat = []
    agent_1 = []
    agent_2 = []
    agent_3 = []
    agent_4 = []
    agent_5 = []
    agent_6 = []
    agent_7 = []
    agent_8 = []
    agent_9 = []
    agent_10 = []
    print("\n1.1")
    for row in df.itertuples(index=False):
        lon = row.Lon
        lat = row.Lat
        node = ox.distance.nearest_nodes(G, X=lat, Y=lon)
        att_dis = row.District
        att_neig = row.Neighborhood
        collec_stat.append([node,att_dis,att_neig])
        if (lat<=step_lat):

            if(lon<=(min_lon-step_lon)):
                agent_1.append(node)
            elif(lon<=(min_lon-(step_lon*2))):
                agent_2.append(node)      
            elif(lon<=(min_lon-(step_lon*3))):
                agent_3.append(node)
            elif(lon<=(min_lon-(step_lon*4))):
                agent_4.append(node)
            else:
                agent_5.append(node)
        else:

            if(lon<=(min_lon-step_lon)):
                agent_6.append(node)
            elif(lon<=(min_lon-(step_lon*2))):
                agent_7.append(node)
            elif(lon<=(min_lon-(step_lon*3))):
                agent_8.append(node)
            elif(lon<=(min_lon-(step_lon*4))):
                agent_9.append(node)
            else:
                agent_10.append(node)
    print("\n1.2")
    hq = ox.distance.nearest_nodes(G, X=-35.26213858466005, Y=-5.753250924379606)
    all_nodes = collec_stat + [[hq,"Center","Center"]]
  

    all_agents = {
              "ag1" : agent_1,
              "ag2" : agent_2,
              "ag3" : agent_3,
              "ag4" : agent_4,
              "ag5" : agent_5,
              "ag6" : agent_6,
              "ag7" : agent_7,
              "ag8" : agent_8,
              "ag9" : agent_9,
              "ag10" : agent_10,
    }
    return all_nodes, all_agents, hq
#===========================================================================================
#===========================================================================================
def path_f(G,hq,all_agents):
    c1=os.path.exists("../db/all_routes.json")
    c2=os.path.exists("../db/all_routes_D.json")
    c3=os.path.exists("../db/all_routes_DC.json")
    c4=os.path.exists("../db/to_tra_ti.json")
    c5=os.path.exists("../db/to_tra_ti_D.json")
    c6=os.path.exists("../db/to_tra_ti_DC.json")
    c7=os.path.exists("../db/total_dist.json")
    c8=os.path.exists("../db/total_dist_D.json")
    c9=os.path.exists("../db/total_dist_DC.json")
    if((c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and c9)==False):
        print("inside if")
        all_distances_as = {f"dist_{i}": {} for i in range(1, 11)}
        all_distances_dijk = {f"dist_{i}": {} for i in range(1, 11)}
        all_distance = {f"dist_{i}": {} for i in range(1, 11)}
        sequence_nodes = []
        sequence_nodes_D = []
        all_routes = []
        all_routes_D = []
        all_routes_DC = []
        to_tra_ti = [0,0,0,0,0,0,0,0,0,0]
        total_dist = [0,0,0,0,0,0,0,0,0,0]
        to_tra_ti_D = [0,0,0,0,0,0,0,0,0,0]
        total_dist_D = [0,0,0,0,0,0,0,0,0,0]
        to_tra_ti_DC = [0,0,0,0,0,0,0,0,0,0]
        total_dist_DC = [0,0,0,0,0,0,0,0,0,0]
        #sum = 0
        print("\n2.1")
        for i, agent in enumerate(all_agents, start=1):
            full_route = []
            full_route_D = []
            full_route_DC = []
            key = f"dist_{i}"
            #print(agent)
            nodes = [hq] + all_agents[agent]
            distances = {}
            distances_dijkstra = {}
            #distances_dijk_sqr = {}

            for u in nodes:
                for v in nodes:
                    if u != v:
                        try:
                            d = nx.astar_path_length(G, u, v, weight='length', heuristic=lambda u, v: ox.distance.euclidean(G.nodes[u]['y'], G.nodes[u]['x'],G.nodes[v]['y'], G.nodes[v]['x']))
                            distances[(u, v)] = d
                        except nx.NetworkXNoPath:
                            distances[(u, v)] = float('inf')
                    
                        try:
                            d2 = nx.dijkstra_path_length(G, u, v, weight='length')
                            distances_dijkstra[(u, v)] = d2
                        except nx.NetworkXNoPath:
                            distances_dijkstra[(u, v)] = float('inf')
                    

            all_distances_as[key] = distances
            all_distances_dijk[key] = distances_dijkstra

            TSP_G = nx.complete_graph(nodes, create_using=nx.DiGraph())
            TSP_G_D = TSP_G
            for u in nodes:
                for v in nodes:
                    if u != v:
                        TSP_G[u][v]['weight'] = distances[(u, v)]
                        TSP_G_D[u][v]['weight'] = distances_dijkstra[(u, v)]

            nodes_route = approx.greedy_tsp(TSP_G, weight='weight', source=hq)
            nodes_route_D = approx.greedy_tsp(TSP_G, weight='weight', source=hq)
            #print(nodes_route)
            #sum= sum+len(nodes_route)-2
            #print(sum,"\n\n")
            sequence_nodes.append(nodes_route)
            sequence_nodes_D.append(nodes_route_D)

            for j in range(len(nodes_route) - 1):
                u = nodes_route[j]
                v = nodes_route[j + 1]

                seg = nx.astar_path(G, u, v, weight='length', heuristic=lambda u, v: ox.distance.euclidean(G.nodes[u]['y'], G.nodes[u]['x'],G.nodes[v]['y'], G.nodes[v]['x']))

                if j == 0:
                    full_route.extend(seg)
                else:
                    full_route.extend(seg[1:])
            
                to_tra_ti, total_dist = total_distance_time(G, full_route_D, seg, i)

            all_routes.append(full_route)

            for j in range(len(nodes_route_D) - 1):
                u = nodes_route_D[j]
                v = nodes_route_D[j + 1]

                seg = nx.dijkstra_path(G, u, v, weight='length')
                seg2 = classic_dijkstra_path(G, u, v, weight='length')

                if j == 0:
                    full_route_D.extend(seg)
                    full_route_DC.extend(seg2)
                else:
                    full_route_D.extend(seg[1:])
                    full_route_DC.extend(seg2[1:])

                to_tra_ti_D, total_dist_D = total_distance_time(G, full_route_D, seg, i)
                to_tra_ti_DC, total_dist_DC = total_distance_time(G, full_route_DC, seg2, i)

            all_routes_D.append(full_route_D)
            all_routes_DC.append(full_route_DC)

        print("\n2.2")
        with open("../db/all_routes.json", 'w') as f:
            json.dump(all_routes, f)

        with open("../db/all_routes_D.json", 'w') as f:
            json.dump(all_routes_D, f)

        with open("../db/all_routes_DC.json", 'w') as f:
            json.dump(all_routes_DC, f)

        with open("../db/to_tra_ti.json", 'w') as f:
            json.dump(to_tra_ti, f)

        with open("../db/to_tra_ti_D.json", 'w') as f:
            json.dump(to_tra_ti_D, f)

        with open("../db/to_tra_ti_DC.json", 'w') as f:
            json.dump(to_tra_ti_DC, f)

        with open("../db/total_dist.json", 'w') as f:
            json.dump(total_dist, f)

        with open("../db/total_dist_D.json", 'w') as f:
            json.dump(total_dist_D, f)

        with open("../db/total_dist_DC.json", 'w') as f:
            json.dump(total_dist_DC, f)
    else:
        with open("../db/all_routes.json", 'r') as f:
            all_routes=json.load( f)

        with open("../db/all_routes_D.json", 'r') as f:
            all_routes_D=json.load( f)

        with open("../db/all_routes_DC.json", 'r') as f:
            all_routes_DC=json.load( f)

        with open("../db/to_tra_ti.json", 'r') as f:
            to_tra_ti=json.load( f)

        with open("../db/to_tra_ti_D.json", 'r') as f:
            to_tra_ti_D=json.load( f)

        with open("../db/to_tra_ti_DC.json", 'r') as f:
            to_tra_ti_DC=json.load( f)

        with open("../db/total_dist.json", 'r') as f:
            total_dist=json.load( f)

        with open("../db/total_dist_D.json", 'r') as f:
            total_dist_D =json.load( f)

        with open("../db/total_dist_DC.json", 'r') as f:
            total_dist_DC =json.load(f) 
    

    return all_routes, all_routes_D,all_routes_DC, to_tra_ti,total_dist,to_tra_ti_D,total_dist_D,to_tra_ti_DC,total_dist_DC

def total_distance_time(G, full_route, seg, i):
    to_tra_ti = [0,0,0,0,0,0,0,0,0,0]
    total_dist = [0,0,0,0,0,0,0,0,0,0]

    if(len(full_route)>2):

        for k in range(len(seg) - 1):
            a = seg[k]
            b = seg[k + 1]

            edge_data = G.get_edge_data(a, b)

            edge = list(edge_data.values())[0]
            to_tra_ti[i - 1] += edge.get("travel_time", 0)
            total_dist[i - 1] += (edge.get("length", 0))/1000
    print("\ntimes dist")
    return to_tra_ti,total_dist

def node_sizes_colors(G, all_nodes):

    node_attr = {item[0]: item[1] for item in all_nodes}
    node_colors = []
    node_sizes =[]
    collec = 10
    Hq = 25
#======================================================
    color_map = {
        "North":"red",
        "South":"cyan",
        "East":"lime",
        "West":"yellow",
        "Center":"magenta",
    }
    sizes_map = {
        "North":collec,
        "South":collec,
        "East":collec,
        "West":collec,
        "Center":Hq,
    }
#====================  Logic  ======================
    for node in G.nodes():
        if node in node_attr:
            color = color_map.get(node_attr[node],"white")
            size = sizes_map.get(node_attr[node],1)
        else:
            color = "white"
            size = 1
        node_colors.append(color)
        node_sizes.append(size)

    return node_sizes, node_colors

def plot_routes_A(G, routes, node_sizes, node_colors, routes_colors, save=""):
    fig2, ax2 = ox.plot_graph(G, show=False, close=False, node_size=node_sizes, node_color=node_colors)
    routes_colors = ['red','blue', 'green', 'orange','purple', 'cyan', 'magenta', 'yellow','brown', 'orangered', 'crimson', 'darkgreen', 'dodgerblue', 'firebrick',
            'forestgreen', 'hotpink', 'indianred', 'mediumblue', 'olivedrab',
            'peru', 'royalblue', 'saddlebrown', 'salmon', 'seagreen',
            'steelblue', 'tan', 'tomato', 'turquoise', 'violet']
    for i, route in enumerate(routes):
        # Cycle through the colors if there are more routes than colors
        color = routes_colors[i%len(routes_colors)]
        ox.plot_graph_route(G, route, route_color=color, route_linewidth=3,
                            node_size=0, ax=ax2, show=False, close=False)

    fig2.savefig(f"../images/map_route{save}.svg", dpi=150, bbox_inches="tight")
    fig2.clf()

def heuristic_maker(G):
    def heuristic(u, v):
        ux, uy = G.nodes[u]['x'], G.nodes[u]['y']
        vx, vy = G.nodes[v]['x'], G.nodes[v]['y']
        return math.hypot(ux - vx, uy - vy)
    return heuristic