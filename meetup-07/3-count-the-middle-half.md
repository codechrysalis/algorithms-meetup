# The Middle Half

## Summary

Suppose you are given a list of random integers. If you ignore the lowest 25% of the numbers and the highest 25% of the numbers, find the sum of the remaining "middle half" of the list.  

You can assume the length of the list is divisible by 4.

Can you do this in linear time?

## Input

An array of integers

## Output

A single integer

## Examples

| Input | Output | Why? |
| --- | --- | --- |
| `[14, 3, 12, 5, 8, 1, 19, 22]` | `39` | (5 + 8 + 12 + 14) |
| `[4, 1, 2, 3]` | `5` | (2 + 3) |

## Time Complexity Goals

* Simple solution: **O(n log n)**
* Ideal solution: **O(n)**
