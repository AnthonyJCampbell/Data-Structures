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
    def insert(self, new_value):

        # Create a recursive function that is able to iterate over the 'left' and 'right' nodes
        def recursive_insert(node, new_value):
            # If the new value is smaller than the value of the current node, we need to either move
            # left (if there's some value there), or insert the value to the left if we're at a leaf.
            if new_value < node.value:
                # If self.left is None, we should add the new node
                if node.left is None:
                    node.left = BinarySearchTree(new_value)
                    return
                
                # Rerun through the function using the child node on the left
                else:
                    recursive_insert(node.left, new_value)
            
            # If the new value >= the current value, we should move over to the right.
            else:
                if node.right is None:
                    node.right = BinarySearchTree(new_value)
                    return

                else:
                    recursive_insert(node.right, new_value)

        return recursive_insert(self, new_value)


    # `contains` searches the binary search tree for the input value, 
    # returning a boolean indicating whether the value exists in the tree or not.
    # Start from root and move down. Stop at the first instance of a value
    # If the traversal reaches a node without children, we know the value is not in the tree
    def contains(self, target):

        def recursive_contains(node, target):
            # print(f"target is {target}, current value is {node.value}")
            # If self.value == target, we've found it and should return it
            if node.value == target:
                return True

            # With each value, we check if the target is smaller than self.value or larger
            # If target is smaller than self.value
            elif target < node.value:
                # If self.left is None, it is not in the tree and should return False
                if node.left is None:
                    return False
                
                # Otherwise we should try again with the node on the left
                else:
                    return recursive_contains(node.left, target)

            # if target is equal or larger than self.value
            else:
                # if self.right is None, it is not in the tree and should return False
                if node.right is None:
                    return False

                # Otherwise rerun with the node on the right
                else:
                    return recursive_contains(node.right, target)

        return recursive_contains(self, target)
            





    # Return the maximum value found in the tree
    def get_max(self):
        # Move over every value in the tree
        
        def recursive_get_max(node):
            # Move over the tree
            # Normally, the largest value in a BST will end up as the right-most leaf

            # If node.right is None, this means that the current value is the largest we can find
            if node.right is None:
                # Therefore, we should return node.value
                return node.value

            else:
                # Rerun function with node.right as node
                return recursive_get_max(node.right)
        
        
        return recursive_get_max(self)





    #  performs a traversal of _every_ node in the tree, 
    #  executing the passed-in callback function on each tree node value. 
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Traverse all nodes in the tree

        # execute callback on self

        # If self.left exists
            # Recursive call with node.left passed as node

        # if self.right exists
            # Recursive call with node.right passed as node

        # if self.right is none and self.left is none
            # return





bst = BinarySearchTree(5)
arr = []
cb = lambda x: arr.append(x)

v1 = 2
v2 = 3
v3 = 8
v4 = 30
v5 = 30

bst.insert(v1)
bst.insert(v2)
bst.insert(v3)
bst.insert(v4)
bst.insert(v5)

bst.for_each(cb)

print(arr)









    # # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterativ e breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
