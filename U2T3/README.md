## ARTHUR GAAG - 20230087350

## OBJECTIVE

  

This assignment is divided into two main parts, the first one is to make modifications to a pre-existing [Jupyter notebook](original_notebook/kruskal_natal.ipynb) to extract points of interest (POI) in an OpenStreetMap (OSM) graph and calculate the minimum spanning tree (MST) using Kruskal's algorithm. The second part was to develop a prompt that could be given to Google's [NotebookLM](https://notebooklm.google) to create an AI generated podcast.

---

### Important Links 

- *Medium article*: [Practical usage of MST, Kruskal’s algorithm](https://medium.com/@arthurgaag/practical-usage-of-mst-kruskals-algorithm-da3f654c20b2)
- *AI podcast*(two listening options): [YouTube](https://youtu.be/MR5qWEbKJFg) or [NotebookLM](https://notebooklm.google.com/notebook/19be486b-038a-4e4c-98fc-18034fa0d84a/audio) 

---

# Part 1



## Original Notebook

The original notebook was copied over into two regular .py files, one called auxfuncs.py and other called main.py.
the auxfuncs file contains a function to convert osmnx multidigraph into a multigraph (directed graph into undirected).
And main.py contains the rest, which is compose of:

- Importing the graph of city
- Call function to convert graph type
- Get locations of POI
- Build a complete graph with the POI nodes
- Employ Kruskal's algorithm to find MST
- Plot MST acquired for better visualization

#### Modifications

The code in the notebook was minimally modified . Before each changed section, there is a "# MOD.:" comment that gives a brief idea of what was changed.

---

## Extra plot

To generate additional plots, another file was created. pics.py plots the city map by itself and the city with cyan dots representing the POI.

---
  
## Choosing POI

After some time reading over the documentation on OSM's wiki the POI chosen were power substations.

Why?

The electrical grid must be interconnected to be more robust and since the conducting materials used to make cables are quite expensive, finding a MST that would connect those stations would minimize the distance and reduce the cost.

---

## Results

This process was used to import a graph for Natal, RN, Brazil, find the energy substations within city bounds and find the MST.
At the end, the total length of this MST was 46.29 km. and the tree maps produced (from left to right) are the map of the city, city + POI, and city + POI + MST.

<div style="display: flex; justify-content: space-between;">
  <img src="images/natal.svg" alt="Natal, Rio Grande do Norte, Brazil" style="width: 32%; height: auto;">
  <img src="images/POI.svg" alt="energy substations in Natal" style="width: 32%; height: auto;">
  <img src="images/plot.svg" alt="MST for the substations" style="width: 32%; height: auto;">
</div>



---
# Part 2

### General view

For the creation of the AI generated podcast, a prompt was formulated with the desired characteristics for the podcast and then fed into Google's NotebookLM.

### Prompt

The process of creating the prompt was simple, with a basic [outline of the criteria](images/outline.jpg), the first draft was written. To clean up the ideas and directions, this draft was passed through ChatGPT GPT-4o for critique. This refining process led to the final version.

```
Prompt:

Create a podcast in the style of an informal, yet informative interview.
The episode should be based entirely on the contents of the Medium article provided (pdf).
Tone: Conversational, curious, and hopeful not too serious, but still educational.

Format: The podcast must feature a dialogue between four different speakers. It should feel like a natural group conversation, people asking questions, sharing ideas, and clarifying points for each other.
Required Structure:
Introduction: Briefly introduce the four participants (can be all hosts or a mix of hosts and guests). Include names, roles, and a quick summary of what the episode will cover.
Problem Statement: What is the main problem or question being tackled in the article?
Key Concepts: Explain graph theory, the Minimum Spanning Tree (MST), and Kruskal’s Algorithm. Keep it accessible, use analogies or examples when needed so that non experts can understand.
Discussion: Have the participants explore the implications, ask each other clarifying questions, or relate the topic to real-world scenarios.
Conclusion: Wrap up by reflecting on the possible impacts or future applications of the topic. End on a hopeful note.

```

### NotebookLM

This NotebookLM is an AI powered tool developed by Google. It is capable of analysing sources and with the knowledge acquired, create different types of media from reading material, presentations, study guides and even natural sounding audio, which is the focus of this section.

The prompt was given to NotebookLM along side the [medium article](https://medium.com/@arthurgaag/practical-usage-of-mst-kruskals-algorithm-da3f654c20b2),as a PDF file, written about the Part 1.



---

## Usage of AI

OpenAI's LLM ChatGPT was used mostly for formatting and refining the prompt. Google's NotebookLM was also used, but to generate the podcast on Part 2.
 
---

