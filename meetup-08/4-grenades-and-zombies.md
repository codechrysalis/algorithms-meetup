# Grenades and Zombies

## Summary

You are given a `N`x`N` board with zombies (2) and walls (1) scattered all about. You are given only one grenade.

Your mission is to kill as many zombies as possible.

A few constraints:

- the impact of the grenade travels only horizontally and vertically
- the impact goes through zombies but NOT walls and of course, ends at the border
- can only place grenades on spaces NOT occupied by walls or zombies

## Input

A 2-D matrix of `N`x`N` with zombies represented by 2 and walls represented by 1. Empty spaces are marked as 0.

## Output

A simple tuple of the row index and column index where the grenade kills the most zombies.

If there are multiple possibilities that kill the same number of zombies, return the appropriate coordinates in a list.

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
