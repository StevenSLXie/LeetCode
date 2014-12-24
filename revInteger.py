class Solution:
    # @return an integer
    def reverse(self, x):
        digits = []
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        num = x
        while num > 0:
            num, digits = decompose(num, digits)
        rev = compose(digits)
        rev = rev*sign
        
        if rev > 2**31-1:
            return 0
        elif rev < -2**31:
            return 0
        return rev
        
def decompose(num, digits):
    res = num % 10
    num = num/10
    digits.append(res)
    return num, digits
    
def compose(digits):
    sum = 0
    i = 0
    while digits:
        d = digits.pop()
        expo = 10**i
        sum += d*expo
        i += 1
        
    return sum
    

        

            
            
            
