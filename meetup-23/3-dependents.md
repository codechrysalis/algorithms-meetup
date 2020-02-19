# Dependents

## Summary

You are given an object with a list of dependencies (represented as strings or other objects). Write a function that loads all the dependencies in the order they are injected.

## Input

An object of strings and objects.

## Output

An array of dependency strings OR false if bad news happens.

## Example

Example 1

Input:

```
var package = {
  a: 'c',
  c: {
    b: 'd',
    d: {
      z: 'a'
    }
  }
  m: 'c',
}
```

Output:
`FALSE`

Example 2

Input:

```
var package = {
  c: {
    b: 'd',
    d: {
      z: 'a'
    }
  }
  m: 'c',
}
```

Output:
`['a', 'z', 'd', 'b', 'c', 'm']`