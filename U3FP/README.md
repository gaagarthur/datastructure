
# ARTHUR GAAG  
## 20230087350  
  
## FINAL PROJECT
This final project will have two distinct but sequential parts. For the first part, two lists of nodes and edges, each with their respective attributes, as well as a Python notebook were provided so a complex network could be built. Real world data was used to model this network, but its attributes were stripped of most identifying information to reduce the chance of bias during the initial analysis.
For the second part of this project, a specialist in the field related to the subject of the complex network will provide insight into the scenario it represents. Armed with that knowledge, a new analysis will be conducted.

---
---
## PART ONE

### OBJECTIVE  
The objective for this part is to use [NetworkX](https://networkx.org/documentation/stable/index.html#) and [Gephi](https://gephi.org/) to calculate five different metrics for the network and then create five different graphs, each displaying a different metric. These metrics are: Degree Centrality, Closeness Centrality, Betweenness Centrality, Eigenvector Centrality, and the core of the network and its shell. Additionally, a version of the graph with identified communities will be deployed.

### GEPHI
[Gephi](https://gephi.org/) is an open source software used to manipulate and analyze graphs. It helps create visually appealing graphs through a graphical interface. Because it doesn't require any coding, it makes graph analysis more accessible across different fields.

### METRICS 
When ranking nodes it's tempting to use the degree of a node to decide its importance to the network. Although that strategy is sufficient in some cases, other times a different metric might be more telling.  
  
  #### Degree Centrality:
  - Conveys the same basic idea as degree, which is the number of direct connections a node has.
  - Difference is: that degree centrality normalizes this measurement by dividing it by the maximum possible degree (N-1).
   degree_centrality = $\frac{k}{N-1}$ ; k is the degree.
  #### Closeness Centrality:
   - Takes into account that even if a node is popular (has high degree), it may still be far from many others
   - Measures how close a node is, on average, to all other reachable nodes.
   - For every node it calculates the sum of the shortest distances from that node to every other reachable node, then 
   it divides the number of nodes (N) minus one by this sum.
    closeness_centrality = $\frac{N-1}{\sum_{j\neq i}^{}l_{ij}}$
  #### Betweenness Centrality:
  - A measure of how often a node appears on the shortest paths between pairs of other nodes.
  - Shows how much of a bridging role a node has. So if that node were to be removed, communication between parts of the graph would become significantly more difficult or even impossible. 
  - If the node is bridging large communities, it would have a higher betweenness, since for any communication happen between them it must go through the bridge. 
  
  #### Eigenvector Centrality:
  - Quality of the connection not just quantity. 
  - A node is considered important if it is connected to other important nodes
  
  #### K-core and its shell:
  - The K-core  is the largest subset which every node has at least K connections to other nodes in the K core.
  - The found by recursively removing nodes with less than K connections (k-core decomposition).
  - The k-shell is a subset that contain the nodes removed when decomposing the kcore into k+1core difference of core k-1 and core k. Can be interpreted as the protective layer for the  k-core
  


### GENERATING GRAPH

The files, [nodes]() and [edges] were provided along with a [python notebook]() to generate a .gexf file that could be opened on Gephi. Since there is no option on the software to generate the k-core and shell, which would be both needed in this project, a couple of changes were made to the original notebook, that resulted in the [main.py]().
#### The major changes were:
- Removed magical commands
- Calculated the k-core and its shell
- Calculated the number of neighbors
- Calculated closeness centrality
- Appended the three new attributes
- Removed plotting section

All of the modifications above as well as any other are stamped with a "MOD.:" comment on main.py.
After running main it resulted in the gexf file that was imported into Gephi.
### THE GRAPH GEPHI

When importing the graph the options **undirected** and **don't merge** were selected, because in the notebook
the the type of graph generated was a multigraph and it is undirected and may have multiple edges between a pair of nodes.
With the graph loaded on Gephi, the sizes of the nodes were changed to be proportional to the number of neighbors
each node has. Then a mixture of the layouts "contraction", "expansion", "ForceAtlas", "ForceAtlas 2","OpenOrd" and
"Noverlap" were used to shape the overall layout. With that done, in the statistics section the "modularity" option for
community detection was applied. The colors were changed based on the community and the with the help of the "SigmaExporter" plugin the graph was exported and later [DEPLOYED]().
#### Applying the metrics
The degree centrality, betweenness and eigenvector were all generated on the same statistics tab, only the closeness centrality that was previously calculated in python. Then the nodes were colored based on those metrics leading to the four graphs.

<div align="center">
<table>
  <tr>
    <td style="width: 300px; text-align: center;">
      <p style="margin: 0 0 5px 0; text-align: center;">Degree Centrality</p>
      <img src="images/degree.svg" alt="Image 1" style="width: 100%; height: auto;">
    </td>
    <td style="width: 300px; text-align: center;">
      <p style="margin: 0 0 5px 0; text-align: center;">Closeness Centrality</p>
      <img src="images/closeness.svg" alt="Image 2" style="width: 100%; height: auto;">
    </td>
  </tr>
</table>
</div>

<div style="display: flex; justify-content: center; gap: 2%;">
  <img src="images/betweenness.svg" alt="Image 3" style="width: 45%; height: auto;">
  <img src="images/eigenvector.svg" alt="Image 4" style="width: 45%; height: auto;">
</div> 