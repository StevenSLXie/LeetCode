
def searchHelper(A,target,left,right):
    # 1 3 5 6:  5
    # 1 3 5 6:  2
    if right==left:
        if A[left] < target:
            return left+1
        return left
        
    mid = (left+right)//2
    # print mid
    if target == A[mid]:
        return mid
    elif target < A[mid]:
        return searchHelper(A,target,left,mid)
    else:
        return searchHelper(A,target,mid+1,right)
        
        
def searchInsert(A,target):
    left = 0
    right = len(A)-1
    
    while left != right:
        mid = (left+right)//2
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            right = mid
        else:
            left = mid+1
            
    if target>A[left]:
        return left+1
    return left
