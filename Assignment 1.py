# Define the structure for each node in the list
class Node:
    def __init__(self, data):
        # Each node holds some data
        self.data = data
        # And a pointer to the next node in the list (initially None)
        self.next = None

# Define the singly linked list
class SinglyLinkedList:
    def __init__(self):
        # When the list is created, it starts out empty (no head node)
        self.head = None

    # Method to add a new node to the end of the list
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, start from the head and find the last node
        current = self.head
        while current.next:
            current = current.next  # Move one step forward in the list

        # Set the next of the last node to point to the new node
        current.next = new_node

    # Method to add a new node at the beginning of the list
    def prepend(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # Point the new node’s next to the current head
        new_node.next = self.head

        # Set the new node as the new head of the list
        self.head = new_node

    # Method to print all elements in the list
    def print_list(self):
        # Start from the head of the list
        current = self.head

        # Traverse the list and print each node’s data
        while current:
            print(current.data)
            current = current.next  # Move to the next node
