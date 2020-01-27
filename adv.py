from room import Room
from player import Player
from world import World
from stack import Stack
from queue import Queue
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

traversal_graph = Graph()

# print(traversal_graph.bft(world.starting_room))

def dft_rec(room, traveled, visited = None):
  if visited is None:
    visited = Graph()
  visited.add_vertex(room.id)

  check = room.get_exits()
  check2 = visited.get_neighbors(room.id)
  check3 = []
  for n in check2:
    check3.append(visited.get_neighbors(n))
  
  if len(visited.vertices) == len(room_graph):
    return traveled
  
  if room.n_to is not None and room.n_to.id not in visited.vertices:
    traveled.append('n')
    visited.add_vertex(room.n_to.id)
    visited.add_edge(room.id, room.n_to.id)
    dft_rec(room.n_to, traveled, visited)
  if room.e_to is not None and room.e_to.id not in visited.vertices:
    traveled.append('e')
    visited.add_vertex(room.e_to.id)
    visited.add_edge(room.id, room.e_to.id)
    dft_rec(room.e_to, traveled, visited)
  if room.s_to is not None and room.s_to.id not in visited.vertices:
    traveled.append('s')
    visited.add_vertex(room.s_to.id)
    visited.add_edge(room.id, room.s_to.id)
    dft_rec(room.s_to, traveled, visited)
  if room.w_to is not None and room.w_to.id not in visited.vertices:
    traveled.append('w')
    visited.add_vertex(room.w_to.id)
    visited.add_edge(room.id, room.w_to.id)
    dft_rec(room.w_to, traveled, visited)
  
  if len(visited.vertices) == len(room_graph):
    return traveled
  
  if len(check) == 1:
    traveled.append(check[0])
    if 'n' in check[0]:
      visited.add_edge(room.id, room.n_to.id)
      dft_rec(room.n_to, traveled, visited)
    if 's' in check[0]:
      visited.add_edge(room.id, room.s_to.id)
      dft_rec(room.s_to, traveled, visited)
    if 'e' in check[0]:
      visited.add_edge(room.id, room.e_to.id)
      dft_rec(room.e_to, traveled, visited)
    if 'w' in check[0]:
      visited.add_edge(room.id, room.w_to.id)
      dft_rec(room.w_to, traveled, visited)
  
  if len(visited.vertices) == len(room_graph):
    return traveled

  if len(check3) > 0:
    if len(check) == 3 and check2 != set() and room.id not in check3[0]:
      if room.n_to is not None:
        if room.n_to.id in check2:
          destination = room.n_to
          if destination.n_to is not None:
            if len(visited.get_neighbors(destination.n_to.id)) < len(destination.n_to.get_exits()):
              arrival = destination.n_to
              traveled.append('n')
              traveled.append('n')
              dft_rec(arrival, traveled, visited)
          elif destination.e_to is not None:
            if len(visited.get_neighbors(destination.e_to.id)) < len(destination.e_to.get_exits()):
              arrival = destination.e_to
              traveled.append('n')
              traveled.append('e')
              dft_rec(arrival, traveled, visited)
          elif destination.w_to is not None:
            if len(visited.get_neighbors(destination.w_to.id)) < len(destination.w_to.get_exits()):
              arrival = destination.w_to
              traveled.append('n')
              traveled.append('w')
              dft_rec(arrival, traveled, visited)
      elif room.e_to is not None:
        if room.e_to.id in check2:
          destination = room.e_to
          if destination.n_to is not None:
            if len(visited.get_neighbors(destination.n_to.id)) < len(destination.n_to.get_exits()):
              arrival = destination.n_to
              traveled.append('e')
              traveled.append('n')
              dft_rec(arrival, traveled, visited)
          if destination.e_to is not None:
            if len(visited.get_neighbors(destination.e_to.id)) < len(destination.e_to.get_exits()):
              arrival = destination.e_to
              traveled.append('e')
              traveled.append('e')
              dft_rec(arrival, traveled, visited)
          if destination.s_to is not None:
            if len(visited.get_neighbors(destination.s_to.id)) < len(destination.s_to.get_exits()):
              arrival = destination.s_to
              traveled.append('e')
              traveled.append('s')
              dft_rec(arrival, traveled, visited)
      elif room.s_to is not None:
        if room.s_to.id in check2:
          destination = room.s_to
          if destination.w_to is not None:
            if len(visited.get_neighbors(destination.w_to.id)) < len(destination.w_to.get_exits()):
              arrival = destination.w_to
              traveled.append('s')
              traveled.append('w')
              dft_rec(arrival, traveled, visited)
          if destination.e_to is not None:
            if len(visited.get_neighbors(destination.e_to.id)) < len(destination.e_to.get_exits()):
              arrival = destination.e_to
              traveled.append('s')
              traveled.append('e')
              dft_rec(arrival, traveled, visited)
          if destination.s_to is not None:
            if len(visited.get_neighbors(destination.s_to.id)) < len(destination.s_to.get_exits()):
              arrival = destination.s_to
              traveled.append('s')
              traveled.append('s')
              dft_rec(arrival, traveled, visited)
      elif room.w_to is not None:
        if room.w_to.id in check2:
          destination = room.w_to
          if destination.n_to is not None:
            if len(visited.get_neighbors(destination.n_to.id)) < len(destination.n_to.get_exits()):
              arrival = destination.n_to
              traveled.append('w')
              traveled.append('n')
              dft_rec(arrival, traveled, visited)
          if destination.w_to is not None:
            if len(visited.get_neighbors(destination.w_to.id)) < len(destination.w_to.get_exits()):
              arrival = destination.w_to
              traveled.append('w')
              traveled.append('w')
              dft_rec(arrival, traveled, visited)
          if destination.s_to is not None:
            if len(visited.get_neighbors(destination.s_to.id)) < len(destination.s_to.get_exits()):
              arrival = destination.s_to
              traveled.append('w')
              traveled.append('s')
              dft_rec(arrival, traveled, visited)
        
  if len(visited.vertices) == len(room_graph):
    return traveled

  if room.w_to is not None and room.w_to.id not in check2:
    traveled.append('w')
    visited.add_edge(room.id, room.w_to.id)
    dft_rec(room.w_to, traveled, visited)
  elif room.s_to is not None and room.s_to.id not in check2:
    traveled.append('s')
    visited.add_edge(room.id, room.s_to.id)
    dft_rec(room.s_to, traveled, visited)
  elif room.e_to is not None and room.e_to.id not in check2:
    traveled.append('e')
    visited.add_edge(room.id, room.e_to.id)
    dft_rec(room.e_to, traveled, visited)
  elif room.n_to is not None and room.n_to.id not in check2:
    traveled.append('n')
    visited.add_edge(room.id, room.n_to.id)
    dft_rec(room.n_to, traveled, visited)

def dft_recursive(room, traveled, visited = None, revisited = None, triple = None):
  if visited is None:
    visited = set()
  visited.add(room)
  if revisited is None:
    revisited = set()
  if triple is None:
    triple = set()
  print(room)
  if len(visited) == len(room_graph):
    return traveled
  if room.n_to is not None and room.n_to not in visited:
    traveled.append('n')
    dft_recursive(room.n_to, traveled, visited, revisited, triple)
  elif room.s_to is not None and room.s_to not in visited:
    traveled.append('s')
    dft_recursive(room.s_to, traveled, visited, revisited, triple)
  elif room.e_to is not None and room.e_to not in visited:
    traveled.append('e')
    dft_recursive(room.e_to, traveled, visited, revisited, triple)
  elif room.w_to is not None and room.w_to not in visited:
    traveled.append('w')
    dft_recursive(room.w_to, traveled, visited, revisited, triple)
  elif room.w_to is not None and room.w_to not in revisited:
    revisited.add(room)
    traveled.append('w')
    dft_recursive(room.w_to, traveled, visited, revisited, triple)
  elif room.e_to is not None and room.e_to not in revisited:
    revisited.add(room)
    traveled.append('e')
    dft_recursive(room.e_to, traveled, visited, revisited, triple)
  elif room.s_to is not None and room.s_to not in revisited:
    revisited.add(room)
    traveled.append('s')
    dft_recursive(room.s_to, traveled, visited, revisited, triple)
  elif room.n_to is not None and room.n_to not in revisited:
    revisited.add(room)
    traveled.append('n')
    dft_recursive(room.n_to, traveled, visited, revisited, triple)
  # triple causes an infinite loop

dft_rec(world.starting_room, traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
