# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next

        slow.next=None #Ending of fist LL
        prev=None
        while mid != None:
            temp=mid.next
            mid.next=prev
            prev=mid
            mid=temp
        
        first=head
        second=prev

        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            second=temp2
            first=temp1

