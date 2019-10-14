import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add to tail
        self.storage.add_to_tail(value)
        # Add 1 to size
        self.size += 1

    def dequeue(self):
        if self.size >= 1:
            # Remove from head
            return_val = self.storage.remove_from_head()
            # Subtract 1 from size
            self.size -= 1
            return return_val
        

    def len(self):
        return self.size
