while len(traversalPath) < 20000:
    # show exits of current room
    room_exits = traversalGraph[player.currentRoom.id]
    # init unexplored exists
    unexplored_exits = []
    # add possible directions to unexplored exits
    for direction in room_exits:
        if room_exits[direction] == '?':
            unexplored_exits.append(direction)
    # while room is explorable
    if len(unexplored_exits) > 0:
        # pick random exit
        random_exit = random.choice(unexplored_exits)
        # add to path
        traversalPath.append(random_exit)
        # set temp variable
        previous_room_id = player.currentRoom.id
        # travel to that room
        player.travel(random_exit)

        exit_dictionary = {}
        for exit in player.currentRoom.getExits():
            exit_dictionary[exit] = '?'
        traversalGraph[previous_room_id][random_exit] = player.currentRoom.id
        exit_dictionary[inverse_directions[random_exit]] = previous_room_id
        traversalGraph[player.currentRoom.id] = exit_dictionary
        '''
        if player.currentRoom.id not in traversalGraph:
            exit_dictionary = {}
            for exit in player.currentRoom.getExits():
                exit_dictionary[exit] = "?"
            traversalGraph[player.currentRoom.id] = exit_dictionary

        traversalGraph[previous_room_id][random_exit] = player.currentRoom.id
        traversalGraph[player.currentRoom.id][inverse_directions[random_exit]] = previous_room_id
        '''

    else:
        # break
        path_creation = True
        path = []
        new_list = list(traversalPath)
        # walk backwards
        while path_creation:
            # Player moves back one room
            if new_list:
                popped = new_list.pop()
                player.travel(inverse_directions[popped])
                # add move to path
                path.append(inverse_directions[popped])

                # check if current_room_exits has not been explored
                current_room_exits = traversalGraph[player.currentRoom.id]
                current_unexplored_exits = []
                # add possible directions to unexplored exits
                for direction in current_room_exits:
                    if current_room_exits[direction] == '?':
                        current_unexplored_exits.append(direction)
                        # add path to traversal
                if len(current_unexplored_exits) > 0:
                    path_creation = False
                    traversalPath.extend(path)
            else:
                break


print(traversalGraph)
print(traversalPath)
print(len(traversalPath))

# queue = deque()
# queue.append(list(inverse_directions[traversalPath[-1]]))

# while queue:
#     dequeued = queue.popleft()
#     last_step = dequeued[-1]
#     player.travel(last_step)

#     current_room_exits = traversalGraph[player.currentRoom.id]
#     current_unexplored_exits = []
#     for direction in current_room_exits:
#         if current_room_exits[direction] == '?':
#             current_unexplored_exits.append(direction)
#     if current_unexplored_exits:
#         traversalPath.extend(dequeued)
