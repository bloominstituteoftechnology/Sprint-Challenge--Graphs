import random
from helpers.walkingblues import walking_blues
from ast import literal_eval
from queue import SimpleQueue
from world import World

traversal_path = []
traversal_length_initial_value = 999
traversal_length = traversal_length_initial_value
total_rooms_visited = 0
bfs_queue = SimpleQueue()


# walking blues until we hit a dead end
def depth_first_spelunking(player, graph):
    global bfs_queue
    current_room_exits = graph[player.current_room.id]
    undiscovered_exits = []
    # Log undiscovered exits in the current room
    for cardinal in current_room_exits:
        if current_room_exits[cardinal] is "?":
            undiscovered_exits.append(cardinal)
    # Use bfs to retrace path if we hit a dead end
    if len(undiscovered_exits) is 0:
        breadcrumbs = breadth_first_spelunking(player, graph)
        room_on_path = player.current_room.id
        for next_room in breadcrumbs:
            for cardinal in graph[room_on_path]:
                if graph[room_on_path][cardinal] is next_room:
                    bfs_queue.put_nowait(cardinal)
                    return
    # Otherwise choose a random direction
    else:
        bfs_queue.put_nowait(
            undiscovered_exits[random.randint(
                0, len(
                    undiscovered_exits
                ) - 1
            )
            ]
        )


# Backtrack to find unexplored paths with bfs
def breadth_first_spelunking(player, graph):
    breadcrumbs = SimpleQueue()
    visited_rooms = set([])
    breadcrumbs.put_nowait([player.current_room.id])
    # retrace path as long as there are breadcrumbs in the queue
    while not breadcrumbs.qsize() is 0:
        path = breadcrumbs.get_nowait()
        last_room = path[-1]
        # Check if we hit an unexplored room
        if last_room not in visited_rooms:
            # Log it
            visited_rooms.add(last_room)
            # Check exits
            for room_exit in graph[last_room]:
                # Return path if we find an unexplored exit
                if graph[last_room][room_exit] is "?":
                    return path
                # Otherwise, keep on truckin'
                else:
                    breadcrumb_path = list(path)
                    breadcrumb_path.append(graph[last_room][room_exit])
                    breadcrumbs.put_nowait(breadcrumb_path)
    # when we run out of breadcrumbs in our queue, return an empty list
    # as we exit the loop since we're back at an unexplored path
    return list()


# Load world
world = World()

map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Fill this out with directions to walk
walking_blues()
