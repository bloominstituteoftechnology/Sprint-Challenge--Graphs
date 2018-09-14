#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=8, num_edges=4, draw_components=True):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num)))

    # Add random edges between vertices
    edges = set()
    while len(edges) < num_edges:
        vertices = sample(graph.vertices.keys(), 2)
        if (vertices[1], vertices[0]) not in edges:
            edges.add((vertices[0], vertices[1]))
            graph.add_edge(vertices[0], vertices[1])

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
