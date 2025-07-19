# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data    # Store the value
        self.next = None    # Pointer to the next node

# Helper function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Recursive function to reverse the linked list
def reverse_recursive(head):
    # Step 1: Base Case
    # If the list is empty or has only one node, it is already reversed
    if head is None or head.next is None:
        return head

    # Step 2: Recursively reverse the rest of the list
    # This will eventually reverse the entire list except the current head
    new_head = reverse_recursive(head.next)

    # Step 3: Reverse the pointer
    # At this point, head.next is the last node in the smaller reversed list
    # So we make that node point back to the current head
    head.next.next = head

    # Step 4: Cut the current node's forward link to avoid a cycle
    head.next = None

    # Step 5: Return the new head of the reversed list
    return new_head

# Create the original linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print the original list
print("Original List:")
print_list(head)

# Reverse the list using the recursive function
reversed_head = reverse_recursive(head)

# Print the reversed list
print("Reversed List:")
print_list(reversed_head)
