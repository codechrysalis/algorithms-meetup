# Normal Human Picnic

## Summary

You decide to go on a normal picnic with your normal picnic blanket to a normal park. 

* The picnic blanket can spread out to any size as long as it is a perfect square.
* If the blanket is placed over a mound of fire ants, the blanket will catch on fire and explode.
* The park you go to is a perfect square.
* The park also has a fire ant infestation.

Calculate the largest possible size you can spread out your blanket without it catching on fire.

## Input

A grid of booleans that represent a map of the park. If the cell is `true`, then this means there is a fire ant mound in that location.

## Output

An integer representing the largest possible size that you can spread out the picnic blanket without it catching on fire. This is the number of grid cells the blanket can cover. For example, if the blanket can cover a 5x5 square, return 25.

## Examples

| Input | Input (Readable) | Output | Why? |
| --- | --- | --- | --- |
| `[[true, false, false, false, false], [false, false, false, false, false], [false, false, false, false, false], [false, false, false, true, false], [false, true, false, false, false]]` | `10000`<br>`00000`<br>`00000`<br>`00010`<br>`01000` | `9` | 3x3 space in the top right corner |
| `[[true, false, true, false, true], [false, true, false, true, false], [true, false, true, false, true], [false, true, false, true, false], [true, false, true, false, true]]` | `10101`<br>`01010`<br>`10101`<br>`01010`<br>`10101` | `1` | Largest space is 1x1 |
| `[[true, false, true, false, true, false, false, false, false, false], [false, false, false, false, false, true, false, false, true, false], [false, false, false, false, false, false, false, false, false, false], [true, false, false, false, false, true, false, false, false, false], [false, false, false, false, false, false, false, false, false, true], [false, true, false, false, false, false, false, false, true, false], [true, false, false, false, true, false, false, false, false, true], [true, false, false, false, false, false, false, false, false, false], [false, false, true, false, false, false, true, true, false, false], [false, false, false, false, false, true, false, false, false, false]]` | `1010100000`<br>`0000010010`<br>`0000000000`<br>`1000010000`<br>`0000000001`<br>`0100000010`<br>`1000100001`<br>`1000000000`<br>`0010001100`<br>`0000010000` | `16` | 4x4 space available towards the top left |

## Complexity Goals

`n` is the side length of the park

* Brute Force Time Complexity: **O(n<sup>4</sup>)**
* Brute Force Space Complexity: **O(n<sup>2</sup>)**
* Ideal Time Complexity: **O(n<sup>2</sup>)**
* Ideal Space Complexity: **O(n)**
