# Telephone Words

## Summary

You may have noticed on your pyhone that each number on the keypad corresponds to a set of Latin letters as well: http://en.wikipedia.org/wiki/File:Telephone-keypad2.svg

Businesses sometimes will come up with something memorable and clever from their phone numbers using these letters. But there are many combinations!

We're going to make it easier for them!

Let's write a function that can take a phone number and return a list of all the permutations.

## Input

A string `T` that is up to 4 numbers long

## Output

An array of all the possible telephone words

## Example

Input: '2745'

Output: ['APGJ', 'APGK', 'APGL',.......,'CSIL']

## Constraints

1 <= length of `T` <= 4

## Tips

* Phone numbers are strings and can start with a 0!
* The digits 0 and 1 do not have letters associated with them, so they should be left as numbers.
* You can't scramble the order! The digits must remain in that order.