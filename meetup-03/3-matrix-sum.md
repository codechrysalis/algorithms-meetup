# Matrix Sum

## Summary

Given a 2D matrix N x N, find the submatrix with the maximum sum.

Submatrix can be square or rectangular, but its area cannot be more than half of the given matrix.

## Input

A list of lists representing the 2D N x N matrix

## Output

A list of lists representing the 2D sub-matrix. The submatrix cannot be larger than half of the given matrix and can be either a square or a rectangle.

## Example

Input:

```js
[
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5]
]
```

Output:

```js
[
  [4, 5],
  [4, 5],
  [4, 5]
]
```

## Constraints

1 < N < 100
