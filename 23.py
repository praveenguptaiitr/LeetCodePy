import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        heap = []
        k = len(lists)
        for i in range(k):
            if lists[i] != None:
                heap.append((lists[i].val, lists[i]))

        heapq.heapify(heap)
        ans = None
        head = None
        while (len(heap) > 0):
            v, l = heapq.heappop(heap)
            t = l.next
            l.next = None
            if head == None:
                head = l
                ans = head

            else:
                ans.next = l
                ans = ans.next

            if t != None:
                heapq.heappush(heap, (t.val, t))

        return head