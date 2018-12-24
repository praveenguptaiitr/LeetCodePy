# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printNone(self, head):
        while(head is not None):
            print(head.val)
            head=head.next

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            return head

        if m==n:
            return head

        if head.next.next is None and m==1 and n==2:
            head.next.next = head
            t = head.next
            head.next = None
            return t

        i = 1
        curr = head
        prev = None
        #next = curr.next
        while(i<m):
            i+=1
            prev = curr
            curr = curr.next

        p1 = head if prev is None else prev
        #inc by 1
        prev = curr
        curr = curr.next
        next = curr.next


        while(i<n and curr and curr.next):
            curr.next=prev
            prev=curr
            curr=next
            next=next.next
            i+=1

        if curr.next is None:
            #if m==1 and i == n:

            if m==1 and i != n:
                curr.next = prev
                #p1.next = curr
                head.next = None
                head = curr

                #p1.next = prev
                print("-------------------")
                self.printNone(head)
                print("-------------------")
                return head


            elif i < n :
                curr.next = prev
                p1.next.next=None
                p1.next = curr
                #prev.next = None
                #p1.next = prev
                print("-------------------")
                self.printNone(head)
                print("-------------------")
                return head



        if m != 1:
            p1.next.next = curr
            p1.next = prev
            print("-------------------")
            self.printNone(head)
            print("-------------------")
            return head

        else:
            head.next = curr
            head = prev
            print("+++++++++++")
            self.printNone(head)
            print("+++++++++++")
            return head


if __name__=="__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    s.reverseBetween(l,2,4)
