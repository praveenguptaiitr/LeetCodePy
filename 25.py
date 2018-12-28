# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printl(self, head):
        print("------------")
        tmp = head
        while(tmp is not None):
            print(tmp.val)
            tmp=tmp.next
        print("=============")
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tmp = head
        l = 0
        while tmp is not None:
            l +=1
            tmp=tmp.next

        if head is None or head.next is None or k == 0 or k == 1:
            return head

        if l == 2 and k == 2:
            head.next.next = head
            t = head.next
            head.next = None
            return t

        pHead = None
        prev = None
        mid = head
        nxt = head.next

        iter = 1
        total = l//k
        while iter <= (l//k):
            i=0
            while (i < k and mid is not None and nxt is not None):
                mid.next = prev
                prev = mid
                mid = nxt
                nxt = nxt.next
                i+=1

            if pHead is None:
                if iter * k != l:
                    pHead = head
                    head = prev
                    pHead.next = mid
                else:
                    mid.next = prev
                    head = mid
                    return head
            else:
                if iter * k != l:
                    t = pHead.next
                    pHead.next = prev
                    t.next = mid
                    pHead=t
                    prev = pHead
                else:
                    pHead.next.next = None
                    pHead.next = mid
                    mid.next = prev
            iter+=1

        #pHead.next = prev

        return head

if __name__ =="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    # l.next.next.next.next = ListNode(5)
    # l.next.next.next.next.next = ListNode(6)
    # l.next.next.next.next.next.next = ListNode(7)
    # l.next.next.next.next.next.next.next = ListNode(8)
    k = s.reverseKGroup(l,4)
    s.printl(k)
