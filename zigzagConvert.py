class Solution:
    # @return a string
    def convert(self,s, nRows):
        # 'This is to ask you to return a string in 4 rows'
        # T    a    t    r
        # h  o s  u o  u n  t
        # i t  k o  r t  a s
        # s    y    e    s 
        
        # t    k   8
        # h   sy   6 2    
        # i  a o   4 4
        # s t  u   2 6
        # t    t   8
        
        # 0 6 12 18
        # 1 5 7 11 13 17 19
        # 2 4 8 10 14 16 20
        # 3 9 15
        
        sum = 2*nRows - 2
        
        offsets = []
        for i in range(nRows):
            offset = []
            for j in range(len(s)/nRows+1):
                if i != nRows-1 and i+(sum-2*i)*j < len(s):
                    offset.append(s[i+(sum-2*i)*j])
                if i != 0 and i+(2*i)*j < len(s):
                    offset.append(s[i+(2*i)*j])
            if 0 in offset:
                offset.remove(0)
            offsets.append(offset)
            
        
        out = ''
        for r in range(nRows): 
            for off in offsets[r]:
                out += off
        return out
        
        

                
