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
        self.dll = DoublyLinkedList()
        # storage dict
        self.storage = {}
        # Most Recently Used Node
        self.head = None
        # Oldest Used Node
        self.tail = None

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key exists, return the Node
        if key in self.storage:
            # Retrieves the value associated with the given key
            node = self.storage[key]
            results = self.storage[key].value

            # if node is already in most recent, just return value
            if node is self.head: return results

            # Remove Node by resetting Connections around Node
            if node.next: node.next.prev = node.prev
            if node.prev: node.prev.next = node.next

            # If Node is the tail, set a new tail
            if node is self.tail:
                self.tail = self.tail.prev

            # Update head node
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

            # Return the value associated with the key
            return results

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
            self.storage[key].value = value
        else:
            # if key doesn't exist
            # Add the given key-value pair to the cache to the head
            self.storage.add_to_head(key, value)
            self.storage[key] = self.head
            print(self.get(key))
            print(self.storage)
        
        # If Not at max capacity, update size
        if self.size < self.limit:
            self.size += 1
        
        # If at max capacity, remove oldest entry
        else:
            # Get key of current tail
            tailKey = self.tail.key

            # Adjust the tail position
            self.tail = self.tail.prev
            self.tail.next = None

            # delete old tail
            del self.storage[tailKey]
        
        # Get Results and Set to most-recently used entry (head)
        return self.get(key)


testCache = LRUCache()

testCache.set('item1', 'a')
testCache.set('item2', 'b')
testCache.set('item3', 'c')

print (testCache.get('item1'))