#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=8, num_edges=8, draw_components=True):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num), component=num))

    # Add random edges between vertices
    edges = set()
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # set vertices_id to a concatenated string of ints from vertices
        vertices_id = str(vertices[0])[-1] + str(vertices[1])[-1]
        if vertices_id not in edges:
            graph.add_edge(vertices[0], vertices[1])
            edges.add(vertices_id)

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        if NUM_EDGES > (NUM_VERTICES * (NUM_VERTICES - 1))/2:
            # bidirectional limit: n*(n-1)/2, else n^2
            print('Too many edges. Choose a lower number')
        else:
            main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
    elif len(argv) == 1:
        main()
    else:
        print('Expected arguments: Vertices(int) Edges(int) Draw_Components(0/1)')
