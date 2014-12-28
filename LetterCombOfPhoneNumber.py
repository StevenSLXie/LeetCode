class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if digits == '':
            return ['']
        num = strToInt(digits)
        out = []
        for c in combination(num):
            out.append(c)
            
        return out
        
        
def combination(num):
    if len(num) == 0:
        return
        
    elif len(num) == 1:
        for n in intToLetter(num[0]):
            yield n
        
    else:
        for l in intToLetter(num[0]):
            for all in combination(num[1:]):
                yield l + all
    
def strToInt(digits):
    num = []
    for i in list(digits):
        num.append(int(i))
    return num
    
def intToLetter(num):
    if num == 2:
        return ['a','b','c']
    elif num == 3:
        return ['d','e','f']
    elif num == 4:
        return ['g','h','i']
    elif num == 5:
        return ['j','k','l']
    elif num == 6:
        return ['m','n','o']
    elif num == 7:
        return ['p','q','r','s']
    elif num == 8:
        return ['t','u','v']
    elif num == 9:
        return ['w','x','y','z']
            
        
