#!/usr/bin/env python
from typing import List, Tuple, Dict, Set, TypeVar, Any, Optional, Iterable, Union
from dungeon_lib import roomGraph4 as roomGraph
AdjSet = Dict[int, Set[Tuple[str, int]]]
# InpSet = Dict[int, List[Union[Tuple[int, int], Dict[str, int]]]]
from datastructures import Stack, Queue

def load_graph(room_graph: Dict[int, List[Any]]) -> AdjSet:
    """ load vertices and labeled edges into a graph """
    rooms = dict()
    for key, value in room_graph.items():
        coords = value[0]
        adj = value[1].items()
        rooms[key] = set(adj)

    return rooms

def walk(room_graph: AdjSet, starting_vertex) -> List[str]:
    """ keep in mind the real adjacency
       set is [x[1] for x in vertices[v]] where x[0] is
           reserved as label """
    walk: List[int] = list()
    walk_moves: List[str] = list()

    visited: Set[int] = set()

    ss: Stack = Stack()
    ss.push(starting_vertex)

    REVERSE = {'n': 's', 'e': 'w'}



    while ss.size>0:
        vertex: int = ss.pop()
        if vertex not in visited:
            visited.add(vertex)
            walk.append(vertex)


            for neigh_dir, neigh_id in room_graph[vertex]:

                dead_end_: Stack = Stack()
                dead_end: Queue = Queue()
                dead_end.enqueue(neigh_id)
                dead_end_.push(neigh_id)

                walk_moves.append(neigh_dir)
                walk.append(neigh_id)

                ss.push(neigh_id)

                if len(room_graph[neigh_id])==1:
                    while dead_end_.size > 0:
                        walk.append(dead_end_.pop())

    return walk # , walk_moves


# test
if __name__=='__main__':
    graph = load_graph(roomGraph)
    #print()
    print(graph)
    #print(roomGraph)
    print()
    print(walk(graph, 0))
