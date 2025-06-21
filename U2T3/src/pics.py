import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

place = "Natal, Rio Grande do Norte, Brazil"

G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")

bridge =(-5.781578, -35.247751)
G_bridge = ox.graph_from_point(bridge, dist=800, network_type="drive")
G = nx.compose(G, G_bridge)

fig, ax = ox.plot_graph(
    G, node_size=0, edge_color="gray", edge_linewidth=0.5, show=False, close=False
)
plt.savefig("images/natal.svg")

tags = {'power': 'substation'}
pois = ox.features.features_from_place(place, tags=tags)


substation_points = []
for idx, row in pois.iterrows():
    if row.geometry.geom_type == 'Point':
        substation_points.append((row.geometry.y, row.geometry.x))
    else:
        substation_points.append((row.geometry.centroid.y, row.geometry.centroid.x))

latitudes = [hp[0] for hp in substation_points]
longitudes = [hp[1] for hp in substation_points]
substation_nodes = ox.distance.nearest_nodes(G, X=longitudes, Y=latitudes)
substation_nodes = list(set(substation_nodes))

fig, ax = ox.plot_graph(
    G, node_size=0, edge_color="gray", edge_linewidth=0.5, show=False, close=False
)

poi_x = [G.nodes[n]['x'] for n in substation_nodes]
poi_y = [G.nodes[n]['y'] for n in substation_nodes]
ax.scatter(poi_x, poi_y, c='cyan', s=80, zorder=5, edgecolor='black')

plt.savefig("images/POI.svg")