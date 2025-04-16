### OBJECTIVE

  

The objective of this assignment is to implement algorithms using Python and NetworkX for the construction and manipulation of graph networks derived from real-world data from UFRN's Electrical and Computing Engineering grad program.

  
#### SECTION 1
For this first section, the data being analyzed is divided by year, from 2010 to 2025.

  

Something that was clear after analyzing the graph was that there is not enough data yet from 2025 to compare it to the other years.

  

In order to extract the number of nodes, edges, the density, and the average number of neighbors, the following methods were applied:

  

````python

nodes = G.number_of_nodes() # Total number of nodes (authors)

edges = G.number_of_edges() # Total number of edges (connections)

density = round(100 * nx.density(G), 2)

avg_neighbors = round((2*edges) / nodes, 2)

````

  

If we don't take the year 2025 into consideration, the densities of the graphs averaged 2.7%, with a low of 2.13% in 2019 and a high of 3.39% in 2012.

The number of nodes doubled from 2010 to 2024, going from 276 to 552, with a high of 605 in 2019. The increased number of nodes in 2019 may have negatively impacted the density of that year.

Both the number of edges and the average number of neighbors increased throughout these years, although at very different rates. The number of edges went from 1,227 in 2010 to 3,811 in 2024, with a high of 3,982 in 2022.

  

This data was organized in two graphs:

  

<div  align="center">

<img  src="image1.png"  alt="Graph Metrics Over Time"  width="45%"  />

<img  src="image2.png"  alt="Histogram of Density vs. Nodes"  width="45%"  />

</div>

  

*Worth noting that the vertical dashed lines on image1 represent the testing years. This periodic testing is aimed at evaluating the quality of the graduate school’s program.

Those testing years may be interpreted as shifting points, which create incentives — or not — to join the program.*

  

---

  
### SECTION 2
For the second section, the data was segmented by testing periods: 2010–2012, and then every four years until 2024.

  

With the objective of analyzing the data, four graphs were generated using the NetworkX and Matplotlib packages — one for each testing period.

The four graphs have the following properties:

  

1. The size of the nodes is proportional to the number of neighbors that node has.

2. The top 5 nodes (by number of neighbors) are highlighted in red.

3. The color of the edge is red if both of the nodes are permanent members of the program.

4. The size of the edge is proportional to the number of citations that edge (paper) has.

  

<div  align="center">

<img  src="image3.png"  alt="Graph 1"  width="45%"  />

<img  src="image4.png"  alt="Graph 2"  width="45%"  />

<br  />

<img  src="image5.png"  alt="Graph 3"  width="45%"  />

<img  src="image6.png"  alt="Graph 4"  width="45%"  />

</div>

  

This was more challenging — from trying to display the nodes properly without them bunching up too much, to figuring out how to read and translate their properties into formatting directives.

  

---

  

## LLM (ChatGPT)

  

The use of an LLM for this assignment was very helpful, mostly for formatting and debugging.

  

---

  

## REFERENCES

  

- [Coscia, Michele. *The Atlas for the Aspiring Network Scientist*](https://www.networkatlas.eu/)

- [NetworkX Documentation](https://networkx.org/documentation/stable/reference/index.html)
