                Part 1: Implementation and Analysis of Selection Algorithms

1. Implementation: [Brilliant.org. (n.d.).]
The Median of Medians algorithm is a deterministic approach to selecting the k^th smallest element with worst-case O(n) time complexity. Please check median.py
Steps:
- Divide the input array into groups of 5 elements.
- Find the median of each group by sorting and selecting the middle element.
- Use the deterministic selection algorithm recursively to find the median of these medians.
- Partition the array around this median and recursively search either the left or right subarray based on the rank of the pivot.

2. Performance Analysis: [Li, C. (Chapter 10)]
- Deterministic Algorithm:
In the worst case, the deterministic algorithm achieves O(n) time complexity by dividing the array into five groups, finding medians, and recursively selecting the pivot.

- Randomized Algorithm:
The randomized algorithm has an expected time complexity of O(n). The randomly selected pivot divides the array so that approximately half the elements are in each partition.
However, O(n^2) is the worst-case time complexity when the pivot consistently partitions the array poorly.

- Space Complexity: [Li, C. (Chapter 10)]
The space complexity of the Deterministic Algorithm is O(n) due to the recursion stack and additional partitions created during the process.
The space complexity of the Randomized algorithm is O(1), as no extra space is required other than the input array and pivot-related partitions.

3. Empirical Analysis:
- The Randomized Selection algorithm is often faster in practice because it has a lower overhead than the Deterministic Selection algorithm.
- The performance differences are more noticeable on larger arrays.



                    Part 2: Elementary Data Structures Implementation and Discussion

1. Implementation:
Please check dataStruc.py for the implementation of basic data structures: arrays, stacks, queues, and linked lists. [Vedaldi, A. (2022)]

2. Performance Analysis:
                         Time Complexity [Vedaldi, A. (2022)]
- Array: Accessing an element by index is O(1), while insertion and deletion are O(n) due to shifting elements.
- Stack operations are O(1) because they occur at one end.
- Queue enqueue is O(1), but dequeue is O(n) due to list shifting.
- Linked List: Insertion at the end is O(n), and deletion/searching is also O(n).

                    Trade-Offs and Efficiency [Choi, E. (2022, January 14)]
- Arrays: Provide constant time access but require shifting elements during insertion and deletion, making them inefficient for large lists with frequent changes.
- Linked Lists: Allow efficient insertions and deletions without shifting but require linear time for access and traversal.
Arrays are efficient for stack operations since we only insert and remove from the top (end of the array), achieving O(1) for both.
Linked lists can provide better performance for queues when operations involve frequent dequeuing from the front (O(1) with linked lists vs O(n) with arrays).

3. Discussion: [Chy, D. (2020, October 4)]
- Array: In finance, arrays store historical stock prices or financial data for analysis and modeling.
In data science, arrays are instrumental in storing and manipulating large datasets for machine learning algorithms.
- Stacks: Used in function calls (call stack), depth-first search (DFS), expression evaluation, and undo operations in software applications.
- Queue: Useful in scheduling problems like task scheduling, breadth-first search (BFS), order processing, and resource management (e.g., CPU scheduling, print queues).
- Linked Lists: Ideal for applications where frequent insertions and deletions occur, such as in memory management, undo features in text editors, or dynamic data structures like hash maps or queues.

Linked lists require extra memory for pointers, making them less memory-efficient than arrays when space is constrained.
Arrays provide constant-time access, making them better for scenarios where access speed is critical, like databases and caching systems. Linked lists are more efficient for dynamic memory allocation scenarios where elements are frequently inserted or deleted.

                                        References

Brilliant.org. (n.d.). Median finding algorithm. Brilliant. https://brilliant.org/wiki/median-finding-algorithm/

Li, C. (n.d.). Chapter 10: Sorting. USTC. http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/chap10.htm

Vedaldi, A. (2022). Elementary data structures. University of Oxford. https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2022/b16/notes/3-elementary-data-structures.html

Choi, E. (2022, January 14). From pancakes to JavaScript: Implementing a stack data structure with array vs linked lists. Medium. https://medium.com/@estherchoi.sh/from-pancakes-to-javascript-implementing-a-stack-data-structure-with-array-vs-linked-lists-d151f7f908b4

Chy, D. (2020, October 4). Introduction to data structures with real-world examples. Medium. https://medium.com/@DevChy/introduction-to-data-structures-with-real-world-examples-15063e4adbad


