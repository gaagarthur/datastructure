import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from auxfuncs import to_undirected_multigraph

# ============================================
# 1. Obter o grafo da cidade de Natal
# ============================================
place = "Natal, Rio Grande do Norte, Brazil"
G = ox.graph_from_place(place, network_type='drive')

# MOD.: add missing bridge path at city limits-------------------------
bridge =(-5.781578, -35.247751)
G_bridge = ox.graph_from_point(bridge, dist=800, network_type="drive")
G = nx.compose(G, G_bridge)
#----------------------------------------------------------------------


# Converte para não-direcionado mantendo o tipo MultiGraph
G_undirected = to_undirected_multigraph(G)


# ============================================
# 2. Obter POIs de interesse (hospitais como exemplo)
# ============================================
# Mod.: Change "amenity" "hospital" to "power" "substation"
tags = {'power': 'substation'}
pois = ox.features.features_from_place(place, tags=tags)
#print(f"Number of POIs found: {len(pois)}")

# Extrair pontos representativos (centroides se for polígono)

# Mod.: "hospital" changed to "substation"

substation_points = []
for idx, row in pois.iterrows():
    if row.geometry.geom_type == 'Point':
        substation_points.append((row.geometry.y, row.geometry.x))
    else:
        substation_points.append((row.geometry.centroid.y, row.geometry.centroid.x))

if not substation_points:
    print("Nenhuma substacao encontrada. Tentando escolas...")
    tags = {'amenity': 'school'}
    pois = ox.features.features_from_place(place, tags=tags)
    for idx, row in pois.iterrows():
        if row.geometry.geom_type == 'Point':
            substation_points.append((row.geometry.y, row.geometry.x))
        else:
            substation_points.append((row.geometry.centroid.y, row.geometry.centroid.x))
    if not substation_points:
        raise ValueError("Nenhum POI encontrado para as categorias tentadas.")



# ============================================
# 3. Encontrar nós mais próximos dos POIs
# ============================================

# Mod.: "hospital" changed to "substation"

latitudes = [hp[0] for hp in substation_points]
longitudes = [hp[1] for hp in substation_points]
substation_nodes = ox.distance.nearest_nodes(G_undirected, X=longitudes, Y=latitudes)
substation_nodes = list(set(substation_nodes))

if len(substation_nodes) < 2:
    raise ValueError("POIs insuficientes para criar um MST (menos de 2 pontos).")


# ============================================
# 4. Construir um grafo completo com menor rota entre POIs
# ============================================

# Mod.: "hospital" changed to "substation"

G_interest = nx.Graph()
for i in range(len(substation_nodes)):
    for j in range(i+1, len(substation_nodes)):
        route = nx.shortest_path(G_undirected, substation_nodes[i], substation_nodes[j], weight='length')
        route_length = 0
        for k in range(len(route)-1):
            route_length += G_undirected[route[k]][route[k+1]][0]['length']  # Como é MultiGraph, usar [0]
        G_interest.add_edge(substation_nodes[i], substation_nodes[j], weight=route_length)



# ============================================
# 5. Calcular o MST
# ============================================
mst_edges = list(nx.minimum_spanning_edges(G_interest, data=True))
total_mst_length = sum([d['weight'] for (u, v, d) in mst_edges])
print("Comprimento total do MST entre os POIs selecionados:", total_mst_length, "metros")

mst_routes = []
for (u, v, d) in mst_edges:
    route = nx.shortest_path(G_undirected, u, v, weight='length')
    mst_routes.append(route)


#==========
# plot
#==========

# Mod.: "hospital" changed to "substation"

# Plotar o grafo base
fig, ax = ox.plot_graph(
    G_undirected, node_size=0, edge_color="gray", edge_linewidth=0.5, show=False, close=False
)

# Destacar as rotas do MST em vermelho
for route in mst_routes:
    x = [G_undirected.nodes[n]['x'] for n in route]
    y = [G_undirected.nodes[n]['y'] for n in route]
    ax.plot(x, y, color='red', linewidth=2, zorder=4)

# Plotar também os POIs (hospitais) em azul
poi_x = [G_undirected.nodes[n]['x'] for n in substation_nodes]
poi_y = [G_undirected.nodes[n]['y'] for n in substation_nodes]
ax.scatter(poi_x, poi_y, c='cyan', s=80, zorder=5, edgecolor='black')

plt.title("MST for POIs (Substations) in Natal, RN, Brazil", fontsize=12)
plt.savefig('images/plot.svg')
