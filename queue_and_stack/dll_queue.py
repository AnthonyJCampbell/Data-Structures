

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        # storage should be initialized with a single Node that contains neither value nor next
        self.storage = Node()

    # add an item to the back of the queue
    def enqueue(self, value):
        # Create a new node
        new_node = Node(value)

        # If there's no 'value' for the first item in the queue, we're dealing with an empty cueue
        if self.storage.value is None:
            self.storage = new_node

        else:
            # Set new node's poiner to the current head node
            new_node.next = self.storage
            # make new node be at the end of the queue
            self.storage = new_node
            
        # Add one to size
        self.size += 1

    # remove and return an item from the front of the queue.
    def dequeue(self):
        # If there's zero items in que, return None
        if self.size is 0:
            return None

        else:
            # We need to loop over the queue to reach the first element (where next == none)

            # Then, we need to set value to None and storage to none

            # Decrement one from self.size
            self.size -= 1
            # Return dequeued value


    # Returns num of items in queue
    def len(self):
        return self.size

q = Queue()
q.enqueue(7)
print(q.size)
q.enqueue(10)
print(q.size)
q.enqueue(14)
print(q.size)
# print(q.storage.value)
# print(f"Next: {q.storage.next}")
# q.enqueue(10)
# print(q.storage.value)
# print(f"Next: {q.storage.next.value}")
# q.enqueue(14)
# print(q.storage.value)
# print(f"Next: {q.storage.next.value}")

q.dequeue()
print(q.size)

