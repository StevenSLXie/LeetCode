class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return square(x,0.0,float(x*2))
        

def square(x,left,right):

    if abs(left-right) < 0.00001:
        print (left+right)/2.0
        return int((left+right)/2.0)
    
    
    mid = float((left+right)/2.0)
    
    if mid*mid - x <= 0:
        return square(x,mid,right)
    else:
        return square(x,left,mid)
        
