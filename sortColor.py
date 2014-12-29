# two pass is like cheating and has little practical meaning;
# quickSort exceeds the time limit.

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        twoPass(A)
        #quickSort(A)
        
        
def quickSort(A):
    sortHelper(A,0,len(A)-1)
    
def sortHelper(A,left,right):
    if left<right:
        midPoint = split(A,left,right)
        
        sortHelper(A,0,midPoint-1)
        sortHelper(A,midPoint+1,right)
        
def split(A,left,right):
    pivot = A[left]
    
    done = False
    
    lm = left
    rm = right
    while not done:
        while lm<=rm and A[lm]<pivot:
            lm+=1
        while lm<=rm and A[rm]>pivot:
            rm-=1
            
        if lm>rm:
            done = True
        elif A[lm]>A[rm]:
            tmp = A[lm]
            A[lm] = B[rm]
            B[rm] = tmp
    tmp = A[rm]
    A[rm] = pivot
    A[first] = tmp
    
    return rm
    
def twoPass(A):
    count = [0]*3
    for i in A:
        for j in range(3):
            if i == j:
                count[j] +=1
                
    #for i in range(len(A)):
    i = 0
    for j in range(3):
        for z in range(count[j]):
            A[i] = j
            i += 1
                
    
    
        
        
        
        
        
        
        
