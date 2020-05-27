# Bombs and Bots

## Summary

You are given a `N`x`N` board with robots (2) and walls (1) scattered all about. You are given only one bomb.

Your mission is to kill as many robots as possible.

A few constraints:
- the impact of the bomb travels only horizontally and vertically
- the impact goes through robots but NOT walls and of course, ends at the border
- can only place bombs on spaces NOT occupied by walls or robots

## Input

A 2-D matrix of `N`x`N` with robots represented by 2 and walls represented by 1. Empty spaces are marked as 0.

## Output

A simple tuple of the row index and column index where the bomb kills the most robots.

If there are multiple possibilities that kill the same number of robots, return the appropriate coordinates in a list.

## Example

Input: 

```
[
  [0, 0, 0, 0, 0, 0],
  [1, 2, 0, 0, 0, 2],
  [0, 0, 0, 0, 0, 0],
  [2, 0, 0, 1, 2, 0],
  [0, 0, 1, 0, 0, 0],
  [2, 0, 0, 0, 0, 0]
]
```

Output: `[4, 1]`

## Constraints 
 
4 < `N` < 10^5
