class Solution:
    # @return a boolean
    def isValid(self, s):
        s2 = []
        for i in range(len(s)):
            if s[i] in '([{':
                s2.append(s[i])
            else:
                if len(s2) == 0:
                    return False
                left = s2.pop()
                if not self.match(left,s[i]):
                    return False
        if len(s2) == 0:
            return True
        else:
            return False
                
        
    def match(self,left,right):
        leftList = '([{'
        rightList = ')]}'
        if leftList.index(left) == rightList.index(right):
            return True
        else:
            return False
