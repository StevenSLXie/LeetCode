class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = collections.OrderedDict()
    # @return an integer
    def get(self, key):
        if not key in self.items:
            return -1
        value = self.items.pop(key)
        self.items[key] = value
        return value
        
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            self.items.pop(key)
        except KeyError:
            if len(self.items) >= self.capacity:
                self.items.popitem(last=False)
        self.items[key] = value
