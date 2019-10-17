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

        def recursive_for_each(node, cb):
            # Traverse all nodes in the tree

            # # execute callback on self
            cb(node.value)

            # if self.right is none and self.left is none, we've reached a dead end and should just return
            if node.right is None and node.left is None:
                return

            # If self.left exists
            if node.left is None:
                # Recursive call with node.left passed as node
                recursive_for_each(node.right, cb)

            # # if node.right exists
            if node.right is None:
                # Recursive call with node.right passed as node
                recursive_for_each(node.left, cb)

            if node.left is not None and node.right is not None:
                recursive_for_each(node.left, cb)
                recursive_for_each(node.right, cb)

        return recursive_for_each(self, cb)













    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Declare a holder list where all values can be stored as we encounter them
        holder = []
        
        # Recursive function
        def recursive_in_order_find(node):
            # Add value to holder
            holder.append(node.value)

            # if node.right is not None and node.left is not None, should rerun with both children nodes
            if node.right is not None and node.left is not None:
                # rerun function with node.right
                recursive_in_order_find(node.right)
                # rerun function with node.left
                recursive_in_order_find(node.left)

            # if node.right is None and node.left is not None
            if node.right is None and node.left is not None:
                # rerun function with node.left
                recursive_in_order_find(node.left)

            # if node.right is not None and node.left is None
            if node.right is not None and node.left is None:
                # rerun function with node.right
                recursive_in_order_find(node.right)

            else:
                return
        
        
        # Call the recursive function with the root node
        recursive_in_order_find(node)

    
        # Take the holder list (which by now contains all values in the tree) and sort them
        holder.sort()

        # Loop over the values in the tree and print them in order
        for values in holder:
            print(values)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # Store starting node as current value
        current = node
        # Initialize a stack
        stack = Stack()
        # Store the size of the tree to check against in the REPL
        tree_size = get_max(node)

        # Initiate a while loop that repeats while the finishing conditions do not match: 
        # current.left is not None 
        # current.right is not None
        # and current.value is not equal to tree_size
            
            # if current.value is not None:
                # print value
                # push to stack
                # set current to current.left

            # elif current is None and current.value is not equal to tree_size
                # store popped item
                # current = popped_item.right

        # If current.left and current.right are None + current.value == tree_size, we've reached the end

        # We should print the final value

        # return
        
        pass

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.dft_print(bst)


    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
