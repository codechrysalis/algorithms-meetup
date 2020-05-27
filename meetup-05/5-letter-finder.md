# Letter Finder

## Summary

Find the longest path of consecutive letters starting from the top left corner. You can move all 8 directions.

You can't go back to a used letter.

## Input

An N x M matrix of single letters.

```
a b e d
b c f e
a b d d
```

## Output

The longest length (an integer).

## Example

Given the above example, the answer would be 10.

Reasoning: Starting from the `a` in the top-left corner...

`a` -> `b` -> `a` -> `b` -> `c` -> `d` -> `e` -> `f` -> `e` -> `d`