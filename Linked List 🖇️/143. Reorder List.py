# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #LeftPortion 
        
        leftListHead = slow.next
        slow.next = None

        #Reversing leftPortion
        prev = None 
        while leftListHead:
            temp = leftListHead.next
            leftListHead.next = prev
            prev = leftListHead
            leftListHead = temp
        leftListHead = prev

        #Merge them
        first, second = head, leftListHead
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
        

    