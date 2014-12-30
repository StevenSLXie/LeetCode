
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
