# Robot Paths

## Summary

You are given an NxM board with a robot in the upper left square.

There are obstacles in the way, represented by 1s. The robot can only travel horizontally and vertically until it hits an obstacle or a wall. Only then can the robot change directions.

What is a path with the fewest amount of moves for the robot to travel to the bottom right corner?

## Input

A 2-D array of 0s and 1s.

## Output

The output should be a string of the directions:

'L' = left
'R' = right
'U' = up
'D' = down

## Example


```
[
  [0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [1, 0, 0, 1, 1, 0],
  [0, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 0, 0]
]
```

Output: 'RD'