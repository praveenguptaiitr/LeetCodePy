class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        self.isFirst = True

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.isFirst:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.isFirst:
            for i in range(len(self.q1)-1):
                e = self.q1.pop(0)
                self.q2.append(e)
            self.isFirst = False
            e1 = self.q1.pop()
            self.q1 = []
            return e1
        else:
            for i in range(len(self.q2)-1):
                e = self.q2.pop(0)
                self.q1.append(e)
            self.isFirst = True
            e1 = self.q2.pop()
            self.q2 = []
            return e1

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.isFirst:
            return self.q1[len(self.q1)-1]
        else:
            return self.q2[len(self.q2) - 1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1)==0 and len(self.q2)==0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)