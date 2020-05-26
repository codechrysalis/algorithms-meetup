# Kim Kardashian

## Summary

You're Kim Kardashian and you have in front of you a case full of expensive jewelry.

Each piece of jewelry has a weight and value. Unfortunately, you've just had another West child, so you can only support a weight capacity of 5 pounds of jewelry.

What is the max value of jewelry you can wear to the upcoming Met Gala? You can wear as much jewelry as you would like, up to 5 pounds.

## Input

Input is a list/vector/dictionary of jewelry objects/classes with the following properties:

- weight: Number (in oz)
- value: Number (in thousands of USD)

## Output

Output is a list/vector of the jewelry you can wear.

## Example

Input:

```js
[
  {weight: 10, value: 160},
  {weight: 20, value: 80},
  {weight: 7, value: 15},
  {weight: 40, value: 70},
  {weight: 30, value: 170},
  {weight: 60, value: 20}
];
```

Output:

```js
[
  {weight: 10, value: 160},
  {weight: 30, value: 170},
  {weight: 20, value: 80},
  {weight: 7, value: 15}
]
```

## Tips/Hints

How many oz are in a pound?