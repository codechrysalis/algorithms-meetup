# Islands

## Summary

Given a map of an ocean, count how many islands there are.

## Input

A 2-D array of 0's and 1's where 0 represents water and 1 represents land;

## Output

An integer representing the number of islands on the map. (If two pieces of land are next to each other on the same column or same row, they are considered "connected" and are thus part of the same island)

Challenge mode: If two pieces of land are diagonal, they are also considered "connected."

## Example

Map:
```
[[1, 1, 1],
 [0, 0, 0],
 [0, 0, 1]]
```

Islands: 2

Map:
```
[[0, 1, 0, 1],
 [0, 0, 0, 0],
 [1, 0, 1, 0],
 [1, 0, 1, 0]]
```

Islands: 4

## Constraints 
 
Map size is at least 1x1 and at most 10x10.

Time complexity must be O(n) or faster.

## Tips

Good luck!
