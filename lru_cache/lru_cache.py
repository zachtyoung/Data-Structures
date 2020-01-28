import sys
sys.path.append('../doubly_linked_list')
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
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.


    """
    def get(self, key):
        if key in self.storage:
            self.order.move_to_end(key)
            return self.storage[key]
        else:
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
        if key in self.storage: 
            self.storage[key]= value
        else: 
            self.storage[key] = value
            self.size +=1

        if self.size == self.limit:
            self.order.remove_from_head() #LFU
            self.order.add_to_tail(value) #MFU
        else: 
            self.order.add_to_tail(value)
 
 #1 Are we at max capactiy? Is self.size == self.limit ?
 #   Yes? - Head needs to be removed, insert value to tail
 #   No?  - insert to tail

 #Look up key in dictionary
 # If it exsists update key with new value
 #If it doesnt exist, insert new key value pair
