from collections import deque

class DequeQueue:
    def __init__(self):
        # Initialize an empty deque to store items
        self.queue = deque()

    def enqueue(self, item):
        # Add item to the end (right side) of the deque
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front (left side)
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.popleft()

    def is_empty(self):
        # Return True if queue is empty, False otherwise
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)


# Test cases to demonstrate functionality
if __name__ == "__main__":
    q = DequeQueue()

    print("Is queue empty?", q.is_empty())  # True
    print("Enqueue 10, 20, 30")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue size:", q.size())          # 3
    print("Is queue empty?", q.is_empty())  # False

    print("Dequeue item:", q.dequeue())     # 10
    print("Queue size after dequeue:", q.size())  # 2

    print("Dequeue item:", q.dequeue())     # 20
    print("Dequeue item:", q.dequeue())     # 30

    print("Is queue empty after all dequeues?", q.is_empty())  # True

    try:
        q.dequeue()  # Should raise an exception
    except IndexError as e:
        print("Exception caught:", str(e))
