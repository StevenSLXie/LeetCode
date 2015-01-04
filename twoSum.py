class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if num[i] not in d:
                d[num[i]] = i+1
            elif 2*num[i] == target:
                return d[num[i]], i+1
        
        for n in d:
            if target-n in d:
                return min(d[n], d[target-n]), max(d[n], d[target-n])
