# Maze Path

Given a maze in the form of a binary rectangular matrix, find the length of the shortest path in a maze from a given source to given destination.

The path can only be constructed out of cells having the value 1 and movement is limited to one adjacent cell up, down, left, or right.

Example:
```
[1, 1, 1, 1, 0, 1],
[1, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 1, 0],
[0, 1, 1, 1, 0, 0],
[1, 1, 0, 1, 1, 1]

Find the shortest path from (0,0) to (3,3).

Solution (visualized with 2's): 5
[2, 1, 1, 1, 0, 1],
[2, 0, 0, 1, 1, 1],
[2, 2, 2, 0, 1, 0],
[1, 1, 0, 1, 1, 0],
[0, 1, 1, 1, 0, 0],
[1, 1, 0, 1, 1, 1]
```