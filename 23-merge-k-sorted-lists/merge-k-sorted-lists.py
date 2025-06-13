class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        while True:
            min_index = -1
            min_val = float('inf')

            # Step 1: Find the list with the smallest head
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i

            # Step 2: If all lists are exhausted
            if min_index == -1:
                break

            # Step 3: Append smallest node and move its pointer
            current.next = lists[min_index]
            current = current.next
            lists[min_index] = lists[min_index].next

        return dummy.next
