from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # Max number of nodes
        self.limit = limit
        # Current number of nodes
        self.size = 0
        # DLL
        self.list = DoublyLinkedList()
        # Storage {}
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key not in self.storage
            # return None

        # return_val = self.storage.key
        # Move node to front

        
        # return return_val

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # We're creating a new node

        # IF self.size > self.limit
            # we have to remove the item at the tail
            # Add node to head
        
        # if key in self.storage:
            # Remove Key from self.storage
            # add node to HEAD
            # set self.storage.key to new value

        # else (if we're below the limit and the new key is not yet in the cache)
            # Add node to HEAD
            # set self.storage.key to new value
        pass
