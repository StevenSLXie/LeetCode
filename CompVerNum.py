class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        ver1 = split(version1)
        ver2 = split(version2)
        
        minL = min(len(ver1),len(ver2))
        
        for i in range(minL):
            tmp = comp(ver1[i],ver2[i])
            if tmp == 0:
                pass
            else:
                return tmp
                
        if len(ver1) < len(ver2) and checkAllZero(ver2,len(ver2)-minL):
            return -1
        elif len(ver1)>len(ver2) and checkAllZero(ver1,len(ver1)-minL):
            return 1

        return 0
        
def checkAllZero(v,res):        
    # this is to check the special case like: 12.0.0 with 12.0
    # if the lengths are different, check whether all the res are 0
     
    if v[-res:].count(0) == res:
        return False
    else:
        return True

def comp(v1,v2):
    if v1<v2:
        return -1
    elif v1>v2:
        return 1
    else:
        return 0

def split(s):
    ver = []
    t = ''
    if s == '':
        return [0]
    for i in range(len(s)):
        if s[i] != '.':
            t += s[i]
        else:
            ver.append(int(t))
            t = ''
    ver.append(int(t))
            
    return ver
    
