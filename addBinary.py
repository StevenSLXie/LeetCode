class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a_dec = binToDec(a)
        b_dec = binToDec(b)
        
        sum = a_dec + b_dec
        return decToBin(sum)

def binToDec(s):
    num = [int(x) for x in list(s)]
    
    sum = 0
    for i in range(len(num)):
        sum += num[i]*2**(len(num)-1-i)
    return sum
    
def decToBin(num):
    #import copy
    #d = copy.copy(num)
    d = num
    sum = 0 
    i = 0
    while d:
        # 7:111  7%2 1 3%2 1 1%2 1
        # 6:110  6%2 0 3%2 1 1%2 1
        # 14:1110 14%2 0 7%2 1 3%2 1 1%2 1
        dig = d % 2
        d = d/2
        sum += 10**i*dig
        i += 1
    return str(sum)
        
        
        
        

        
