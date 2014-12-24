class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        #import operator
        s = {}
        for n in num:
            s = count(s, n)
        #mar = max(s.iteritems(), key=operator.itemgetter(1))[0]
        mar = max(s, key=s.get)
        return mar
        
def count(s, n):
    if n in s:
        s[n] += 1
    else:
        s[n] = 1
        
    return s
