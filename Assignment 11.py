# A simple implementation of a Node for the Binary Search Tree
class Node:
    """
    A single node in the Binary Search Tree.
    Each node holds a value and references to its left and right children.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    An implementation of a Binary Search Tree.
    Supports insertion of new nodes and searching for existing values.
    """

    def __init__(self):
        # The root of the tree, initially None
        self.root = None

    def insert(self, value):
        """
        Inserts a new value into the Binary Search Tree.
        If the tree is empty, the new value becomes the root.
        Otherwise, it recursively finds the correct position for the new node.
        """
        # If the tree is empty, the new node becomes the root
        if self.root is None:
            self.root = Node(value)
        else:
            # Otherwise, call the private recursive helper method
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        """
        A private recursive helper method to insert a value.
        Compares the new value with the current node's value to decide
        whether to go left or right.
        """
        if value < current_node.value:
            # Go left: if the left child is None, insert the new node here.
            # Otherwise, continue the recursion on the left child.
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursively(current_node.left, value)
        elif value > current_node.value:
            # Go right: if the right child is None, insert the new node here.
            # Otherwise, continue the recursion on the right child.
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursively(current_node.right, value)
        # Note: This implementation does not handle duplicate values.

    def search(self, value):
        """
        Searches for a value in the Binary Search Tree.
        Returns the node if the value is found, otherwise returns None.
        """
        return self._search_recursively(self.root, value)

    def _search_recursively(self, current_node, value):
        """
        A private recursive helper method to search for a value.
        Compares the target value with the current node's value to
        decide whether to go left or right.
        """
        # Base case 1: The current node is None, which means the value was not found.
        if current_node is None:
            return None

        # Base case 2: The value is found at the current node.
        if value == current_node.value:
            return current_node

        # Recursive step:
        elif value < current_node.value:
            # If the value is smaller, search the left subtree.
            return self._search_recursively(current_node.left, value)
        else:
            # If the value is larger, search the right subtree.
            return self._search_recursively(current_node.right, value)

    def in_order_traversal(self):
        """
        Helper method to perform an in-order traversal of the tree.
        Prints the nodes in sorted order.
        """
        result = []
        self._in_order_traversal_recursively(self.root, result)
        return result

    def _in_order_traversal_recursively(self, node, result):
        if node:
            self._in_order_traversal_recursively(node.left, result)
            result.append(node.value)
            self._in_order_traversal_recursively(node.right, result)


# --- Test Cases ---

if __name__ == "__main__":
    # Create a new Binary Search Tree instance
    bst = BinarySearchTree()

    # 1. Test insertion
    print("Inserting values: 50, 30, 70, 20, 40, 60, 80")
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Use the helper traversal method to verify the tree structure
    print("In-order traversal of the tree (should be sorted):", bst.in_order_traversal())
    print("-" * 30)

    # 2. Test search for an existing value
    search_value_1 = 40
    result_node_1 = bst.search(search_value_1)
    if result_node_1:
        print(f"✅ Found value {result_node_1.value} in the tree.")
    else:
        print(f"❌ Value {search_value_1} not found.")

    print("-" * 30)

    # 3. Test search for a value that does not exist
    search_value_2 = 99
    result_node_2 = bst.search(search_value_2)
    if result_node_2:
        print(f"✅ Found value {result_node_2.value} in the tree.")
    else:
        print(f"❌ Value {search_value_2} not found.")

    print("-" * 30)

    # 4. Test search for the root node
    search_value_3 = 50
    result_node_3 = bst.search(search_value_3)
    if result_node_3:
        print(f"✅ Found value {result_node_3.value} in the tree.")
    else:
        print(f"❌ Value {search_value_3} not found.")
