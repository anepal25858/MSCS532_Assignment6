# Array implementation
class Array:
    def __init__(self):
        self.array = []

    def insert(self, index, value):
        self.array.insert(index, value)

    def delete(self, index):
        if index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index out of bounds.")

    def access(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of bounds.")

# Test Case for Array
arr = Array()
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
print("Access element at index 1:", arr.access(1))
arr.delete(1)
print("Array after deletion:", arr.array)


# Matrix implementation
class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[None for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def insert(self, row, col, value):
        if row < self.rows and col < self.cols:
            self.matrix[row][col] = value
        else:
            print("Index out of bounds")

    def access(self, row, col):
        if row < self.rows and col < self.cols:
            return self.matrix[row][col]
        else:
            return "Index out of bounds"

# Stack implementation (LIFO - Last In, First Out)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

#Test Case
stack = Stack()
stack.push(5)
stack.push(10)
print("Peek at top element:", stack.peek())
stack.pop()
print("Stack after pop:", stack.stack)

# Queue implementation (FIFO - First In, First Out)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

# Test Case for Queue
queue = Queue()
queue.enqueue(15)
queue.enqueue(25)
print("Peek at front element:", queue.front())
queue.dequeue()
print("Queue after dequeue:", queue.queue)


#linked lists implementation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next
        if current:
            previous.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test Case for Singly Linked List
ll = SinglyLinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Linked List after insertion:")
ll.traverse()
ll.delete(20)
print("Linked List after deletion:")
ll.traverse()
