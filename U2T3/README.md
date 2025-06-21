## ARTHUR GAAG - 20230087350

## OBJECTIVE

  

This assignment is divided in two main parts, the first one is to make modifications to a pre-existing [jupyter notebook]() to extract points of interenst (POI) in a OpenStreetMap (OSM) graph and calculate and find the minimum spanning tree (MST) using Kruskal's algorithm. The second part was to develop a prompt that could be given to google's [Notebooklm]() to create an AI generated podcast.

---

## Original Notebook

The original notebook was copied over into two regular .py files, one called auxfuncs.py and other called main.py.
the auxfuncs file contains a function to convert osmnx multidigraph into a multigraph (directed graph into undirected).
And the main has the rest, which is compose of:

- Importing the graph of city
- Call function to convert type of graph
- Get locations POI
- Build a complete graph with the POI nodes
- Employ the Kruskal's algorithms to find MST
- Plot MST acquired for better visualization

#### Modifications

The code in the notebook was minimaly modifyed. Before every section changed there is a "# MOD.:" comment that gives a brief idea of what was changed.

---

## Extra plot

To get other plots anoter file was created. pics.py plots the map of the city by itself and the city with cyan dots that represent the POI.

---
  
## Choosing POI

After some time reading over the documentations on OSM's wiki the POI choosen were power substations.

Why?

The electrical grid must be interconnected to be more robust and since the conducting materials used to make cables are quite expensive, finding a MST that would connect those stations would minimize the distance and reduce the cost.

---

## Results

This process were used to import a graph for natal RN Brazil, find the energy substations withing citybounds and find the MST.
at the end the total length of this MST was 46.29 Km. and the tree maps produced (from left to right) are the map of the city, city + POI, and city + POI + MST.

<div style="display: flex; justify-content: space-between;">
  <img src="images/natal.svg" alt="Natal, Rio Grande do Norte, Brazil" style="width: 32%; height: auto;">
  <img src="images/POI.svg" alt="energy substations in Natal" style="width: 32%; height: auto;">
  <img src="images/plot.svg" alt="MST for the substations" style="width: 32%; height: auto;">
</div>



---

  

## LLM (ChatGPT)
 

The use of an LLM for this assignment was used mostly for formatting.

  
---


## REFERENCES

  

- [Coscia, Michele. *The Atlas for the Aspiring Network Scientist*](https://www.networkatlas.eu/)

- [NetworkX Documentation](https://networkx.org/documentation/stable/reference/index.html)
