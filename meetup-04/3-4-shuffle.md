# Shuffle

## Summary

Shuffle a deck of cards in a random order. You cannot use any native functions/methods or libraries.

Each given card should be as likely as any other to appear in a given deck index. Think carefully how to create your algorithm---it's really easy to create a biased algo.

## Input

An array containing a deck of cards.

## Output

An array containing a shuffled deck of cards.

## Example

Input: `["A♥","2♥","3♥",...,"J♦","Q♦","K♦"]`

Output: `["2♠","J♣","A♦", ... ,"7♣","8♣","K♠"]`

## Limit

O(N) time and O(1) space

Your algorithm must remain ubiased as the deck size increases.

## Tips

* [pseudorandom number generator](http://en.wikipedia.org/wiki/Pseudorandom_number_generator)

## Extra

How do you write tests for this?