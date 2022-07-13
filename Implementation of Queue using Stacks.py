#TC : O(1)
#SC : O(n)
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        return self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        last = self.out_stack[-1]
        self.out_stack = self.out_stack[:-1]
        return last

    def peek(self) -> int:
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    
    def empty(self) -> bool:
        if len(self.in_stack) + len(self.out_stack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()