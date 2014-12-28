class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        
        prefix = ''
        for i in range(shortestString(strs)):
            tmp = strs[0][i]
            for str in strs:
                if str[i] != tmp:
                    return prefix
            prefix += tmp
        return prefix
        
def shortestString(strs):
    #import sys
    #min = sys.maxint
    min = 100000
    for str in strs:
        if len(str)<min:
            min = len(str)
            
    return min
    
    
