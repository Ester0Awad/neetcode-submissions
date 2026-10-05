# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer_1 = list1
        pointer_2 = list2

        # Dummy node concept, acts as a placeholder
        starting_node = ListNode (0)
        tail_node = starting_node

        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                tail_node.next = pointer_1
                pointer_1 = pointer_1.next

            else:  
                tail_node.next = pointer_2
                pointer_2 = pointer_2.next  


            tail_node = tail_node.next


        # Handling leftover
        if pointer_1 is not None:
            tail_node.next = pointer_1

        elif pointer_2 is not None:
            tail_node.next = pointer_2

        return starting_node.next    
