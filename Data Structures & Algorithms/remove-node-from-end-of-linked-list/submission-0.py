# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def traverseListLen(root):
            lenghtOfList = 0
            if not root:
                return 0
            curr = root

            while curr:
                lenghtOfList +=1
                curr=curr.next
            return lenghtOfList
        def deleteNode(head,pos):
            if pos == 0:
                return head.next
            curr = head
            while curr and pos>1:
                pos-=1
                curr = curr.next
            if curr and curr.next: 
                curr.next = curr.next.next
            return head


        lenOfLL = traverseListLen(head)
        k = lenOfLL - n

        return deleteNode(head,k)

        