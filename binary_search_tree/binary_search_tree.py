import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # `insert` adds the input value to the binary search tree, 
    # adhering to the rules of the ordering of elements in a binary search tree.
    # We'll need to traverse to find the spot to insert
    def insert(self, value):
        pass

    # `contains` searches the binary search tree for the input value, 
    # returning a boolean indicating whether the value exists in the tree or not.
    # Start from root and move down. Stop at the first instance of a value
    # If the traversal reaches a node without children, we know the value is not in the tree
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    #  performs a traversal of _every_ node in the tree, 
    #  executing the passed-in callback function on each tree node value. 
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass










    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterativ e breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
