## Description

You are provided with a pre-generated graph consisting of 500 rooms. You are responsible for filling `traversal_path` with directions that, when walked in order, will visit every room on the map at least once.

Open `adv.py`. There are four parts to the provided code:

* World generation code. Do not modify this!
* An incomplete list of directions. Your task is to fill this with valid traversal directions.
* Test code. Run the tests by typing `python3 adv.py` in your terminal.
* REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.


You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

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

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.

Your solution **must** generate the solution by using graph traversal algorithms. Hardcoding a solution is not acceptable.

## Hints

There are a few smaller graphs in the file which you can test your traversal method on before committing to the large graph. You may find these easier to debug.

Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.

2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

If all paths have been explored, you're done!

## Minimum Viable Product

* __1__: Tests do not pass
* __2__: Tests pass with `len(traversal_path) <= 2000`
* __3__: Tests pass with `len(traversal_path) < 960`

## Stretch Problems

It is very difficult to calculate the shortest possible path that traverses the entire graph. Why?

My best path is 957 moves. Can you find a shorter path?


## Rubric
| OBJECTIVE | TASK | 1 - DOES NOT MEET Expectations | 2 - MEETS Expectations | 3 - EXCEEDS Expectations | SCORE |
| ---------- | ----- | ------- | ------- | ------- | -- |
| _Student can demonstrate applied knowledge of Graph Theory by traversing a large map_ | Complete traversal of a large Graph | Student unable to produce a valid traversal path of 2000 moves or less | Student is able to produce a valid traversal path between 960 and 2000 | Student produces a valid traversal path of 959 moves or less |  |
| **FINAL SCORE** | | **0-1** | **2** | **3** |  |


Change for initial push

 0, 1, 2, 5, 6, 23, 58, 23, 57, 68, 57, 94, 113, 145, 183, 145, 113, 94, 97, 153, 97, 110, 157, 110, 118, 133, 151, 188, 151, 133, 234, 247, 369, 247, 234, 280, 234, 259, 291, 306, 415, 306, 291, 259, 234, 133, 118, 218, 252, 261, 345, 409, 488, 409, 345, 261, 252, 218, 144, 134, 65, 62, 6, 62, 65, 134, 144, 218, 118, 110, 97, 94, 57, 23, 6, 5, 50, 66, 96, 179, 181, 179, 201, 206, 232, 244, 264, 290, 264, 244, 232, 265, 268, 276, 322, 424, 322, 276, 459, 467, 459, 276, 268, 265, 273, 296, 382, 455, 382, 296, 308, 317, 416, 317, 308, 337, 383, 460, 383, 337, 308, 296, 273, 298, 360, 364, 401, 420, 464, 420, 401, 427, 438, 448, 475, 496, 475, 448, 490, 448, 438, 427, 474, 427, 401, 364, 360, 298, 273, 265, 232, 206, 201, 179, 96, 66, 50, 70, 116, 159, 116, 70, 87, 117, 127, 212, 229, 237, 370, 237, 229, 212, 127, 173, 202, 267, 302, 402, 403, 439, 403, 402, 302, 267, 202, 249, 202, 173, 127, 117, 170, 182, 211, 248, 272, 248, 211, 182, 170, 117, 87, 70, 50, 5, 2, 10, 38, 10, 2, 1, 22, 1, 7, 12, 18, 24, 29, 54, 29, 24, 25, 43, 77, 130, 77, 43, 49, 119, 219, 242, 286, 309, 371, 430, 440, 430, 371, 309, 377, 456, 377, 309, 286, 288, 498, 288, 326, 288, 286, 242, 219, 305, 330, 348, 330, 454, 330, 305, 219, 119, 131, 329, 407, 329, 131, 119, 49, 43, 25, 24, 18, 34, 39, 52, 39, 71, 115, 160, 214, 246, 412, 246, 325, 246, 214, 160, 115, 71, 150, 251, 150, 71, 39, 34, 35, 44, 59, 189, 275, 283, 376, 468, 376, 283, 275, 189, 59, 44, 48, 53, 75, 88, 103, 88, 125, 198, 270, 300, 320, 471, 320, 300, 270, 198, 125, 238, 293, 238, 381, 431, 381, 238, 125, 88, 75, 78, 90, 142, 245, 343, 245, 142, 90, 98, 186, 262, 390, 398, 487, 398, 390, 262, 186, 98, 90, 78, 75, 53, 48, 44, 35, 34, 18, 12, 20, 26, 27, 55, 56, 67, 84, 86, 95, 109, 136, 231, 294, 311, 499, 311, 389, 311, 294, 363, 294, 231, 282, 231, 136, 109, 95, 86, 146, 86, 84, 67, 56, 73, 132, 172, 132, 73, 56, 55, 27, 26, 20, 31, 37, 42, 51, 93, 51, 42, 37, 91, 101, 91, 37, 31, 20, 12, 7, 9, 13, 14, 17, 28, 30, 28, 60, 64, 111, 114, 120, 114, 111, 121, 123, 138, 139, 176, 139, 147, 154, 184, 154, 192, 239, 336, 421, 336, 373, 336, 239, 255, 239, 192, 154, 147, 152, 196, 224, 287, 353, 380, 445, 480, 445, 446, 445, 380, 476, 380, 353, 287, 313, 287, 224, 196, 278, 338, 278, 196, 152, 233, 240, 304, 321, 334, 384, 435, 384, 334, 321, 354, 361, 366, 497, 366, 361, 354, 386, 388, 257, 163, 165, 169, 385, 169, 223, 483, 223, 169, 165, 197, 199, 281, 350, 425, 434, 425, 350, 281, 392, 408, 443, 477, 443, 408, 392, 281, 199, 318, 394, 426, 394, 422, 461, 422, 394, 318, 340, 374, 340, 318, 199, 197, 165, 163, 148, 121, 148, 178, 148, 163, 228, 253, 285, 253, 228, 163, 257, 388, 386, 354, 321, 304, 240, 233, 152, 147, 139, 138, 143, 138, 123, 121, 111, 64, 102, 107, 141, 175, 200, 204, 200, 328, 200, 175, 141, 107, 102, 64, 60, 28, 17, 33, 17, 46, 61, 82, 155, 185, 195, 185, 292, 316, 341, 316, 292, 185, 155, 82, 61, 63, 140, 63, 61, 46, 79, 106, 161, 166, 208, 307, 208, 166, 161, 106, 112, 210, 112, 124, 174, 277, 331, 387, 444, 387, 331, 277, 174, 221, 250, 295, 332, 351, 417, 442, 417, 351, 453, 351, 332, 295, 250, 289, 319, 441, 319, 289, 324, 391, 489, 491, 489, 391, 396, 391, 324, 411, 428, 452, 428, 429, 451, 429, 428, 411, 324, 289, 250, 221, 342, 357, 342, 221, 174, 124, 112, 106, 79, 46, 17, 14, 47, 14, 13, 15, 19, 32, 19, 40, 74, 40, 45, 85, 45, 81, 137, 168, 207, 297, 207, 168, 171, 168, 137, 81, 108, 167, 187, 303, 352, 303, 333, 358, 397, 358, 399, 400, 492, 400, 399, 358, 333, 365, 414, 365, 447, 365, 333, 303, 187, 301, 187, 167, 108, 81, 92, 128, 194, 227, 194, 128, 162, 205, 254, 284, 470, 284, 368, 436, 368, 465, 368, 284, 349, 418, 479, 418, 463, 458, 359, 344, 367, 462, 486, 462, 367, 344, 230, 220, 314, 339, 404, 482, 484, 482, 404, 339, 314, 220, 215, 177, 156, 209, 213, 216, 236, 258, 236, 263, 372, 433, 372, 263, 299, 312, 355, 457, 494, 457, 355, 312, 347, 437, 347, 375, 393, 375, 413, 478, 493, 478, 413, 419, 413, 375, 347, 312, 299, 356, 405, 432, 449, 450, 449, 432, 473, 432, 405, 356, 299, 263, 236, 216, 213, 217, 271, 310, 271, 217, 213, 209, 156, 149, 191, 193, 241, 256, 327, 362, 469, 362, 395, 423, 395, 362, 327, 256, 279, 323, 279, 256, 241, 193, 203, 269, 315, 406, 410, 406, 315, 335, 346, 335, 378, 466, 472, 481, 485, 481, 472, 495, 472, 466, 378, 335, 315, 269, 203, 193, 191, 149, 135, 126, 104, 89, 72, 69, 41, 76, 41, 36, 21, 3, 11, 80, 83, 99, 122, 99, 83, 80, 11, 3, 0, 8, 16, 8, 0, 4, 0, 3, 21, 36, 41, 69, 72, 89, 104, 105, 129, 190, 222, 274, 222, 190, 129, 105, 225, 226, 260, 266, 379, 266, 260, 226, 225, 105, 104, 126, 158, 235, 158, 164, 180, 164, 158, 126, 135, 149, 156, 177, 215, 243