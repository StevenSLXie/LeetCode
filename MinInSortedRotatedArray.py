class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        #  7 8 9 10 0 1 2 3 4 5 6

        return helper(num,0,len(num)-1)
        
def helper(num,left,right):
    if left == right:
        return num[right]
        
    mid = (right+left)//2
    
    if num[mid]>num[right]:
        return helper(num,mid+1,right)
    else:
        return helper(num,left,mid)
        

        
