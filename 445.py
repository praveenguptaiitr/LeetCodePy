# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.carry = 0

    def addSingle(self, head, tmp, l3):
        if head is tmp:
            return l3


        l = ListNode(float("-inf"))
        l.next = self.addSingle(head.next,tmp,l3)
        c = head.val + self.carry
        if c > 9:
            c = c%10
            self.carry = 1
        else:
            self.carry=0

        l.val = c
        return l

    def print1(self, node, c = "-"):
        print(c * 10)
        while(node is not None):
            print(node.val)
            node=node.next

    def add(self, l1,l2):
        if l1 is None:
            return None

        l3 = ListNode(float("-inf"))
        l3.next = self.add(l1.next,l2.next)
        c = l1.val+l2.val + self.carry
        if c > 9:
            c = c%10
            self.carry = 1
        else:
            self.carry=0

        l3.val = c
        return l3

    def len(self, head):
        tmp = head
        i=0
        while(tmp is not None):
            i+=1
            tmp=tmp.next

        return i

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        len1 = self.len(l1)
        len2 = self.len(l2)
        tmp1 = l1
        tmp2 = l2

        if len1 > len2:
            k = len1-len2
            for i in range(k):
                tmp1 = tmp1.next
        else:
            k = len2-len1
            for i in range(k):
                tmp2 = tmp2.next


        l3 = self.add(tmp1,tmp2)
        #self.print(l3)
        l4 = None
        if len1 > len2:
            l4 = self.addSingle(l1,tmp1,l3)
        elif len2>len1:
            l4 = self.addSingle(l2,tmp2,l3)

        if len1==len2:
            l4 = l3
        k = ListNode(1)
        if self.carry == 1:
            k.next = l4
            return k
        else:
            return l4

if __name__ =="__main__":
    s = Solution()
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = s.addTwoNumbers(l1,l2)
    s.print1(l3,"+")