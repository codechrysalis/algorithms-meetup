# Frogger

## Summary

You are a frog. You are given a path represented by a string that starts and ends with X's and in between is filled with a random mix of X's and O's, where X's are land and O's are holes. You will need to get from one side of the path to another safely. The largest you can hop is over 2 holes in a row.

Can you make it?

## Input

A string that starts and ends with 'X' and in between, is filled with X's and O's.

## Output

A boolean (true/false).

## Example

Example 1

Input: 'XOOXXOXOXOXOOOOX'

Output: false

This isn't safe because we can't jump over so many O's!

Example 2

Input: 'XOXOOXXXXOX'
Output: true

## Constraints

No constraints.