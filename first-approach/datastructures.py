#!/usr/bin/env python

from typing import List, Tuple, Dict, Set, TypeVar, Any, Optional, Iterable
from collections import defaultdict
from dungeon_lib import roomGraph4 as roomGraph
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

    def pop(self) -> Optional[A]:
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

    def get_neighbors(self, tail: int) -> List[Edge]:
        """ given a node get its neighbors """
        return [e for e in self.edges if e.tail==tail]

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

    def bf_path(self, starting_vertex: int, destination_vertex: int) -> List[int]:
        """ returns the shortest path from a starting vertex to a destination vertex """
        traversals: Dict[Tuple[int, int], List[int]] = {(0,0): [0]}
        qq: Queue = Queue()
        visited_vertices: Set[int] = set()

        qq.enqueue([starting_vertex])
 
        while qq.size > 0:
            path: List[int] = qq.dequeue()
            vertex: int = path[-1]

            if vertex not in visited_vertices:
                visited_vertices.add(vertex)
                for edge in self.get_neighbors(vertex):
                    if edge.head not in visited_vertices:
                        path_copy = path.copy()
                        path_copy.append(edge.head)
                        traversals[(starting_vertex, edge.head)] = path_copy
                        qq.enqueue(path_copy)

        return traversals[(starting_vertex, destination_vertex)]
            

    def walk(self, starting_vertex: int) -> List[int]:
        """
        1. naive dft
        2. test for dead end: if dead end, do bf_path back to start
        3. continue from start, but maintaining visited_vertex list

        """
        traversal: List[int] = list()

        visited_vertices: Set[int] = set()

        ss: Stack = Stack()

        ss.push(starting_vertex)
        intermediary_root = starting_vertex
        while ss.size > 0:
            vertex: int = ss.pop()
            traversal.append(vertex)
            if vertex not in visited_vertices:
                visited_vertices.add(vertex)
                for edge in self.get_neighbors(vertex):
                    # print(edge.head)
                    if edge.head not in visited_vertices:

                        # deadend logic

                        neighbs = self.get_neighbors(edge.head)
                        unvisited_neighbs = [e for e in neighbs if e.head not in visited_vertices]
                        if len(unvisited_neighbs) > 1: # new "intermediary root"
                            intermediary_root = vertex
                        # dead-end
                        if len(unvisited_neighbs)==0: # then its a deadend
                            bf_path = self.bf_path(edge.head, intermediary_root)
                            traversal.extend(bf_path[:-1])
                            ss.push(intermediary_root)
                        else:
                            ss.push(edge.head)
                            # traversal.append(edge.head)
                            continue
                    else:
                        #traversal.extend(self.bf_path(starting_vertex, edge.head))
                        continue
            else:
                # ss.pop()
                continue
           
        return traversal


    def walk_by_edges(self, starting_vertex: int) -> List[int]:
        """ hacked together combination of bft and dft
           to walk through a maze, sometimes you have to walk backwards.

           mark edges as visited instead of nodes.
        """
        edge_traversal: List[Edge] = list()
        traversal: List[int] = list()
        moves: List[str] = list()

        visited_edges: Set[Edge] = set()

        init_edges = self.get_neighbors(starting_vertex)
        for edge in init_edges:
            ss = Stack()

            ss.push(edge)

            visited_edges.add(edge)
           
            while ss.size > 0:
                e: Edge = ss.pop()

                vertex: int = e.head

                traversal.append(vertex)

                edges = self.get_neighbors(vertex)

                for edge in edges:
                    if edge not in visited_edges:

                        ss.push(edge)
                        visited_edges.add(edge)
                        edge_traversal.append(edge)
                        traversal.append(edge.head)

        return edge_traversal, traversal

    def get_labels_from_walk(self, traversal: List[int]) -> List[str]:
        """ given a list of integers representing a path through the graph
           get edge labels that correspond to that path
        """
        path_by_moves = list()
        while traversal:
            first = traversal.pop(0)
            edges = self.get_neighbors(first)
            edge = [e for e in edges if e.tail==traversal[0]]
            assert len(edge)==1
            path_by_moves.append(edge[0].label)
        return path_by_moves

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
    print()
    # print(roomGraph)
    print()
    print(graph.edges)
    print([edge for edge in graph.edges if edge.head==8])
    #print()
    print()
    traversal = graph.walk(0)
    #print(traversals)
    #print(max(len(path) for key, path in traversals.items()))
    print(traversal)
    #print(roomGraph)
    print()
