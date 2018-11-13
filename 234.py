class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""

		if head is None:
			return  True
		if head.next is None:
			return True
		if head.next.next is None and head.val == head.next.val:
			return True
		if head.next.next is None and head.val != head.next.val:
			return False

		f = head
		s = head
		ps = head
		while f is not None and f.next is not None:
			ps = s
			s=s.next
			f= f.next.next
		if f is None:
			mid = ps
		else:
			mid = s

		p = None
		c = mid.next
		n = mid.next.next

		while n is not None:
			c.next = p
			p = c
			c = n
			n = n.next

		c.next = p
		mid.next = c

		a = head
		b = mid.next
		while b is not None:
			if a.val != b.val:
				return False
			a=a.next
			b=b.next

		return True

if __name__ == "__main__":
	h = ListNode(1)
	h.next = ListNode(1)
	h.next.next = ListNode(2)
	h.next.next.next = ListNode(1)
	s = Solution()
	print(s.isPalindrome(h))

