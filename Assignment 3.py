class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.items = []

    def enqueue(self, item):
        # Add the item to the end (tail) of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front (head) of the queue
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        # Return True if the queue is empty, else False
        return len(self.items) == 0

    def size(self):
        # Return the number of items currently in the queue
        return len(self.items)

    def __str__(self):
        # Optional: neatly display the queue contents
        return "Queue: " + " -> ".join(str(item) for item in self.items)