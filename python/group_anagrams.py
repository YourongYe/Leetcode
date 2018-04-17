#https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            #sorted_s = ''.join(sorted(s))
            hash.setdefault(sorted_s,[]).append(s)
            
        result = []
        for h in hash:
            result.append(hash[h])
            
        return result
