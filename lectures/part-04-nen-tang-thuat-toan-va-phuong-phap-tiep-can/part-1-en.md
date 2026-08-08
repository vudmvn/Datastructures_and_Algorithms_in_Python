# Part I — Foundations of Algorithms and Data Structures

**Last updated:** August 03, 2026

## 1. Learning Objectives

This section provides the conceptual foundation before diving into specific data structures and algorithm analysis techniques. The goal is not only to memorize individual definitions, but also to understand the relationship between problems, data, algorithms, programs, and data structures.

After this section, learners will be able to:

- distinguish between **problem**, **input**, **output**, **algorithm**, and **program**;
- explain what an algorithm is and state the basic properties of an algorithm;
- distinguish between **data type**, **data structure**, and **Abstract Data Type — ADT**;
- recognize basic data structures and describe the typical use cases of each structure;
- clearly explain common operations on data structures such as access, search, insert, delete, update, and traverse;
- explain the relationship between algorithms and data structures;
- evaluate a solution based on three basic criteria: **correctness**, **efficiency**, and **scalability**.

---

## 2. Problems, Inputs, Outputs, Algorithms, and Programs

When solving a problem with a computer, we usually go through a sequence of thinking steps. First, we need to accurately define the problem to be solved, next describe the input data and output results, then select or design a suitable algorithm, and finally implement that algorithm with a specific program.

This process can be visualized as follows:

```text
Problem
    ↓
Input and Output Specification
    ↓
Algorithm
    ↓
Data Structures
    ↓
Program
```

Each component plays its own role. If the problem is described unclearly, the algorithm might solve the wrong goal. If input and output are not specified accurately, it is very difficult to evaluate correctness. If an inappropriate data structure is chosen, a correct algorithm can still perform inefficiently.

### 2.1. Problem

A **problem** is a task or question to be solved.

A computational problem typically describes:

- what data is provided;
- what processing needs to be performed;
- what results must be generated;
- what constraints must be satisfied.

Example:

> Given a list of integers and a `target` value. Determine the first position of `target` in the list. If `target` does not appear, return `-1`.

This is a search problem. The problem description is not yet an algorithm, because it only says **what to find**, not **how to find it**.

### 2.2. Input

The **input** is the data provided to the algorithm before processing begins.

In the above example:

```text
arr = [7, 2, 9, 4, 1]
target = 4
```

We have two inputs:

- `arr`: a list of integers;
- `target`: the value to find.

When describing input, it is recommended to clarify:

- data type;
- number of elements;
- value domain;
- special constraints.

Example:

```text
Input:
- n: a positive integer
- A: an array of n integers
- target: the integer to find
```

Defining input clearly is very important because algorithms can be designed differently depending on data characteristics. For instance, searching on a sorted array is different from searching on an unsorted array.

### 2.3. Output

The **output** is the result that the algorithm must produce after processing the input.

With the example:

```text
arr = [7, 2, 9, 4, 1]
target = 4
```

The output is:

```text
3
```

if the index starts from `0`.

A good output specification needs to clearly state:

- result type;
- meaning of the result;
- how to handle special cases.

Example:

```text
Output:
- the first index i such that A[i] = target;
- return -1 if target does not exist.
```

### 2.4. Algorithm

An **algorithm** is a finite procedure consisting of well-defined steps to transform input into output.

A Linear Search algorithm can be described by the idea:

1. start from the first element;
2. compare each element with `target`;
3. if found, return the position;
4. if traversed completely without finding it, return `-1`.

Implemented in Python:

```python
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1
```

The key point is that the algorithm describes **how to solve the problem**, not just stating input and output requirements.

### 2.5. Program

A **program** is a concrete implementation of an algorithm using a programming language.

The same Linear Search algorithm can be written in:

- Python;
- C++;
- Java;
- Rust;
- or many other languages.

The algorithmic idea does not change, but specific programs may differ in:

- syntax;
- data types;
- memory management;
- libraries used;
- implementation details.

It can be summarized as:

> **Algorithm is the method of solution; program is the concrete implementation of that method using a programming language.**

---

## 3. What Is an Algorithm?

An **algorithm** is a finite sequence of well-defined instructions aimed at solving a problem or performing a computation.

This process can be visually described by a diagram:

```text
Input
    ↓
Finite sequence of well-defined steps
    ↓
Output
```

Or concisely written as:

```text
Input → Algorithm → Output
```

The core point is that an algorithm must receive data, perform a sequence of steps with clear logic, and produce a result after a finite number of steps.

For example, consider the problem of finding the maximum value in a non-empty array:

```python
def find_max(arr):
    maximum = arr[0]

    for value in arr[1:]:
        if value > maximum:
            maximum = value

    return maximum
```

The above algorithm operates on the principles:

1. assume the first element is the maximum;
2. sequentially compare the remaining elements with the current maximum value;
3. update the maximum value when a larger element is found;
4. return the result after traversing the entire array.

This example shows that an algorithm is not just code. Before writing a program, we already have a logical process independent of programming languages.

---

## 4. Properties of Algorithms

For a procedure to be considered an algorithm, it needs to satisfy several basic properties. These properties help ensure that the algorithm is clearly described, executable, and produces correct results.

### 4.1. Input

An algorithm may receive zero inputs or one or more inputs, but the input data must be clearly specified.

Example:

```text
Input:
- n: a positive integer
- A: an array of n integers
```

In practice, describing input usually needs to be accompanied by constraints. For example:

```text
1 ≤ n ≤ 100000
-10^9 ≤ A[i] ≤ 10^9
```

These constraints can directly affect the choice of algorithms and data structures.

### 4.2. Output

An algorithm must produce at least one output result or an observable state.

Example:

```text
Output:
- maximum value in array A.
```

A well-described output must be clear enough so that we can verify whether the algorithm returns the correct result.

### 4.3. Definiteness

Each step of the algorithm must be clear and unambiguous.

Bad example:

```text
Pick a sufficiently large number.
```

This sentence does not point out what "sufficiently large" means.

Better example:

```text
Set maximum to the first element of the array.
```

The more complex an algorithm is, the more important the requirement for clarity becomes. Vague descriptions can lead to multiple interpretations and lose the ability to verify correctness.

### 4.4. Finiteness

An algorithm must terminate after a finite number of steps for all valid inputs.

The following example does not terminate:

```python
while True:
    pass
```

For recursive algorithms, there must be a **base case** to ensure the function call process does not continue infinitely.

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

### 4.5. Effectiveness

Each step of the algorithm must be sufficiently basic so that it can be carried out in a finite amount of time.

Operations such as:

- value assignment;
- addition, subtraction, multiplication, division;
- comparison;
- element access;
- calling a well-defined procedure;

are all executable operations.

A description like:

```text
Immediately find the optimal solution for any problem.
```

is not an effective step in the algorithmic sense, because it does not specify how to perform it.

### 4.6. Correctness

An algorithm must return the correct result for all valid inputs.

For example, an algorithm finding the maximum value must return an element that is no smaller than any other element in the data.

Correctness can be evaluated by:

- logical reasoning;
- proof;
- loop invariant;
- induction;
- testing on typical and edge cases.

Testing can help detect errors, but is not always sufficient to prove that the algorithm is correct for all inputs.

### 4.7. Deterministic and Randomized Algorithms

Not all algorithms are deterministic.

- **Deterministic algorithm**: given the same input, the algorithm always executes the same sequence of steps and produces the same result.
- **Randomized algorithm**: the algorithm may use random choices during execution.

For example, Randomized Quick Sort may select a pivot randomly. Two runs on the same input may produce different sequences of partitions.

However, randomness does not deprive an algorithm of its fundamental nature. The essential point is that the procedure must be clearly defined and have appropriate correctness criteria.

---

## 5. What Is a Data Structure?

As the volume of data grows, storing individual values in variables is no longer sufficient. We need a systematic way to organize data so that required operations can be performed efficiently.

A **data structure** is a way of organizing, storing, and managing data to support operations such as access, search, insert, delete, and traverse.

For example:

- a list of score points can be stored using an array;
- undo operation history can be managed using a stack;
- a customer waiting queue can be modeled using a queue;
- a road network can be represented using a graph;
- key-value pairs can be stored using a hash table.

The key point is that the same dataset can be organized in multiple different ways, and each way has its own advantages for specific operations.

> **There is no single best data structure for all problems. The appropriate structure is the one that most efficiently supports the most frequently used operations.**

---

## 6. Common Operations on Data Structures

Before learning each data structure, it is necessary to understand basic operations commonly performed on data. This is also the basis for comparing data structures with one another.

### 6.1. Access

**Access** is the operation of directly retrieving an element at a specific position or via a specified address.

Example with array:

```python
values = [10, 20, 30, 40]
print(values[2])
```

Output:

```text
30
```

In an array, accessing by index is typically a very efficient operation.

### 6.2. Search

**Search** is the operation of finding an element that satisfies a condition or has a specific value.

Example:

```python
def find_value(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i

    return -1
```

Search can be performed in various ways depending on the data structure, such as Linear Search, Binary Search, hash lookup, or tree search.

### 6.3. Insert

**Insert** is the operation of adding a new element into the data structure.

Example:

```python
values = [10, 20, 30]
values.append(40)
```

The insertion position can be:

- beginning;
- end;
- middle;
- a position determined by key or priority.

Insertion cost heavily depends on the data structure.

### 6.4. Delete

**Delete** is the operation of removing an element from the data structure.

Example:

```python
values = [10, 20, 30, 40]
values.remove(30)
```

Some structures support efficient deletion when the position or node is already known, while other structures may require shifting multiple elements.

### 6.5. Update

**Update** is the operation of modifying the value of an existing element.

Example:

```python
scores = [7.5, 8.0, 9.0]
scores[1] = 8.5
```

Update differs from insert in that it does not increase the number of elements.

### 6.6. Traverse

**Traverse** is the operation of visiting elements of the data structure in a specific order.

Example with list:

```python
for value in values:
    print(value)
```

With a tree or graph, traversal can use different strategies such as DFS or BFS.

### 6.7. Membership Test

**Membership test** checks whether an element belongs to the data structure.

Example:

```python
visited = {1, 3, 5}

print(3 in visited)
```

Output:

```text
True
```

The same membership test can have very different costs on a list, set, hash table, or tree.

### 6.8. Find Minimum / Maximum

This operation determines the smallest or largest element according to an ordering or priority criterion.

Example:

```python
values = [7, 2, 9, 4]
print(min(values))
print(max(values))
```

A heap or priority queue is specially designed to support retrieving the element with the highest or lowest priority efficiently.

### 6.9. Predecessor / Successor

Suppose elements have an order.

- **Predecessor** of an element is the largest element smaller than it.
- **Successor** is the smallest element larger than it.

For example, in the set:

```text
{2, 5, 8, 12}
```

for element `8`:

```text
Predecessor = 5
Successor = 12
```

These operations are particularly important in ordered sets and balanced search trees.

### 6.10. Merge

**Merge** is the operation of combining two data structures or two datasets into a new structure.

Example:

```text
A = [1, 3, 5]
B = [2, 4, 6]
```

Can be merged into:

```text
[1, 2, 3, 4, 5, 6]
```

Merge is a core operation in Merge Sort and many advanced data structures.

### 6.11. Split

**Split** is the operation of dividing a data structure into two or more parts according to a condition.

Example:

```text
[1, 2, 3, 4, 5, 6]
```

split at the middle position into:

```text
[1, 2, 3]
[4, 5, 6]
```

Split appears in divide-and-conquer, balanced trees, and many partitioning algorithms.

### 6.12. Summary of Operations

| Operation | Concise Definition |
|---|---|
| Access | Directly retrieve an element at a specified position or address |
| Search | Find an element satisfying a condition or having a specific value |
| Insert | Add a new element |
| Delete | Remove an element |
| Update | Change the value of an existing element |
| Traverse | Visit elements in a specific order |
| Membership | Check whether an element belongs to the structure |
| Min/Max | Find the smallest or largest element |
| Predecessor/Successor | Find the immediately preceding or following element in order |
| Merge | Combine two structures or datasets |
| Split | Divide a structure into multiple parts |

---

## 7. Abstract Data Types

An **Abstract Data Type — ADT** is an abstract model describing data and the operations allowed on that data.

An ADT typically specifies:

1. a set of data objects;
2. a set of supported operations;
3. the expected behavior of each operation.

ADT focuses on the question:

> **What does this structure allow doing, and how should operations behave?**

While implementation focuses on the question:

> **How is data stored in memory, and what algorithms implement the operations?**

### Example: Stack ADT

A Stack typically supports:

- `push(x)`: add element `x` to the top of the stack;
- `pop()`: retrieve and remove the top element;
- `top()` or `peek()`: view the top element without removing it;
- `is_empty()`: check whether the stack is empty.

A Stack operates on the principle:

```text
LIFO = Last-In, First-Out
```

Meaning the element added last will be retrieved first.

A Stack can be implemented using:

- array;
- dynamic array;
- linked list.

Different implementations can still provide the same Stack ADT interface, but time cost, memory, and capacity management may differ.

> **ADT describes interface and behavior; data structure implementation describes how data is organized and operations are implemented.**

---

## 8. Basic and Commonly Used Data Structures

The following data structures appear frequently in programming, algorithms, data science, artificial intelligence, and operations research. Each structure is suitable for a specific group of operations and problem types.

### 8.1. Array / Dynamic Array

Array stores elements in a linear order and usually supports access by index.

Example:

```python
values = [10, 20, 30, 40]
print(values[2])
```

Output:

```text
30
```

Array is suitable when needing:

- fast access by index;
- sequential traversal;
- storing data in order.

Dynamic array allows the size to increase or decrease during runtime. Python `list` is a typical example of a dynamic array.

### 8.2. Linked List

Linked List consists of nodes, where each node contains data and one or more links to other nodes.

Linked List is suitable when:

- insertion or deletion at a known position is needed;
- fast random access by index is not required;
- structure size changes frequently.

An important difference from array is that nodes do not necessarily lie contiguously in memory.

### 8.3. Stack

Stack is a linear structure operating on the principle:

```text
LIFO = Last-In, First-Out
```

An intuitive example is a stack of plates: the plate placed last will be removed first.

Applications:

- DFS;
- backtracking;
- expression evaluation;
- undo operations;
- call stack.

### 8.4. Queue

Queue operates on the principle:

```text
FIFO = First-In, First-Out
```

The element pushed first will be retrieved first.

Applications:

- BFS;
- task scheduling;
- waiting lines;
- simulations;
- processing requests in arrival order.

### 8.5. Deque

Deque, short for **double-ended queue**, allows insertion and deletion at both ends.

Applications:

- sliding window;
- monotonic queue;
- palindrome processing;
- certain BFS variants.

Deque is more flexible than a standard queue because it does not restrict operations to one input end and one output end.

### 8.6. Hash Table / Dictionary / Map

Hash Table stores data in mapping form:

```text
key → value
```

Example in Python:

```python
student = {
    "name": "Minh",
    "score": 9.0
}
```

Lookup, insertion, and deletion operations by key usually have an expected time close to `O(1)` under normal conditions.

Hash table is especially suitable when needing:

- fast key lookup;
- frequency counting;
- caching;
- indexing.

### 8.7. Set

Set stores distinct elements and does not allow duplicate values in the sense of equality.

Example:

```python
visited = {1, 3, 5}
```

Applications:

- membership test;
- duplicate removal;
- set representation;
- intersection, union, and difference.

### 8.8. Priority Queue / Heap

Priority Queue manages elements along with priority levels. The element retrieved is not necessarily the one inserted first, but the element with the highest or lowest priority depending on convention.

Heap is a common structure for implementing Priority Queue.

Applications:

- Dijkstra;
- A*;
- event simulation;
- scheduling;
- branch-and-bound;
- maintaining top-k.

### 8.9. Tree

Tree represents hierarchical relationships among objects.

A node can have a parent node and child nodes.

Application examples:

- file system;
- organization hierarchy;
- syntax tree;
- decision tree.

Tree is particularly suitable for hierarchical data.

### 8.10. Binary Search Tree

Binary Search Tree — BST is a binary tree with order properties.

For a node with key `x`:

- keys in the left subtree are smaller than `x`;
- keys in the right subtree are larger than `x`;

under a simple convention with no duplicate keys.

In the case of a balanced tree, operations:

- search;
- insert;
- delete;

can achieve time:

```text
O(log n)
```

If the tree becomes severely unbalanced, cost can degrade to `O(n)`.

### 8.11. Graph

Graph consists of:

- vertices or nodes;
- edges representing relationships between objects.

Graph is suitable for modeling:

- road networks;
- social networks;
- computer networks;
- routing;
- dependency graphs;
- supply-chain networks.

Many important algorithmic problems such as shortest path, connectivity, and flow are modeled on graphs.

### 8.12. Disjoint Set / Union-Find

Disjoint Set, also called Union-Find, manages a collection of elements partitioned into disjoint subsets.

Two basic operations:

- `find(x)`: identify the representative of the set containing `x`;
- `union(x, y)`: merge two sets.

Applications:

- Kruskal's algorithm;
- connectivity;
- clustering;
- dynamic component merging.

With techniques like path compression and union by rank/size, Union-Find performs exceptionally well in practice.

---

## 9. Choosing a Data Structure Based on Operations

Choosing a data structure should start from the question:

> **Which operations appear most frequently in the algorithm?**

For example:

- If continuous access by index is needed, array is usually suitable.
- If push/pop operations follow LIFO, stack is a natural choice.
- If processing follows first-come, first-served order, queue is suitable.
- If multiple key lookups are needed, hash table is usually a good choice.
- If continuously retrieving the element with the best priority is needed, priority queue is suitable.
- If data represents a network of relationships, graph is a natural model.

Orientation table:

| Primary Need | Commonly Suitable Data Structure |
|---|---|
| Random access | Array |
| Frequent insertion/deletion at known position | Linked List |
| LIFO processing | Stack |
| FIFO processing | Queue |
| Two-ended operations | Deque |
| Fast key lookup | Hash Table |
| Membership queries | Set |
| Maintain min/max priority | Heap / Priority Queue |
| Hierarchical data | Tree |
| Ordered search | Balanced BST |
| Network relationships | Graph |
| Dynamic connectivity | Union-Find |

This table is for guidance only. A practical problem may require combining multiple data structures simultaneously.

---

## 10. The Relationship Between Algorithms and Data Structures

Algorithms and data structures should not be viewed in isolation.

An algorithm describes how data is processed, while a data structure determines how data is organized to support those operations.

A change in data organization can significantly alter performance.

### Example: Membership Test

Suppose we need to repeatedly check whether a value appears in the dataset.

With list:

```python
target in values
```

In the worst case, the entire list might have to be checked.

With hash set:

```python
target in values_set
```

Lookup typically has an expected time close to `O(1)`.

Thus, for the same logical operation — checking membership — different data structures can lead to very different performance.

It can be summarized as:

> **Algorithms transform data; data structures organize data so that algorithms can manipulate it efficiently.**

An important principle when designing algorithms is:

> **Identify dominant operations first, then select the data structure that best supports those operations.**

---

## 11. Correctness, Efficiency, and Scalability

When evaluating an algorithm, one should not merely ask "does the algorithm run". Three more important criteria are correctness, efficiency, and scalability.

### 11.1. Correctness

**Correctness** answers the question:

> Does the algorithm always produce correct results for all valid inputs?

Correctness is the most basic condition. An algorithm that runs very fast but returns wrong results has no value.

For example, with the algorithm finding the maximum value, the result must be no smaller than any other element in the data.

### 11.2. Efficiency

**Efficiency** examines the amount of resources used by the algorithm, primarily:

- time;
- memory.

Two algorithms can correctly solve the same problem yet differ significantly in performance.

Example:

```text
Linear Search:  Θ(n)
Binary Search:  Θ(log n)
```

However, Binary Search requires data to be sorted and support appropriate access.

Therefore, one should not evaluate an algorithm solely by a complexity notation while ignoring application conditions.

### 11.3. Scalability

**Scalability** describes the ability to maintain performance when the input size increases.

Example:

```text
n = 100
n = 10^6
n = 10^9
```

An `O(n²)` algorithm may perform well with `n = 100`, but becomes infeasible when `n` is very large.

Scalability depends on:

- growth rate of running time;
- required memory;
- data characteristics;
- parallelizability;
- hardware and system limits.

The key point is:

> **Correctness indicates whether the algorithm is correct; efficiency indicates how it uses resources; scalability indicates whether it remains feasible as the problem grows.**

---

## 12. Summary

Key points to remember:

- **Problem** specifies the task to be solved.
- **Input** describes the data provided.
- **Output** describes the result to be produced.
- **Algorithm** is a finite and well-defined procedure to transform input into output.
- **Program** is a concrete implementation of an algorithm using a programming language.
- An algorithm needs to have properties such as definiteness, finiteness, effectiveness, and correctness.
- **Data structure** organizes data to support efficient operations.
- Basic operations include access, search, insert, delete, update, traverse, membership, min/max, predecessor/successor, merge, and split.
- **ADT** describes data and behavior at an abstract level, independent of specific implementation.
- Common data structures include Array, Linked List, Stack, Queue, Deque, Hash Table, Set, Heap, Tree, BST, Graph, and Union-Find.
- There is no single best data structure for all problems.
- Selecting a data structure should be based on the most frequently performed operations.
- Algorithms and data structures have a close relationship and should be designed together.
- Correctness, efficiency, and scalability are three important criteria to evaluate a solution.
