import unittest
from Array_Matrices_Stack_Queue import Array, Matrix, Stack, Queue




class TestArray(unittest.TestCase):
    def test_array_set_get(self):
        # initialize the size of array into 10 
        A = Array(10)
        for i in range(len(A)):
            A[i] = i
        for i in range(len(A)):
            self.assertEqual(A[i], i)
        with self.assertRaises(IndexError):
            _ = A[10]


class TestMatrix(unittest.TestCase):
    def test_matrix_set_get(self):
        m = Matrix(2, 3)
        # Initialize matrix elements:
        #  1  2  3
        #  4  5  6
        m.set(0, 0, 1)
        m.set(0, 1, 2)
        m.set(0, 2, 3)
        m.set(1, 0, 4)
        m.set(1, 1, 5)
        m.set(1, 2, 6)
        
        self.assertEqual(m.get(0, 0), 1)
        self.assertEqual(m.get(0, 2), 3)
        self.assertEqual(m.get(1, 0), 4)
        self.assertEqual(m.get(1, 2), 6)
        with self.assertRaises(IndexError):
            m.get(2, 0)  # Out-of-bounds access

class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack(5)
        self.assertTrue(s.is_empty())
        
        s.push(10)
        s.push(20)
        s.push(30)
        
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)
        
        with self.assertRaises(IndexError):
            s.pop()  # Underflow: stack is empty now

    def test_stack_overflow(self):
        s = Stack(3)
        s.push(1)
        s.push(2)
        s.push(3)
        with self.assertRaises(IndexError):
            s.push(4)  # Overflow: capacity is 3

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        # Create a queue with capacity 5.
        q = Queue(5)
        self.assertTrue(q.is_empty())
        
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        # The queue now contains: 3, 4, 5 (in order)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 5)
        
        with self.assertRaises(IndexError):
            q.dequeue()  # Underflow: queue is empty

    def test_queue_overflow(self):
        q = Queue(3)
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        with self.assertRaises(IndexError):
            q.enqueue('d')  # Overflow: queue is full

if __name__ == "__main__":
    unittest.main()