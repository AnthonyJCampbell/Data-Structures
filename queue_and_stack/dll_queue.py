

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.size = 0
        # storage should be initialized with a single Node that contains neither value nor next
        self.storage = Node()
        self.first = Node()

    # add an item to the back of the queue
    def enqueue(self, value):
        # Create a new node
        new_node = Node(value)

        # If there's no 'value' for the first item in the queue, we're dealing with an empty cueue
        if self.storage.value is None:
            self.storage = new_node
            self.first = new_node

        else:
            # Make sure the current head node knows what's going to be added after him.
            self.storage.prev = new_node
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

        # If que is only one item, we should remove the value and make the queue have an empty Node
        elif self.size is 1 and self.storage.next is None:
            self.storage = Node()

        # If self.size > 1, we should set the second value to be the first thereby moving up the queue
        else:
            print(self.first.next)
            

    # Returns num of items in queue
    def len(self):
        return self.size

q = Queue()
q.enqueue(7)
q.enqueue(10)
q.enqueue(14)
# print(q.storage.value)
# print(f"Next: {q.storage.next}")
# q.enqueue(10)
# print(q.storage.value)
# print(f"Next: {q.storage.next.value}")
# q.enqueue(14)
# print(q.storage.value)
# print(f"Next: {q.storage.next.value}")

q.dequeue()


