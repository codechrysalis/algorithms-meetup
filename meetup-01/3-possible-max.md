# Possible Max

## Summary

You are given a set S = {1, 2, 3, ..., N} and an integer K.

Find two integers A and B from the set S that fulfill the following:

* A < B
* A & B is the max possible (**& represents the operator bitwise AND**)
* Less than K

## Input

N = the max number in your set (int)

K = max number limit that your outputs cannot surpass (int)

## Output

Two outputs: A and B

They can be returned in an array or however you see fit. But it needs to be two numbers, A and B, that fulfill the criteria.

## Constraints

* 2 <= N <= 10^3
* 2 <= K <= N

## Example

* N = 5, K = 2
* S = {1, 2, 3, 4, 5}

Possible Values of A & B:

```
A = 1, B = 2. So, A & B = 0
A = 1, B = 3. So, A & B = 1
A = 1, B = 4. So, A & B = 0
A = 1, B = 5. So, A & B = 1
A = 2, B = 3. So, A & B = 2
A = 2, B = 4. So, A & B = 0
A = 2, B = 5. So, A & B = 0
A = 3, B = 4. So, A & B = 0
A = 3, B = 5. So, A & B = 1
A = 4, B = 5. So, A & B = 4
```

* Output: 1 (max possible value of A & B)


## Tips

* [Bitwise AND on MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators#Bitwise_AND)
* [Bitwise AND on Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation#AND)