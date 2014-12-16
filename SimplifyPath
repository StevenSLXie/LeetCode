class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        
        last = 0
        
        s = []
        for i in range(1,len(path)):
            if path[i] == '/':
                if i == last + 1:
                    #'//' redandunt slashes
                    pass
                elif path[last+1:i] == '.':
                    pass
                elif path[last+1:i] == '..':
                    if len(s) != 0:
                        s.pop()
                else:
                    s.append(path[last+1:i])
                last = i
                
        if  last == len(path)-1 or path[last+1:] == '.':
            pass
        elif path[last+1:] == '..':
            if len(s) != 0:
                s.pop()
        else:
            s.append(path[last+1:])
        
        s = '/'+'/'.join(s)    
          
        if s == '/' or s == '//' or s == '///' or s == '/../':
            return '/'
        else:
            return s
