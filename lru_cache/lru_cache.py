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
        # DLL
        self.storage = DoublyLinkedList()
        # Cache {}
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.cache:
            return None

        # return_val itself is now the object associated with the key in cache
        return_val = self.cache[key]

        # Move value to front of the storage
        self.storage.move_to_front(return_val)

        # Return the value of the K-V pair location in the 'value' of the Object in cache
        return return_val.value[1]
        

    """Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # If the key is already in the cache, we'll need to update it
        if key in self.cache:
            # Create a new 'node', which'll be passed to the DLL
            new_node = self.cache[key]
            # Set it's value attribute to be a tuple containing the key and value so it satisfies
            # The param requirements of Node()
            new_node.value = (key, value)
            # We should move the node in the DLL to the front, since we've requested it last.
            self.storage.move_to_front(new_node)
            

        elif self.storage.length >= self.limit:
            # Remove Key-value pair from cache, targetting the value that is current at tail
            del self.cache[self.storage.tail.value[0]]
            # Remove value from tail to ensure that the old value is removed and size is once again equal to limit
            self.storage.remove_from_tail()
        
        # Add new node to the head of storage by passing in (key, value) as value param for Node()
        self.storage.add_to_head((key, value))
        # Set cache at the designated key to have the value of the object
        self.cache[key] = self.storage.head

lru = LRUCache(2)
lru.set("item 1", "a")
lru.set("item 2", "b")
print(f"{lru.cache}\n")
lru.set("item 1", "a")
print(f"{lru.cache}\n")
lru.set("item 3", "c")
print(f"{lru.cache}\n")
print(lru.get("item 4"))
print(lru.get("item 3"))