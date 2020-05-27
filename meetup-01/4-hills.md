# The Hills

## Summary

There are N hills numbered 1 to N. There is gold at the peak of hill N.

Some of these hills are connected by one way rope bridges (directed), and these rope bridges are the only way to reach hill N and return back to hill 1. Each rope bridge disappears after being used once.

There are some traps for climbers. Some rope bridges do not lead to hill N, and some lead to hill N but without a way to return back to hill 1.

You MUST use all the rope bridges in your journey from hill 1 to N and back to 1.

If multiple ropes are connecting two hills then it should be counted multiple times and all of the ropes must be used once.

Given N hills and M pairs of connected hills, write a function that will determine whether there is a possible route or whether it is unsafe.

## Input

You get two inputs: n and m

N = number of hills

M = array of tuples [v1, v2]. Each tuple represents the hills connected by rope bridges.

## Output

Boolean (or different strings, up to you)

## Example

Example 1:

  * N = 4
  * M = [[1, 2], [2, 3], [3, 4], [4, 1]]
  * Output: "Yay!!"
    * Path/explanation: 1 -> 2 -> 3 -> 4 (treasure!) -> 1

Example 2:

  * N = 4
  * M = [[1, 2], [2, 3], [3, 1]]
  * Output: "Nooooo!"
    * Path/explanation: 1 -> 2 -> 3 -> 1 (but the treasure is on 4!)


## Constraints 
 
* 1 <= N <= 10^5
* 0 <= M <= 2 * 10^5