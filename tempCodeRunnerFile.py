rooms(self, starting_room):
#     neighbor_rooms_to_visit = Queue()
#     visited_rooms = {}

#     neighbor_rooms_to_visit.enqueue([starting_room])
#     while neighbor_rooms_to_visit.size() > 0:
#         current_path = neighbor_rooms_to_visit.dequeue()
#         current_path_last_vertex = current_path[-1]
#         if current_path_last_vertex not in visited_rooms:
#             visited_rooms[current_path_last_vertex] = current_path
#             for neighbor in player.current_room.get_exits():
#                 re