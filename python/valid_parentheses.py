#https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        
        stack = []
        
        for i in range(len(s)):
            c = s[i]
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
                continue
            
            if not stack:
                return False
            
            out = stack.pop()
            if (c==')' and out=='(' or \
                c==']' and out=='[' or \
                c=='}' and out=='{'):
                continue
            else:
                return False

        return not stack
                
