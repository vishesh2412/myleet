class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow=head
        fast=head

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                temp = head
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow

        if not fast.next:
                return None