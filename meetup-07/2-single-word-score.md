# Single Word Score

## Summary

In the game of Scrabble, players fight to the death by placing letter tiles on a board to create words. Each letter is worth a different number of points and a word's score is calculated by adding the point value of each letter.

Given a list of words, find the word that contains the highest possible Scrabble score. If multiple words have the same score, return the word that is alphabetically first.

For your convenience, the point value of each letter is provided as JSON at the bottom of this page.

## Input

An array of strings containing English words. 

## Output

A single string of the word that has the highest scrabble score.

## Examples

| Input | Output |
| --- | --- |
| `["QUIXOTIC", "QUICKLY", "WHIZBANG", "JUMBLES", "MAXIMIZE"]` | `"MAXIMIZE"` |
| `["KWYJIBO", "ID", "OXIDIZE"]` | `"KWYJIBO"` |
| `["IS", "WILL", "ONLY", "THE", "AN", "EMU"]` | `"ONLY"` |

## Scrabble Letter Scores as JSON

```
{
  "A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2,
  "H":4, "I":1, "J":8, "K":5, "L":1, "M":3, "N":1,
  "O":1, "P":3, "Q":10, "R":1, "S":1, "T":1, "U":1,
  "V":4, "W":4, "X":8, "Y":4, "Z":10
}
```
