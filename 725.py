# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = 0
        curr = root

        while curr is not None:
            l+=1
            curr=curr.next

        ans = []
        if l==0:
            for i in range(k):
                ans.append([])
            return ans

        l1 = l//k
        l2 = l%k
        curr = root
        prev = None
        if l1 ==0:
            for i in range(k):
                if curr is None:
                    ans.append([])
                else:
                    ans.append(curr)
                    prev = curr
                    curr = curr.next
                    prev.next = None
            return ans

        for i in range(k+1):
            if curr is not None:
                ans.append(curr)
            if i < l2:
                for j in range(l1+1):
                    prev = curr
                    curr=curr.next
                prev.next = None
            else:
                for j in range(l1):
                    prev = curr
                    if curr is not None:
                        curr=curr.next
                if prev is not None:
                    prev.next = None

        return ans

if __name__=="__main__":
    s = Solution()
    l = None
    # l = ListNode(1)
    # l.next = ListNode(2)
    # l.next.next = ListNode(3)
    # l.next.next.next = ListNode(4)
    # l.next.next.next.next = ListNode(5)
    # l.next.next.next.next.next = ListNode(6)
    # l.next.next.next.next.next.next = ListNode(7)
    s.splitListToParts(l,3)