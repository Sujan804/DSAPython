# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         
        slow, fast = head, head
        currNo = 0

        while True:
            fast = fast.next
            if fast == None:
                break
            currNo += 1
            if currNo > n:
                slow = slow.next
        if currNo < n:
            return slow.next
        slow.next = slow.next.next

        return head
    

    
                
