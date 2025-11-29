class Solution:
    
    def get_valid_char_idx(self,s,p):
        skip = 0 
        while p>=0:
            if s[p] == "#": 
                skip+=1 # need to move back 1 pointer 
                p-=1 # moving back the backspace
            elif skip >0: # if already seen backspace 
                p-=1 # moving the pointer back as skip already seen
                skip-=1 # as 1 backspace work done 
            else :
                return p # return the current location if no skip or return the next valid after skipping
        return -1 # no valid char left

    def backspaceCompare(self, str1: str, str2: str) -> bool:
        i1 = len(str1) - 1
        i2 = len(str2) - 1
        while True:
            i1 = self.get_valid_char_idx(str1,i1)
            i2 = self.get_valid_char_idx(str2,i2)
            if i1<0 and i2<0:
                return True # both char have passed all the conditions
            if str1[i1] != str2[i2]:
                return False # as the valid idx char are not equal
            if i1<0 or i2<0 : 
                return False # as either one str is smaller then other finally
            i1-=1 # moving to the next char
            i2-=1 # moving to the next char and checking from there

        