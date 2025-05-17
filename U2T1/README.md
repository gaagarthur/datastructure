
# ARTHUR GAAG  
## 20230087350  
  
## OBJECTIVE  
the objective for this assignment is to compare the shortest paths algorithms (SPAs), the one native to OSMnx, Dijkstra(O(n^2)) and Dijkstra implemented with a min-heap.  
In order to do that I chose the first scenario proposed by the professor. the scenario was to, applying the SAPs, find the shortest routes from a large public hospital (Mosenhor Walfredo Gurgel) to different neighborhoods in the city.  
  
## DATA THROUGH LLM  
  
In order to get a list of neighborhoods, in the city of Natal, for this project, the LLM ChatGPT was used with the following prompt (Prompt 1).  

````
(Prompt 1) 
Give me a list of the neighborhoods in the city of Natal RN Brazil, except Tirol.  
The list must contain seven neighborhoods from the south region, three from  
the east side, one from the west side, and one from the north region.  
Important: the return list must contain the names of the neighborhoods selected  
(twelve in total), each one between quotation marks, and separated by a comma.  
  
````  
  
This resulted in a list that contain the neighborhoods:  
- Lagoa Nova  
- Candelaria  
- Capim Macio  
- Neopolis  
- Nova Descoberta  
- Pitimbu  
- Ponta Negra  
- Petropolis  
- Alecrim  
- Mae Luiza  
- Quintas  
- Redinha  
  
## DATA FROM OPEN SOURCE MAP  
  
The graph that represents Natal's road system, which is used to compare the performance of the algorithms was imported from OpenSourceMap (OSM) with the OSMnx library in python. After the road system was imported and the graph G was created, the node in G that best represents the location of the hospital Mosenhor Walfredo Gurgel was assigned to "node_walfredo_gurgel" through a two step process. First step was to obtain the coordinates of the hospital, then, the longitude and latitude were passed as parameters to a osmnx function. At last, the node that best fits with the coordinates of the neighborhoods was assigned to "target_node" the same way that was done with the hospital's node, only difference is that this process was done inside a for loop so the code would have to iterate through the neighborhood list only once.  
  
#### The code from previous explanation:  
  
````python  
import osmnx as ox  
. . .  
#import the map of the roads of Natal RN, and turn into graph.  
G = ox.graph_from_place("Natal, RN, Brazil", network_type="drive")  
  
#Get coordinates of hospital.  
walfredo_gurgel = (ox.geocode("Complexo Hospitalar Mosenhor Walfredo Gurgel, natal RN, Brazil"))  
  
#find the nearest node to the coordinate.  
node_walfredo_gurgel = ox.distance.nearest_nodes(G,walfredo_gurgel[1],walfredo_gurgel[0])  
  
#Get coordinates of neighborhood -> find the nearest node to the coordinate.  
for nh in neighborhoods:  
taget = (ox.geocode(f"{nh}, natal, RN, Brazil"))  
taget_node = ox.distance.nearest_nodes(G,taget[1],taget[0])  
. . .  
````  
When importing the map from OSM, the way was done, the edge list represents drivable roads. This list comes with a couple of attributes already, but to facilitate later, the speed and travel times were added as edge attributes.  
  
  
## FINDING THE SHORTEST PATH  
  
As mentioned in the objective, three methods of finding the shortest path between two nodes were to be used:  
  
The first one was the Dijkstra's algorithm implemented with a min heap (priority queue), Networkx implements it in the "shortest_path" function,  
all that had to be done was, call the function making sure to pass the graph , starting node, target node, method of comparison, and method of search as parameters.

The second method used was the classic Dijkstra shortest path algorithm, which has a time complexity of $O(n^2)$. Because of the how inefficient the classic algorithm is, compared to the one implemented with a priority queue, it is not built in to networkx. Since the main objective was to use and compare the different algorithms, the LLM ChatGPT was used to implement a classic ( $O(n^2)$ ) that would take the same parameters given to Networkx's "shortest_path()", minus the method of search (prompt 2).

````

In python, implement the classic Dijkstra shortest path algorithm (the one with a time complexity O(n^2)). 
This implementation must recieve as parameters (G, source_node, target_node, weight="length"), where:

G : is a networkx mutidigraph graph.
source_node : is the starting node for the search.
target_node : is the destination (last) node of the search.
weight : is an edge atribute used to compare paths.

This implementation must return a list of nodes for the path found.

````