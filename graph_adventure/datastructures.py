#!/usr/bin/env python

from typing import List, Tuple, Dict, Set, TypeVar, Any, Optional
from collections import defaultdict
from dungeon_lib import roomGraph5 as roomGraph
A = TypeVar('A')

class Queue:
    def __init__(self):
        self.queue: List[A] = list()

    def enqueue(self, a: A):
        self.queue.append(a)

    def dequeue(self) -> Optional[A]:
        if self.size > 0:
            rtrn: A = self.queue.pop(0)
            return rtrn
        else:
            return None

    @property
    def size(self):
        return len(self.queue)

#lass Node:
#   def __init__(self, id: int):
#       self.id: int = id
#
#   def __repr__(self) -> str:
#       return f"Node: {self.id}"
#
#   def __str__(self) -> str:
#       return f"{self.id}"
    
class Edge:
    def __init__(self, tail: int, label: str, head: int) -> None:
        self.tail: int = tail
        assert label in ('n', 's', 'e', 'w')
        self.label: str = label
        self.head: int = head
        return None

    def __repr__(self) -> str:
        return f"Edge: {self.tail}={self.label}=>{self.head}"

    def __str__(self) -> str:
        return f"{self.tail}={self.label}=>{self.head}"

class Graph:
    """ an edge-labeled, directed graph. """
    def __init__(self) -> None:
        self.vertices: Set[int] = set()
        self.edges: Set[Edge] = set()

    def add_vertex(self, v: int):
        if v not in self.vertices:
            self.vertices.add(v)
        else:
            pass

    def add_edge(self, tail: int, label: str, head: int):

        if tail in self.vertices and head in self.vertices:
            self.edges.add(Edge(tail, label, head))
        else:
            raise Exception("Please verify that vertices are being added.")

   
    def traverse(self, starting_vertex: int) -> List[str]:
        traversal = ['n', 's']

        visited_rooms = set()

        qq = Queue()


        qq.enqueue(starting_vertex)

        while qq.size > 0:
            vertex = qq.dequeue()

            if not vertex in visited_rooms:

                visited_rooms.add(vertex)

                #traversal.append(vertex)

                for edge in (e for e in self.edges if e.head==vertex):
                    qq.enqueue(edge.tail)
                    traversal.append(edge.label)

        return traversal
# test
#f __name__=='__main__':
#
#   graph = Graph()
#   room_graph = dict()
#   for key, value in roomGraph.items():
#       coords = value[0]
#       adj = value[1].items()
#       room_graph[key] = adj
#       graph.add_vertex(key)
#
#   for tail, labels_heads in room_graph.items():
#       for label, head in labels_heads:
#           graph.add_edge(tail, label, head)
#
#   #print(graph.edges)
#   #print()
#   print()
#   print(len(graph.traverse(0)))
#   #print(roomGraph)
#   print()
#
