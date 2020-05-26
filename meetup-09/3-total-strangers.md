# Total Strangers

## Summary

You are given a set of people and their friends.

Your mission is to return a set of people and their _total strangers_. In other words, for each person, compute the people that are not even _friends of friends_.

## Input

A JSON representation of a set whose keys represent people, and values represent the people they know directly.

## Output

A JSON representation of a set whose keys represent people, and values represent the people they don't know or have mutual friends with.

## Example

### Input

```
{
  alice: ["carol"],
  bob: ["dave"],
  carol: ["alice"],
  dave: ["bob"]
}
```

### Output

```
{
  alice: ["bob", "dave"],
  bob: ["alice", "carol"],
  carol: ["bob", "dave"],
  dave: ["alice", "carol"]
}
```
