class MinStack:
    
    def __init__(self):
        self.ele = []
        self.min = float("inf")
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if x < self.min:
            self.min = x
        self.ele.append(x)
        return self.ele[len(self.ele)-1]
        
    # @return nothing
    def pop(self):
        a = self.ele.pop()
        if not self.isEmpty() and a == self.min:
            self.min = min(self.ele)
        elif self.isEmpty():
            self.min = float("inf")
        
    # @return an integer
    def top(self):
        return self.ele[len(self.ele)-1]
        
    # @return an integer
    def getMin(self):
        return self.min
        
    def isEmpty(self):
        if len(self.ele) == 0:
            return True
        else:
            return False
        
