from room import Room
from player import Player
from world import World
from foo import foo

import random
from ast import literal_eval
from collections import deque

# rooms2obj takes the world's rooms object and produces familiar
#    graph adjacency matrix
def rooms2obj(rms):
    ret_grph_work = {}
    ret_grph_vstd = {}

    # Iterate through rooms dict
    for k, rm in rms.items():
        # Initialize a room directive dict value
        tmp_wrk_dict = {
            "n": None,
            "s": None,
            "e": None,
            "w": None
        }
        tmp_vst_dict = {
            "n": True,
            "s": True,
            "e": True,
            "w": True
        }
        if rm.n_to != None:
            tmp_wrk_dict["n"] = rm.n_to.id
            tmp_vst_dict["n"] = False
        if rm.s_to != None:
            tmp_wrk_dict["s"] = rm.s_to.id
            tmp_vst_dict["s"] = False
        if rm.e_to != None:
            tmp_wrk_dict["e"] = rm.e_to.id
            tmp_vst_dict["e"] = False
        if rm.w_to != None:
            tmp_wrk_dict["w"] = rm.w_to.id
            tmp_vst_dict["w"] = False

        # Assign the room directive to the return graph 
        ret_grph_work[k] = tmp_wrk_dict
        ret_grph_vstd[k] = tmp_vst_dict

    # Done iterating - return the built graph
    return (ret_grph_work, ret_grph_vstd)

# gen_next_step takes a room and generates the next step to take in the 
#    traversal
def gen_next_step(nde):
    # inspect the directive dict for this room (in the working graph)
    nde_status  = graph_vst[nde]

    # Find a key (direction) that has not been inspected/visted
    for dr, vstd in nde_status.items():
        # has this node's direction been visited?
        if vstd:
            # yes, skip to another direction
            continue

        # Found a node direction not visited - return
        nde_drtv = graph_trv[nde]
        return (True, dr, nde_drtv[dr])  # (returned_next_step=True, directive, next_node)

    # Iteration complete: no step identified
    return (False, "", -999)             # (returned_next_step=False)

# gen_back_up_step takes a directive INTO a node and generates
#   the directive needed to step BACK OUT of the node (its inverse)
def gen_back_up_step(dir_in):
    tmp_dict = {
        "n": "s",
        "s": "n",
        "e": "w",
        "w": "e"
    }

    return tmp_dict[dir_in]

# trav_graph traverses a constructed graph object starting 
#   with the passed start node and returns traversed path
def trav_graph(grph, strt):

    # deep_dive traverses down a graph thread recursively
    def deep_dive(nde):

        # node_dive does a deep traversal from the passed node in a recursive manner
        def node_dive(nod):
            # Are we at the end of the dive (no children to traverse to)
            rslt_tup = gen_next_step(nod)
            if not rslt_tup[0]:
                # reached the end of the thread - return the current node
                path_trvse_id.append(nod)  # add node to our running traversal path 
                return nod

            # Have a node to continue traversing in this thread
            cur_node = nod
            nxt_node = rslt_tup[2]
            cur_dirt = rslt_tup[1]
            path_trvse_id.append(nod)                       # add to our running traversal path 
            path_trvse_drt.append(cur_dirt)                 # add to our running execution of steps ("n","s","e","w")
            path_bkup.append(gen_back_up_step(cur_dirt))    # add directive to get back to the current node
                                                            # from the next node (inverse of cur_dirt)

            # Mark node/directives as visted/inspected
            graph_vst[cur_node][cur_dirt] = True                    # mark the current node/current directive as visited
            graph_vst[nxt_node][gen_back_up_step(cur_dirt)] = True  # mark the next node's back path to the current node
                                                                    # as visited so we don't double back on ourselves
            foo()
            
            # traverse deeper calling node_dive recursively
            return node_dive(nxt_node)

        # Trigger the recursive diving with the passed node
        rt_node = node_dive(nde)
        return rt_node

    # Kick off the action and take a deep dive from the starting node
    current_node = deep_dive(strt)

    # Keep diving while the back up stack has values
    while len(path_bkup) != 0:
        # pop the last back up path directive (to get us to node upstream)
        bk_dir = path_bkup.pop()

        # take a deep dive on this node (after backing up one node)
        bk_nde = graph_trv[current_node][bk_dir]
        path_trvse_drt.append(bk_dir)               # add to our running execution of steps ("n","s","e","w"
        current_node = deep_dive(bk_nde)

#****************************************
#* MAIN PROC
# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Parse through the "world" object and construct an adjacency matrix
my_graphs       = rooms2obj(world.rooms)
graph_trv       = my_graphs[0]
graph_vst       = my_graphs[1]
path_trvse_id   = []
path_trvse_drt  = []
path_bkup       = deque()

# Start traversing
trav_graph(graph_trv, world.starting_room.id)
foo()
quit()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TRAVERSAL TEST - DO NOT MODIFY
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
