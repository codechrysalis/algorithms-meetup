# Slugify

## Summary

**Slug** is a url friendly version of any name (person name, blog post title, etc.). **Slugify** is a tool to convert a string (usually a person name, a blog post title, etc.) into a slug.

There are multiple versions of **Slugify**. In our scope, **Slugify** ensures 3 things:

- The output contains only lowercase alphanumerical characters and hyphens
	* Uppercase letters will be replaced with lowercase ones.
	* Other characters will be replaced with hyphens
- There should not be 2 hyphens next to each other (multiple hyphens should be reduced to one hyphen)
- The first and the last characters of the output should not be a hyphen

## Input 

A string in English that represents a post title.

## Output

A slug version of the string

## Examples

```
INPUT
Microsoft acquiring GitHub is a good thing. Here is why. 

OUTPUT
microsoft-acquiring-github-is-a-good-thing-here-is-why
```

```
INPUT
Top 10 JavaScript errors from 1000+ projects (and how to avoid them)

OUTPUT
top-10-javascript-errors-from-1000-projects-an-how-to-avoid-them
```

```
INPUT
[JavaScript] Most popular books!!!

OUTPUT
javascript-most-popular-books
```
