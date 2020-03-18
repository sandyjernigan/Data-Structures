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
        # max number of nodes
        self.limit = limit
        # current number of nodes - start with 0
        self.size = 0
        # DLL that holds the key-value entries
        self.order = DoublyLinkedList()
        # storage dict
        self.storage = {}
        # Most Recently Used Node
        self.head = None
        # Oldest Used Node
        self.tail = None

    def get(self, key):
        # if key exists, return the Node
        if key in self.storage:
            # Get the Node
            node = self.storage[key]
            # Move to Front
            self.order.move_to_front(node)
            # Returns the value associated with the key
            return node.value[1]
        else:
            # Returns None if the key-value pair doesn't exist in the cache
            return None

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
        # If key already exists in cache, overwrite the value
        if key in self.storage:
            # Get the Node
            node = self.storage[key]
            # Overwrite value
            node.value = (key, value)
            # Move to Front
            self.order.move_to_front(node)
            # Exit
            return
        
        # If at max capacity, remove oldest entry
        if self.size == self.limit:
            # delete old tail
            del self.storage[self.order.tail.value[0]]
            self.order.remove_from_tail()
            self.size -= 1

        # Add the given key-value pair to the cache to the head
        self.order.add_to_head((key, value))
        self.storage[key] = self.order.head
        self.size += 1
        
        # Get Results and Set to most-recently used entry (head)
        return self.get(key)