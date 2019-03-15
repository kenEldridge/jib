# Data-Structures and Algorithms To Implement for Edification

## Data-Structures
 - [LinkedList](#linkedlist)
 - [GraphNode](#graphs)
   - Bidirectional: issue #10
   - Make it iterable: issue #9
 - [TreeNode](#trees)
 - [BinaryTreeNode](#binarytrees)
 - Trie
 - [Heap](#heaps)
 - Vector / ArrayList
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
BinaryTreeNodes inherit from [TreeNode](#trees).  They support adding children via directly setting the `left` and `right` attributes.  When `left` or `right` are set, the class will enforce tree constraints.  

| function | description |
| :------------: | :---------- |
| add(child) | Currently works as it's inherited from TreeNode but should be **deprecated**, issue #11 |
| remove(child) | from GraphNode |

### Heaps
Heaps are commonly implemented as arrays.  However, I've been doing the inheritace thing with GraphNodes so I'm tempted to continue that strategy and implement Heaps as a sub-class of BinaryTreeNode.  Before I do that, let's make a quick space/time trade-off comparison for a max-heap.

#### Space
| | Space Complexity |
| :--: | :--: |
| Array Implementation Space | O(n) |
| Node Implementation Time | O(n) |

This is one of those cases where the array implementation is clearly smaller but it has the same complexity as it's node based counterpart. 

#### Time
| | Array Implementation | Node Implementation |
| :--: | :--: | :--: |
| find-max | O(1) | O(1) |
| delete-max | O(log n) | O(log n) |
| insert | O(log n) | O(log n) |
| decrease | O(log n) | O(log n) |
| merge | O(n) | O(n) |

#### Array vs. Node Conclusion
The time completxity will be the same for the array and node implementations.  The space complexity is of the same magnitude, although admittedly the array version will have a smaller practicle footprint.  Since I am inclided to use the node version and the two are so similar in space and time, I am going to go with the node version.

## Algorithms
 - Breadth-First Search: TreeNode.add() uses BFS
 - Depth-First Search
 - Binary Search
 - Merge Sort
 - Quick Sort
