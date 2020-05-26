# Search DNA

## Summary

You've been hired by COOL-BIO-TECH-COMPANY to help efficiently process large batches of DNA.
COOL-BIO-TECH-COMPANY specialiazes in showing customers which genetic traits they are likely to express.

How its done:
1. Customers submit their DNA sequences (their genomes).
2. COOL-BIO-TECH-COMPANY checks their submitted sequences against a list of DNA sequences that correspond to genetic traits
3. COOL-BIO-TECH-COMPANY returns the list of matches to the customer.

Your goal is a small part of this operation. You will be given many different DNA sequences provided by customers to search against (the customer's genomes), and a series of specific DNA sequences you are looking for (traits).

Example:
Customer's Genome: "ATTATTA..."
Target: "ATTATTG"

You could solve this by looping over the customers genome, checking if it matches target the genetic trait at each location, and restarting beginning at the next index when a mismatch is detected. In the worst case, this will take O(n x m) where n is genome length and m is the length of the trait we're looking for

We can do much better than this. Imagine we're searching for the sequence ATTATTG in a genome which starts with "ATTATTA..." (shown above). This does not match our sequence (it ends with an 'A' not a 'G' at index 7). However, based on what pairs we have seen so far we know that ATT*ATTA*... matches the first part of the sequence we're looking for: *ATTA*TTG. We should remember this partial match, and continue reading the next letter (expecting to see a T next). By remember these partials matches, we only ever need to read each letter in Customer's Genome once.

Your goal is to construct a "state machine" to do this. The state machine will have a number of states equal to the number base pairs in the sequence. Each state will point to a previous state if the next base in the given sequence is not found.

Example:
Target: "CAT"

```
state-1 -> C -> go to state-2 
        -> A -> go to state-1
        -> T -> go to state-1
        -> G -> go to state-1

state-2 -> C -> go to state-2
        -> A -> go to state-1
        -> T -> go to state-1
        -> G -> go to state-1

state-3 -> C -> go to state-2
        -> A -> go to state-1
        -> T -> You found a match!
        -> G -> go to state-1
```

## Input

INPUT-1) A sequence of DNA that you will be searching for.

## Output
A state machine which searches genome for "INPUT-1"s sequence in linear time.

The state machine is a function which accepts a genome as its only parameter.
It returns true if INPUT-1 is found in the passed in genome, else returns false.

## Example

Inputs:
1) AATTCCGG
2) TCCG

Output: true

============

Inputs:
1) AATTCCGG
2) AATTT

Output: false

============

Input
1) ATCGATCGATCGAA
2) ATCGATCGAA

Output: true

============

Input
1) ATCGATCGATCGA
2) ATCGAA

Output: false

## Constraints

Construction of your state machine may take an arbitrary amount of time. Your state machine must search DNA strings in linear time O(n) with respect to Input-1 (the DNA sequence you are searching against). Each character in Input-1 should only be read once.

## Tips
The vast majority of your state steps should point back to state-1.

Look at the "CAT" and "ATTATTG" examples carefully.
The "CAT" example above already shows how partial matching occurs (from state-2 seeing a "C" does not send you to state-1, it sends you back to state-2).
"ATTATTG" is slightly more complicated. Try manually creating a state machine for "ATTATTG" by hand before attempting to generalize a solution for any input strings.

