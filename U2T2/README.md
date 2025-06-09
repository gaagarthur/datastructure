# ARTHUR GAAG  
## 20230087350  
  
## OBJECTIVE  
The objective for this assignment is to use route mapping algorithms such as  A* and Dijkstra to plan the best route for field agents to reach collection points of aedes aegypti egg traps (Ovitraps). These traps that were strategically placed throughout the city of Natal RN, and  are used to monitor the movement patterns of the mosquito. 
  
### DETAILS 
  
The collection points for the Ovitraps and the headquarters  for the organization in charge are represented in the map below. In total there are ten field agents available to go collect the traps and 65 locations to visit.
Some requirements are:
- Visit every point of collection
- Every agent must start and end at the headquarters
- Must minimize the total distances
- Must use the A* and Dijkstra's algorithms to calculate the routes. 

<div style="text-align: center;">
  <img src="images/piedmont_map.svg" alt="Centered Image" style="max-width: 60%; height: auto;">
</div>

### Section 1

The first challenge of this assignment was to decide which locations would be assigned to each agent. For that the map was divided into 10 sectors, and each agent would be responsible for one of them. This did cause at least one of the sectors to not have any collection points within its bounds, but maybe more stations can be added later on.

#### How:
After importing the database containing the coordinates for the collection points, the data was iterated over to find the extreme stations. 
With that done, the map was then divided into left and right and into five horizontal segments, with a total of 10 spaces. Whatever many collection station fell into one section they were assigned to the same agent. the map division be seen on the picture below. 

<div style="text-align: center;">
  <img src="images/t.svg" alt="Centered Image" style="max-width: 60%; height: auto;">
</div>

### Section 2

With the delegation of the stations done, now were used the Dijkstra and A* algorithms to find/estimate the distances between every node in each section.

With the arrays of distances we had to find the best sequence of nodes, which is basically the travelling salesman problem. The Networkx offers a great approximation to solve this problem.

And finally, with the sequence of nodes we can use the A* algorithm, and both Dijkstra's algorithms to find the best path between the nodes. these 3 resulted in the following paths.
| A* | Dijkstra miniheap | Dijkstra classic | 
|---|---|---|

<div style="display: flex; justify-content: space-between;">
  <img src="image1.png" alt="images/map_routeAstar" style="width: 32%; height: auto;">
  <img src="image2.png" alt="images/map_routeDijk" style="width: 32%; height: auto;">
  <img src="image3.png" alt="images/map_routeDijkClass" style="width: 32%; height: auto;">
</div>
*the routes came out all the same color, will resolve it later.

### Data found

| A* | Dijkstra miniheap | Dijkstra classic | 
|---|---|---|


### Conclusion
The paths between A* and Dijkstra algorithms were not really much different. 

### IA
ChatGPT used mainly for for explaining concepts, debugging and formatting.