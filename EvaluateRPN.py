class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        l = []
        while len(tokens) > 0:
            temp = tokens.pop(0)
            if not self.isOperator(temp):
                l.append(int(temp))
            else:
                opt = temp
                y = l.pop()
                x = l.pop()
                l.append(self.operation(x,y,opt))
        return l[0]
        
    
    def operation(self,x,y,opt):
        if opt == '+':
            return x+y
        elif opt == '-':
            return x-y
        elif opt == '*':
            return x*y
        elif opt == '/':
            # note that the division in Python is floor
            if x*y < 0:
                return - (-x/y)
            return x/y
        
    def isOperator(self,opt):
        if opt in '+-*/':
            return True
        else:
            return False
