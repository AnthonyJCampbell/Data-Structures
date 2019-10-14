

class Node:
    def __init__(self, value=None, next=None):
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
            # connect new Node to previous HEAD node
            new_node.next = self.storage
            print(new_node.next)
            # make new Node new HEAD node
            self.storage = new_node
            
        # Add one to size
        self.size += 1

    def dequeue(self):
        # remove and return an item from the front of the queue.
        print(self.storage.value)

    # Returns num of items in queue
    def len(self):
        return self.size

q = Queue()
q.enqueue(7)
q.enqueue(10)
q.enqueue(14)
q.dequeue()




