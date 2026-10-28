## Google Interview Question

You are given an English word dictionary. You may first, during a
**preprocessing / setup phase**, build a suitable data structure for the
dictionary so that subsequent queries can be answered as efficiently as
possible.

Each query gives you **9 letters**. You need to find the **longest word
in the dictionary** that can be formed using these 9 letters.

### Rules
- If a letter appears once, it can be used **at most once**.
- The input **may contain duplicate letters**.
- Return the longest word from the dictionary that can be formed.

### Example

**Dictionary:**
["cat", "coat", "taco", "cocoa"]

**Input:**
['c', 'o', 'a', 't', 'x', 'y', 'z', 'm', 'n']

**Output:**
"coat" or "taco"