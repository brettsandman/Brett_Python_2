# The Node class represents a single node in the binary tree.
# Each node holds a value and pointers to its left and right children.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# The BinaryTree class manages the overall tree structure.
class BinaryTree:
    def __init__(self):
        # The root is the starting point of the tree. Initially, it's empty.
        self.root = None

    # Public method to insert a new node into the tree.
    # It calls a private recursive helper method to do the actual insertion.
    def insert(self, value):
        if self.root is None:
            # If the tree is empty, the new node becomes the root.
            self.root = Node(value)
        else:
            # Otherwise, find the correct position recursively.
            self._insert_recursive(self.root, value)

    # Private recursive helper method for insertion.
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            # If the value is less, it goes to the left subtree.
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            # If the value is greater, it goes to the right subtree.
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        # Note: We are ignoring duplicate values in this simple implementation.

    # Public method for in-order traversal.
    # Visits the left subtree, then the root, then the right subtree.
    def in_order_traversal(self):
        print("In-order Traversal:", end=" ")
        self._in_order_recursive(self.root)
        print()

    # Private recursive helper method for in-order traversal.
    def _in_order_recursive(self, current_node):
        if current_node:
            self._in_order_recursive(current_node.left)
            print(current_node.value, end=" ")
            self._in_order_recursive(current_node.right)

    # Public method for pre-order traversal.
    # Visits the root, then the left subtree, then the right subtree.
    def pre_order_traversal(self):
        print("Pre-order Traversal:", end=" ")
        self._pre_order_recursive(self.root)
        print()

    # Private recursive helper method for pre-order traversal.
    def _pre_order_recursive(self, current_node):
        if current_node:
            print(current_node.value, end=" ")
            self._pre_order_recursive(current_node.left)
            self._pre_order_recursive(current_node.right)

    # Public method for post-order traversal.
    # Visits the left subtree, then the right subtree, then the root.
    def post_order_traversal(self):
        print("Post-order Traversal:", end=" ")
        self._post_order_recursive(self.root)
        print()

    # Private recursive helper method for post-order traversal.
    def _post_order_recursive(self, current_node):
        if current_node:
            self._post_order_recursive(current_node.left)
            self._post_order_recursive(current_node.right)
            print(current_node.value, end=" ")


# --- Test Cases ---
if __name__ == "__main__":
    # 1. Create a new BinaryTree instance
    tree = BinaryTree()

    # 2. Insert some values into the tree
    print("Inserting values: 50, 30, 70, 20, 40, 60, 80")
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    # 3. Perform and print the three types of traversal
    # In-order traversal should output a sorted list of the values.
    tree.in_order_traversal()

    # Pre-order traversal is useful for creating a copy of the tree.
    tree.pre_order_traversal()

    # Post-order traversal is useful for deleting the tree.
    tree.post_order_traversal()

