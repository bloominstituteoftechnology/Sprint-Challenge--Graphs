#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex
import random

def main(num_vertices=8, num_edges=8, draw_components=True):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    all_edges = []

    for num1 in range(num_vertices):
        for num2 in range(num1 + 1, num_vertices):
            all_edges.append((num1, num2))
            # print(all_edges)

    # Add random edges between vertices
    random.shuffle(all_edges)
    edges = all_edges[:num_edges - 2]

    if num_edges > len(all_edges):
        print("Too many edges")
    print(all_edges)

    for num in range(num_vertices):
        graph.add_vertex(num)

    for edge in edges:
        # print(edge)
        graph.add_edge(edge[0], edge[1])
    print(len(edges))


    # for _ in range(num_edges):
    #     vertices = sample(graph.vertices.keys(), 2)
    #     # TODO check if edge already exists
        
    #     graph.add_edge(vertices[0], vertices[1])

    # bg = BokehGraph(graph)
    # bg._setup_graph_renderer()

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    # bokeh_graph._setup_graph_renderer("1")
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
    else:
        main()
# """
# Demonstration of Graph and BokehGraph functionality.
# """

# from random import sample
# from sys import argv
# from draw import BokehGraph
# from graph import Graph, Vertex


# def main(num_vertices=8, num_edges=8, draw_components=True):
#     """Build and show random graph."""
#     graph = Graph()
#     # Add appropriate number of vertices
#     for num in range(num_vertices):
#         graph.add_vertex(Vertex(label=str(num)))

#     # Add random edges between vertices
#     for _ in range(num_edges):
#         vertices = sample(graph.vertices.keys(), 2)
#         # TODO check if edge already exists
#         graph.add_edge(vertices[0], vertices[1])

#     bokeh_graph = BokehGraph(graph, draw_components=draw_components)
#     bokeh_graph.show()


# if __name__ == '__main__':
#     if len(argv) == 4:
#         NUM_VERTICES = int(argv[1])
#         NUM_EDGES = int(argv[2])
#         DRAW_COMPONENTS = bool(int(argv[3]))
#         main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
#     else:
#         main()