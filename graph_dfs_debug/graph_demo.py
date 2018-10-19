#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=8, num_edges=8, draw_components=True):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(num)
        print (graph.vertices)
    # Add random edges between vertices
    # for edge in range(num_edges):
    #     vertices = sample(graph.vertices.keys(), 2)
    #     if edge not in graph.vertices[0].edges:
    #         graph.add_edge(vertices[0].label, vertices[1].label)
    def randnode():
        index = random.randint(0, len(graph.vertices)-1)
        nodes = list(graph.vertices.keys())
        return nodes[index]
    for node in list(graph.vertices.keys()):
        graph.add_edge(node, randnode())

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
    else:
        main()
