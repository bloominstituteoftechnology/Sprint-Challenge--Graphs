from room import Room
from player import Player
from world import World
import itertools
import re


def checkExits(player):
    exits = []  # checking the exits for our current room
    directions = ['n', 's', 'e', 'w']
    for direction in directions:
        if player.currentRoom.getRoomInDirection(direction):
            exits.append(
                [direction, player.currentRoom.getRoomInDirection(direction).id])
    print(exits)
    return exits
