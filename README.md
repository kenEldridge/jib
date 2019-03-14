# Data-Structures and Algorithms To Implement for Edification

## Data-Structures
 - [LinkedList](#linkedlist)
 - [GraphNode](#graphs)
   - Bidirectional (todo)
   - Make it iterable (todo)
 - [TreeNode](#trees)
 - [BinaryTreeNode](#binarytrees)
 - Trie
 - Heap
 - Vector / ArrayList
   - Use this collection in GraphNode (todo)
 - Hash table
 - Stack
 - Queue

### LinkedList

| function | description |
| :------------: | :---------- |
| insert(node)   | Insert node either following a specific node (by_value) or at the end of the list |
| remove(node) | Remove specified node. Assumes self is the head |
| __iter__() | init to implement iterable |
| __next__() | next to implement iterable |

### Graphs
Directed graph of arbitrary degree.

| function | description |
| :------------: | :---------- |
| add(node) | Adds node to self's adjacency list |
| remove(node) | Removes node from self's adjacency list |

### Trees
TreeNodes inherit from [GraphNode](#graphs).  They support arbitrary degree.  TreeNodes enforce tree constraints when adding nodes.  They have a `parent` attribute, allowing a TreeNode to walk backwards to it's root.  

| function | description |
| :------------: | :---------- |
| add(child)   | add child if no tree constraint dependency |
| remove(node) | from GraphNode |

### BinaryTrees
BinaryTreeNodes inherit from [TreeNode](#trees).  They support left and right children.

***WIP: add more tests?, remove(), what if someone tired to use the adjacency list from TreeNode?***

| function | description |
| :------------: | :---------- |
|    |  |

## Algorithms
 - Breadth-First Search: TreeNode.add() uses BFS
 - Depth-First Search
 - Binary Search
 - Merge Sort
 - Quick Sort
