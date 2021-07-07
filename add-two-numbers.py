"""
I knew absolutely nothing about Linked List implementations in Python going in to this question.
I'm satisfied I could answer this in an interview, without having used google to solve.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    @staticmethod
    def gen_num_from_linked_list(linkedlist):
        llist = []
        next = linkedlist.next
        llist.append(linkedlist.val)
        while next:
            llist.append(next.val)
            next = next.next
            if not next:
                break
        return int(''.join([str(l) for l in llist[::-1]]))
    
    @staticmethod
    def gen_linked_list_from_num(num):
        for l,n in enumerate(num):
            if l == 0:
                result = ListNode(n, None)
                continue
            result = ListNode(n, result)
        return result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = str(self.gen_num_from_linked_list(l1) + self.gen_num_from_linked_list(l2))
        return self.gen_linked_list_from_num(int(r) for r in result)
      
"""
Runtime: 72 ms, faster than 21.81% of Python online submissions for Add Two Numbers.
Memory Usage: 13.7 MB, less than 15.33% of Python online submissions for Add Two Numbers.
"""
