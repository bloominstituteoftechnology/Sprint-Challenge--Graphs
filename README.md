# Sprint Challenge: Graphs

For this Sprint Challenge, you will be traversing a map based on the adventure engine from Week 1 of `Intro to Python`.

Good luck and have fun! :smile:

Note: The `legacy` directory contains an old exercise for archival purposes. You do not need to work on this and it will not be graded.

# Sprint Challenge: Graphs

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint explored Graphs. During this Sprint, you studied breadth and depth first traversals and searches along with random graphs.

You are provided with a pre-generated graph consisting of 500 rooms. You are responsible for filling `traversalPath` with directions that, when walked in order, will visit every room on the map at least once.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency graphs and your command of the concepts and techniques from this week's material.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

Open `adv.py`. There are four parts to the provided code:

* World generation code. Do not modify this!
* A list with two directions in it. Your task is to fill this with valid traversal directions.
* Test code. Run the tests by typing `python3 adv.py` in your terminal.
* REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.


You may find the commands `player.currentRoom.id` and `player.currentRoom.getExits()` useful.

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

Try moving south and you will find yourself in room `5` which contains exits `['n', 's', 'e']`. You can now fill in some entries in your graph:

```
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
```

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path as it walks.

## Minimum Viable Product

* __1__: Tests do not pass
* __2__: Tests pass with `len(traversalPath) < 2000`
* __3__: Tests pass with `len(traversalPath) < 960`

## Stretch Problems

It is very difficult to calculate the shortest possible path that traverses the entire graph. Why?

My best path is 957 moves. Can you find a shorter path?
