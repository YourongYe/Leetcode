#https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        new_head = RandomListNode(head.label)
        new_node = new_head
        
        node_dict = {}
        node_dict[head] = new_head
        
        #copy list & save node mapping
        next_node = head
        next_node = next_node.next
        while next_node:
            new_node.next = RandomListNode(next_node.label)
            node_dict[next_node] = new_node.next
            
            new_node = new_node.next
            next_node = next_node.next
        
        #copy randoms
        new_node = new_head
        node = head
        while node:
            if node.random:
                new_node.random = node_dict[node.random]
            new_node = new_node.next
            node = node.next
        
        return new_head
            
