class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        
        returnable, val = preprocess(s)
        if returnable:
            return val
         
        r1, r2 = 1, 1 
        for i in range(1,len(s)):
            if s[i]!= '0':
                x = r1
            else:
                x = 0
            
            if int(s[i-1:i+1])<27 and s[i-1]!= '0':
                y = r2
            else:
                y = 0
            r1 = x + y
            r2 = x
        return r1
        
 
            
def isSome(char,some):
    if int(char) == some:
        return True
    return False
    
def preprocess(s):
    if len(s) == 0:
        # empty string
        return True, 0
    if int(s) == 0:
        # string of zero value
        return True, 0
    if str(int(s)) != s:
        # with one or more zeros as prefix
        return True,0
    if len(s) == 1:
        # one digit from 1 to 9
        return True, 1
        
    return False,None
    
    

    
        
