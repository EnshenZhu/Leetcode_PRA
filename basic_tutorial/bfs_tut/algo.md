# General
Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. BFS can be easily implemented using recursion and data structures like dictionaries and lists.

# Source
https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

# Algorithm

* Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
* If there are no remaining adjacent vertices left, remove the first vertex from the queue.
* Repeat step 1 and step 2 until the queue is empty or the desired node is found.