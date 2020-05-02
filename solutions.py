def first_pass():
    map_graph = {}
    explored = set()
    to_explore = Queue()
    exits = player.current_room.get_exits()
    current_room = player.current_room.id
    explored.add(current_room)
    map_graph[current_room] = {}
    for exit in exits:
        to_explore.enqueue(exit)
        map_graph[current_room].update({f'{exit}': '?'})
    while len(explored) < len(room_graph):
        prev_room = current_room
        direction = to_explore.dequeue()
        print(direction)
        player.travel(direction)
        current_room = player.current_room.id
        if current_room not in explored and current_room != prev_room:
            map_graph[current_room] = {}
            map_graph[prev_room].update({f'{direction}': current_room})
            traversal_path.append(direction)
            exits = player.current_room.get_exits()
            for exit in exits:
                if map_graph[current_room][exit] != '?':
                    explored.add(current_room)
                to_explore.enqueue(exit)
                map_graph[current_room].update({f'{exit}': '?'})

    print(map_graph)


def second_try():
    explored = {}
    while len(explored) < len(room_graph):
        current_room = player.current_room.id
        exits = player.current_room.get_exits()

        if current_room not in explored:
            explored[current_room] = {exit: '?' for exit in exits}
        need_to_visit = [
            exit for exit in explored[current_room] if explored[current_room][exit] == '?']

        if len(need_to_visit) > 0:
            to_travel = need_to_visit.pop()
            player.travel(to_travel)
            traversal_path.append(to_travel)


first_pass()
