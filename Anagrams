class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        table = {}
        
        if strs == ['']:
            return []

        for i in range(len(strs)):
            if sortAndToStr(strs[i]) not in table:
                table[sortAndToStr(strs[i])] = [i]
            else:
                table[sortAndToStr(strs[i])].append(i)
        out = []
        for t in table:
            if len(table[t]) > 1:
                for i in table[t]:
                    out.append(strs[i])
                
        return out

def sortAndToStr(l):
    l = sorted(l)
    s = ''
    for i in l:
        s += i
    return s
    
