# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        to_return_head = ListNode(None,None)

        curr1 = list1
        curr2 = list2

        curr = to_return_head

        while (curr1 is not None) or (curr2 is not None):
            if curr1 and curr2:
                val_to_append = min(curr1.val,curr2.val)

                if val_to_append == curr1.val:
                    curr1 = curr1.next
                else:
                    curr2 = curr2.next

                temp = ListNode(val_to_append,None)
                curr.next = temp
                curr = temp
            else:
                curr.next = curr1 if curr1 else curr2
                break

        return to_return_head.next