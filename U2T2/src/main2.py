import networkx as nx
from networkx.algorithms import approximation as approx
import matplotlib.pyplot as plt
import osmnx as ox
import time
import pandas as pd
import os 
#--------------------- getting map --------------------------------------
if(os.path.exists("../db/natal_drive.graphml")):
  G = ox.load_graphml("../db/natal_drive.graphml")
else:
  G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")
  bridge =(-5.781578, -35.247751)
  G_bridge = ox.graph_from_point(bridge, dist=800, network_type="drive")#-5.781578, -35.247751
  G = nx.compose(G, G_bridge)
  ox.add_edge_lengths(G)
  ox.add_edge_speeds(G)
  ox.add_edge_travel_times(G)
  ox.save_graphml(G, filepath="../db/natal_drive.graphml")

df = pd.read_csv("../db/centroid_filtered.csv")

collec_stat = []

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

step_lat = (max_lat+min_lat)/2
step_lon = (min_lon-max_lon)/5

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
#===============STOP===========================

#==================== Calculate where is the node for the HQ ==================================
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



all_distances = {f"dist_{i}": {} for i in range(1, 11)}
sequence_nodes = []
sum = 0

all_routes = []
total_travel_time = [0,0,0,0,0,0,0,0,0,0]
total_distance = [0,0,0,0,0,0,0,0,0,0]

for i, agent in enumerate(all_agents, start=1):
    full_route = []
    key = f"dist_{i}"
    #print(agent)
    nodes = [hq] + all_agents[agent]
    distances = {}

    for u in nodes:
        for v in nodes:
            if u != v:
                try:
                    d = nx.astar_path_length(G, u, v, weight='length', heuristic=lambda u, v: ox.distance.euclidean(G.nodes[u]['y'], G.nodes[u]['x'],G.nodes[v]['y'], G.nodes[v]['x']))
                    distances[(u, v)] = d
                except nx.NetworkXNoPath:
                    distances[(u, v)] = float('inf')

    all_distances[key] = distances

    TSP_G = nx.complete_graph(nodes, create_using=nx.DiGraph())

    for u in nodes:
      for v in nodes:
        if u != v:
            TSP_G[u][v]['weight'] = distances[(u, v)]

    nodes_route = approx.greedy_tsp(TSP_G, weight='weight', source=hq)
    #print(nodes_route)
    #sum= sum+len(nodes_route)-2
    #print(sum,"\n\n")
    sequence_nodes.append(nodes_route)



    for j in range(len(nodes_route) - 1):
      u = nodes_route[j]
      v = nodes_route[j + 1]

      seg = nx.astar_path(G, u, v, weight='length', heuristic=lambda u, v: ox.distance.euclidean(G.nodes[u]['y'], G.nodes[u]['x'],G.nodes[v]['y'], G.nodes[v]['x']))

      if j == 0:
        full_route.extend(seg)
      else:
        full_route.extend(seg[1:])

      if(len(full_route)>2):

        for k in range(len(seg) - 1):
          a = seg[k]
          b = seg[k + 1]

          edge_data = G.get_edge_data(a, b)

          edge = list(edge_data.values())[0]
          total_travel_time[i - 1] += edge.get("travel_time", 0)
          total_distance[i - 1] += (edge.get("length", 0))/1000

    all_routes.append(full_route)
#print(total_distance)



  #call the travelling salesman aprox needs: nodes, distances
  #inside new func:

routes_colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'orangered']

#============================= Assigning colors and sizes =========================================
#====================  ==================================
node_attr = {item[0]: item[1] for item in all_nodes}
node_colors = []
node_sizes =[]
collec = 10
Hq = 25
#====================  ==================================
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

#==================================== Plot Map =======================================================

fig, ax = ox.plot_graph(G, show=False, close=False, node_size = node_sizes, node_color = node_colors)
#xlim = ax.get_xlim()
#ylim = ax.get_ylim()
#for i in range(1,5):
  #y_ = max_lon + (i*step_lon)
  #ax.axhline(y=y_, color="orange", linestyle="--", linewidth=2)
#x_mid =step_lat

#ax.axvline(x=x_mid, color="orange", linestyle="--", linewidth=2)


for i, route in enumerate(all_routes):
    fig2, ax = ox.plot_graph(G, show=False, close=False, node_size = node_sizes, node_color = node_colors)
    color = routes_colors[i % len(routes_colors)]
    ox.plot_graph_route(G, route, route_color=color, route_linewidth=3, node_size=0, ax=ax, show=False, close=False, node_color = node_colors)
    fig2.savefig(f"../images/map_route{i+1}.svg", dpi=150, bbox_inches="tight")

fig.savefig("../images/piedmont_map.svg", dpi=150, bbox_inches="tight")


