#!/usr/bin/env python

from typing import List, Tuple, Dict, Set, TypeVar, Any, Optional, Iterable
from collections import defaultdict
from dungeon_lib import roomGraph2 as roomGraph
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

class Stack:
    def __init__(self):
        self.stack: List[A] = list()

    def push(self, a: A):
        self.stack.append(a)

    def pop(self) -> A:
        if self.size > 0:
            return self.stack.pop()
        else:
            return None

    @property
    def size(self):
        return len(self.stack)

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

class BaseGraph:
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

    def get_neighbors(self, head: int) -> Iterable[Edge]:
        """ given a node get its neighbors """
        return (e for e in self.edges if e.head==head)

    def get_label(self, head: int, tail: int) -> Optional[str]:
        """ given a head and a tail, return either the label of the edge between them or none"""
        neighbors = self.get_neighbors(head)
        edge = None
        for e in neighbors:
            if e.tail==tail:
                edge = e
                break
        if edge:
            return edge.label
        else:
            return None

class Walker(BaseGraph):
    def __init__(self) -> None:
        super().__init__()

    def walk(self, starting_vertex: int) -> List[int]:
        """ hacked together combination of bft and dft
           to walk through a maze, sometimes you have to walk backwards.
        """
        traversals: Dict[Tuple[int, int], List[int]] = dict() #['n', 's']

        traversal: List[int] = list() # [starting_vertex]

        visited_rooms: Set[int] = set()

        qq = Queue()

        ss = Stack()

        ss.push(starting_vertex)
        qq.enqueue(starting_vertex)
        while len(self.vertices) > len(visited_rooms):
            #print("hi")
            while ss.size > 0:
                vertex = ss.pop()

                #traversal.append(vertex)
                if not vertex in visited_rooms:
                    visited_rooms.add(vertex)
                    traversal.append(vertex)

                    for edge in self.get_neighbors(vertex):
                        ss.push(edge.tail)

                        # dead end logic
                        tail_neighbs = list(self.get_neighbors(edge.tail))
                        if len(tail_neighbs)==1:
                            assert vertex == tail_neighbs[0].tail
                            traversal.append(edge.tail)
                            traversal.append(vertex)
                            break
                        
            while qq.size > 0:
                vertex = qq.dequeue()

                if not vertex in visited_rooms:
                    visited_rooms.add(vertex)

                    for edge in self.get_neighbors(vertex):
                        qq.enqueue(edge.tail)
                        tail_neighbs = list(self.get_neighbors(edge.tail))
                        if len(tail_neighbs)==1:
                            assert vertex == tail_neighbs[0].tail
                            traversal.append(edge.tail)
                            traversal.append(vertex)
                           

#                tail_neighbs = list(self.get_neighbors(edge.tail))
#                   if len(tail_neighbs)==1:
#                       assert vertex == tail_neighbs[0].tail
#                       traversal.append(vertex)


#       ss.push([starting_vertex])
#
#       while ss.size > 0:
#           path: List[int] = ss.pop()
#           vertex: int = path[-1]
#
#           if not vertex in visited_rooms:
#
#               visited_rooms.add(vertex)
#               traversal.append(vertex)
#
#               e = next(self.get_neighbors(vertex))
#               print(e)
#               for edge in self.get_neighbors(vertex):
#                   #print(edge)
#                   # if vertex (head) is the only thing in the neighbors of tail
#
#                   path_copy = path.copy()
#                   path_copy.append(edge.tail)
#                   if (starting_vertex, edge.tail) not in traversals.keys():
#                       traversals[(starting_vertex, edge.tail)] = path_copy
#                   ss.push(path_copy)
#
#                   tail_neighbs = list(self.get_neighbors(edge.tail))
#                   if len(tail_neighbs)==1:
#                       assert vertex == tail_neighbs[0].tail
#                       traversal.append(vertex)
#

        return traversal

    def walk_by_labels(self, traversal: List[int]) -> List[str]:
        """ given a list of integers representing a path through the graph
           get edge labels that correspond to that path
        """
        pass
   
def load_graph(room_graph: Dict[int, List[Any]]) -> Walker:
    """ load vertices and labeled edges into a graph """
    graph = Walker()
    rooms = dict()
    for key, value in room_graph.items():
        coords = value[0]
        adj = value[1].items()
        rooms[key] = adj
        graph.add_vertex(key)

    for tail, labels_heads in rooms.items():
        for label, head in labels_heads:
            graph.add_edge(tail, label, head)

    return graph

# test
if __name__=='__main__':

    graph = load_graph(roomGraph)
    #print(graph.edges)
    #print()
    print()
    traversal = graph.walk(0)
    #print(traversals)
    #print(max(len(path) for key, path in traversals.items()))
    print(traversal)
    #print(roomGraph)
    print()
