# Path Statistics

## Summary

You are given a tree with `n` nodes, that is, an acyclic connected graph, where each node `i` is assigned a value `c`<sub>i</sub>.

You must answer `q` queries in the form `u v k`. For each query, find and print the `k^th` most frequent value on the path between `u` and `v`. If two values appear the same number of times, for tie-breaking, the smaller number is considered less frequent than, the bigger one.

## Input

You are given `n` and `q` (integers)
You are given an array of integer tuples describing the respective values of `c`<sub>1</sub>, `c`<sub>2</sub>, ...`c`<sub>n</sub>.
You are given an array of array of integers describing the queries: `u`, `v`, `k`.


## Output

You should return a single integer for each query, denoting the `k^th` most frequent value on the path between `u` and `v` as an array of integers.

## Example

Example

Input:
`n = 6`
`q = 4`
values of c = `[1, 1, 3. 2. 4. 2]`
edges: `[[1, 4], [4, 5], [6, 2], [3, 6], [4, 2]]`
queries: `[[1, 2, 1], [1, 2, 2], [1, 3, 1], [1, 3, 3]]`

Output: `[1, 2, 2, 3]`

For the first and second queries, the numbers that appear on the path are [1, 2, 1]. The most frequent number is 1 and the second one is 2.

For the third and fourth queries, the path is composed by [1, 2, 1, 2, 3]. Since both 1 and 2 appear twice on the path, and according to the problem statement, 1 being smaller is considered less frequent than 2, the answer for the query [1, 3, 1] is 2 because 2 is the most frequent number. The second most frequent number is 1 (only because it is smaller than 2), and the third one is 3, thus the answer for the last query is 3.

## Constraints 

1 <= n, q <= 5 x 10<sup>4</sup>  
1 <= c<sub>i</sub> <= 10<sup>9</sup>  
1 <= u, v <= n  
1 <= k <= number of distinct values on the path between u and v
