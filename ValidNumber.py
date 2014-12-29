class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        '''
        The process of determining validity.
        1. delete the first-n and last-n spaces
        2. delect the first '+' and '-'
        3. for the rest, if not in OK_set, False;
        4. if multiple dots, False;
        5. if multiple e-s, False;
        6. if '+' '-' not after 'e', False;
        7. any dot after 'e', False;
        8. next to dot there must be at least number, otherwise False;
        9. if there is no number at all, False;
        10. set all the other as valid.
        '''
        
        
        if s == '':
            # empty string
            return False
            
        num = list(s)
        # delect all prefix spaces
        while num[0] == ' ':
            num.pop(0)
            if num == []:
                return False
                
        # delect all spaces backwards    
        while num[-1] == ' ':
            num.pop()
            if num == []:
                return False

        # delect the first '+' or '-'
        if num[0] == '+' or num[0] == '-':
            num.pop(0)
            if num == []:
                return False
            
        e_count = 0
        dot_count = 0
        num_count = 0
        
        OK_set = ['0','1','2','3','4','5','6','7','8','9','e','-','.','+']
        num_set = ['0','1','2','3','4','5','6','7','8','9']
        
        
        for i in range(len(num)):
            
            if num[i] not in OK_set:
                return False
                
            if num[i] == 'e':
                if i == len(num)-1 or i == 0:
                    return False
                e_count += 1
                if e_count > 1:
                    return False
            
            elif num[i] == '.':
                #if i != len(num)-1 and num[i+1] == 'e':
                #    return False
                if e_count > 0:
                    return False
                
                if len(num) ==1:
                    return False
                if i == 0:
                    if num[i+1] not in num_set:
                        return False
                elif i == len(num)-1:
                    if num[i-1] not in num_set:
                        return False
                elif num[i-1] not in num_set and num[i+1] not in num_set:
                    return False
                
                #if i != 0 and num[i-1] == 'e':
                #    return False
                    
                dot_count += 1
                if dot_count > 1:
                    return False
            
                    
            elif num[i] == '-' or num[i] == '+':
                # '+' '-' can appear only when after 'e'
                if num[i-1] == 'e' and i != len(num)-1:
                    pass
                else:
                    return False
                    
            else:
                num_count += 1
                
        if num_count:           
            return True
        else:
            return False 
            
            
        # delete all the spaces on both sides
        
        # detect any characters other then 0-9, 'e' and dot, return False
        
        # detect 2 dots or 2 'e', return False
        
        # '-' must be right in the beginning, or right after 'e'
        
        # 'e' must not be at the beginning 46.e3
        
#def popEmpty(num,dir,)
        

        
