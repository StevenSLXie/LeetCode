class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
            
        d = 0
        while s[-(d+1)]==' ':
            d += 1
            if d == len(s):
                return 0
            
        for i in range(d,len(s)):
            if s[-(i+1)] == ' ':
                return i-d
                
        return len(s)-d
        
