'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        
        if(head is None):
            return None
        
        
        root = head
        node = None
        
        
        def reverseLinkedList(curr):
            
            start = curr
            prev = None
            
            while curr:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev,start
        
        
        len_linkedList = 0  
        while head:
            len_linkedList +=1
            head = head.next
        
        
        head = root
        len_linkedList -= len_linkedList % k
        
        
        m = 0
        n = m + k - 1
        
        while n < len_linkedList:
            
            
            curr = head
            prev = node
        
            front = prev
            mhead = curr


            while m < n:

                curr = curr.next
                m+=1

            if(curr is None):
                break
                
            lasthead = curr.next
            curr.next = None

            if(front):
                front.next,start = reverseLinkedList(mhead)

            else:
                root,start = reverseLinkedList(mhead)

            start.next = lasthead
            
            head = lasthead
            node = start
            
            m+=1
            n = m + k - 1
            
        return root

