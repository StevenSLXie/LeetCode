class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = {}
        self.recent = {}
        self.count = 0
        
    # @return an integer
    def get(self, key):
        if key in self.items:
            self.count += 1
            self.recent[key] = self.count
            return self.items[key]
        else:
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.items:
            return
        
        if len(self.items) == self.capacity:
            min_key = min(self.recent,key=self.recent.get)
            self.items.pop(min_key,None)
            self.recent.pop(min_key,None)
            
        self.items[key] = value
        self.recent[key] = 0
