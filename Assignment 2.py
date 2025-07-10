# Define the Node class to store data and the next node reference
class Node:
    def __init__(self, data):
        self.data = data        # Store the data
        self.next = None        # Pointer to the next node

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None        # Initialize the head of the list

    def append(self, data):
        """Adds a new node with the specified data at the end of the list."""
        new_node = Node(data)
        if self.head is None:               # If the list is empty
            self.head = new_node           # New node becomes head
            return
        last = self.head
        while last.next:                   # Traverse to the last node
            last = last.next
        last.next = new_node               # Append the new node at the end

    def prepend(self, data):
        """Adds a new node with the specified data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head          # Point to the current head
        self.head = new_node               # Update head to new node

    def print_list(self):
        """Prints all elements in the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print node data
            current = current.next
        print("None")

    def remove(self, data):
        """Removes the first node with the specified data."""
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous is None:
                    # Node to remove is the head
                    self.head = current.next
                else:
                    # Skip over the current node
                    previous.next = current.next
                return
            previous = current
            current = current.next

        # If data is not found
        print("Node not found in the LinkedList!")


