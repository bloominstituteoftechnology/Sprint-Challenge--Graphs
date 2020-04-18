import unittest
import io
from contextlib import redirect_stdout
from ast import literal_eval

from room import Room
from player import Player
from world import World
from adv import traversal_path

class Test(unittest.TestCase):
    def setUp(self):
        file_path="maps/main_maze.txt"
        with open(file_path, "r") as f:
            map_file = f.read()

        self.world = World()
        self.room_graph = literal_eval(map_file)
        self.world.load_graph(self.room_graph)

        self.player = Player(self.world.starting_room)

    def test_valid(self):
        visited_rooms = set()
        visited_rooms.add(self.player.current_room)

        for move in traversal_path:
            print_trap = io.StringIO()
            with redirect_stdout(print_trap):
                self.player.travel(move)
                visited_rooms.add(self.player.current_room)

        self.assertEqual(len(visited_rooms), len(self.room_graph))

    def test_mvp(self):
        self.assertLessEqual(len(traversal_path), 2000)

if __name__ == '__main__':
    unittest.main()