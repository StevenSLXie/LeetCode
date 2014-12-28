class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        s2 = clean(s)
        
        return palindrome(s2)
        
def clean(s):
    s2 = []
    for i in list(s):
        if (i >= '0' and i <= '9') or (i >= 'a' and i <='z') or (i >= 'A' and i <= 'Z'):
            s2.append(i.upper())
    return s2
        
        
def palindrome(s):
    mid = len(s)/2
    if isOdd(s):
        # stehets
        for i in range(mid):
            if s[mid-i-1] != s[mid+i+1]:
                return False
        return True
    else:
        # sefhhfes
        for i in range(mid):
            if s[mid+i] != s[mid-1-i]:
                return False
        return True
    
def isOdd(s):
    if len(s) % 2 == 0:
        return False
    else:
        return True
    
