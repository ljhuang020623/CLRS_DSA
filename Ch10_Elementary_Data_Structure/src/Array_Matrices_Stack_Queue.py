import unittest
"""
Chapter 10: Elementary Data Structures

This chapter examines the representation of dynamic sets by simple data structures that use pointers.
Although many complex data structures can be built using pointers, this chapter focuses on the rudimentary ones:
arrays, matrices, stacks, queues, linked lists, and rooted trees.

10.1 Simple array-based data structures: arrays, matrices, stacks, queues

10.1.1 Arrays
-------------
An array is stored as a contiguous block of memory. In most programming languages, if the first element of an array
is at a starting memory address (say, A) and each element occupies a fixed number of bytes (say, b), then the nth
element (using 0-indexing) resides at the memory address computed as:

    Address = A + (n * b)

For example:
- The 0th element occupies addresses A to A + b - 1.
- The 1st element occupies addresses A + b to A + 2*b - 1.

This fixed-size layout allows constant-time access to any element, assuming that all memory locations are equally
accessible (as in the RAM model). Most programming languages require each element of an array to be of the same size.
If elements vary in size, the array typically stores pointers to objects rather than the objects themselves.

"""

# ===========================
# Implementation in Python
# ===========================

class Array:
    """
    A simple array implementation that mimics a contiguous block of memory.

    Attributes:
        capacity (int): The fixed size of the array.
        data (list): Underlying storage for array elements.
    """
    def __init__(self, capacity, initial=None):
        """
        Initialize the array with a given capacity.

        Parameters:
            capacity (int): The number of elements the array can hold.
            initial: The initial value for each element (default is None).
        """
        self.capacity = capacity
        self.data = [initial] * capacity  

    def __getitem__(self, index):
        """
        Retrieve the element at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not (0 <= index < self.capacity):
            raise IndexError("Array index out of bound")
        return self.data[index]

    def __setitem__(self, index, value):
        """
        Set the element at the specified index to the given value.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not (0 <= index < self.capacity):
            raise IndexError("Array index out of bounds")
        self.data[index] = value

    def __len__(self):
        """
        Return the capacity of the array.
        """
        return self.capacity

    def __iter__(self):
        """
        Return an iterator over the array elements.
        """
        return iter(self.data)

"""

10.1.2 Matrices
--------------
A matrix (or two-dimensional array) is generally represented using one or more one-dimensional arrays. The two most 
common methods are row-major and column-major order. In row-major order, an m×n matrix is stored row by row, while 
in column-major order, it is stored column by column. Alternative strategies involve storing each row (or column) in its 
own array and maintaining a separate array of pointers to these rows (or columns). Single-array representations are 
usually more efficient, while multiple-array approaches offer flexibility, such as supporting ragged arrays.

(m x n matrix)
If the row, columns and the single array all are indexed starting at s, then M[i,j] the element in row i and column j 

row major order index: s + (n(i - s)) + (j - s)
column major order index: s + (m(j - s)) + (i - s)
"""

class Matrix:

    """
    Represents an m x n matrix stored in a single one-dimensional list using row-major order.
    """
    def __init__(self, rows, cols, initial=None):
        self.rows = rows
        self.cols = cols
        # Allocate a list to store all elements (row-major order)
        self.data = [initial] * (rows * cols)

    def index(self, i, j):
        """
        Compute the index in the single list for the element at row i and column j.
        (Assumes 0-origin indexing.)
        """
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            raise IndexError("Matrix index out of bounds")
        return i * self.cols + j

    def get(self, i, j):
        """
        Return the element at row i, column j.
        """
        return self.data[self.index(i, j)]

    def set(self, i, j, value):
        """
        Set the element at row i, column j to the given value.
        """
        self.data[self.index(i, j)] = value

"""
10.1.3 Stacks 
-------------------------
A stack is a dynamic data structure that follows the Last-In, First-Out (LIFO) principle.
This means the most recently inserted element is the first one to be removed.

Key Characteristics:
--------------------
- LIFO Behavior:
  The last element pushed onto the stack is the first element popped off.

- Main Operations:
  - PUSH: Inserts an element onto the stack.
    * In an array-based implementation, this involves incrementing a pointer (or index) and placing the new element at that position.
  - POP: Removes and returns the top element from the stack.
    * This operation decrements the pointer, effectively "forgetting" the removed element.
  - STACK-EMPTY: A check to determine if the stack contains any elements.
    * When the pointer (e.g., 'top') indicates an empty state (such as a value of -1), the stack is empty.

- Error Conditions:
  - Underflow: Occurs when attempting to pop an element from an empty stack.
  - Overflow: In fixed-size implementations (such as an array-based stack), an error is raised when trying to push an element onto a full stack.

"""

class Stack:
    """
    Implements a stack (LIFO) using a fixed-size list (array).
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity  # underlying array storage
        self.top = -1  # when top == -1, the stack is empty

    def is_empty(self):
        return self.top == -1

    def push(self, item):
        if self.top == self.capacity - 1: # if the capacity is 5 then the max index is 4. thus means it is full cant push onto the stack
            raise IndexError("Stack overflow")
        else:
            self.top = self.top + 1
            self.data[self.top] = item
    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        else:
            value = self.data[self.top]
            self.top -= 1
            return value



class Queue:
    """
    Implements a FIFO queue using a fixed-size list (array) with circular wrap-around.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0  # index of the current head element
        self.tail = 0  # index where the next element will be enqueued
        self.size = 0  # current number of elements in the queue

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return self.size == 0

    def is_full(self):
        """
        Check if the queue is full.
        """
        return self.size == self.capacity

    def enqueue(self, item):
        """
        Add an item to the tail of the queue.
        Raises an error if the queue is full.
        """
        if self.is_full():
            raise IndexError("Queue overflow")
        self.data[self.tail] = item
        # Move tail forward, wrapping around if necessary.
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """
        Remove and return the item from the head of the queue.
        Raises an error if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue underflow")
        item = self.data[self.head]
        # Move head forward, wrapping around if necessary.
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item


# ========================================
# Unit Testing using Python's unittest
# ========================================

