# Woke up this morning, and I had those walking blues...
# Woke up this morning, and I had those walking blues...
# I wasn't walking nowhere, because I didn't have no legs!
# But I'm alright! (He's alright...) I'm alright! (He's alright...)
# But I'm alright! (He's alright...) I'm alright! (He's alright...)
# You know I'm alright now! (He's alright...) You know I'm alright now! (He's alright...)
# You know I'm alright now, cuz I finished CS Sprint Challenge 3!


def walking_blues():
    from player import Player
    import adv
    total_rooms_visited = adv.total_rooms_visited
    traversal_length = adv.traversal_length
    world = adv.world
    bfs_queue = adv.bfs_queue
    room_graph = adv.room_graph
    while not total_rooms_visited > 500:
        cardinal_pairs = dict(n="s", e="w", s="n", w="e")
        player: Player = Player(world.starting_room)
        walking_graph = {}
        starting_room = {}
        total_rooms = []

        for cardinal in player.current_room.get_exits():
            starting_room[cardinal] = "?"
        walking_graph[world.starting_room.id] = starting_room
        adv.depth_first_spelunking(player, walking_graph)

        while not bfs_queue.qsize() is 0:
            start_room = player.current_room.id
            next_room = bfs_queue.get_nowait()
            player.travel(next_room)
            total_rooms.append(next_room)
            exit_room = player.current_room.id
            walking_graph[start_room][next_room] = exit_room
            if exit_room not in walking_graph:
                walking_graph[exit_room] = {}
                for room_exit in player.current_room.get_exits():
                    walking_graph[exit_room][room_exit] = "?"
            walking_graph[exit_room][cardinal_pairs[next_room]] = start_room
            if bfs_queue.qsize() is 0:
                adv.depth_first_spelunking(player, walking_graph)
        if not len(total_rooms) >= traversal_length:
            traversal_path = total_rooms
            total_rooms_visited = len(total_rooms)
            traversal_length = total_rooms_visited

            visited_rooms = set([])
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
