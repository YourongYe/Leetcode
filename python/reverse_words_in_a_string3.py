#https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        out = ""
        for w in words:
            out+=w[::-1]+" "
            
        return out[:-1]
