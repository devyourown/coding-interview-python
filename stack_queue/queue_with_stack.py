class MyQueue:
    def __init__(self):
        self.pop_stack = []
        self.push_stack = []

    def append(self, value):
        self.push_stack.append(value)

    def remove(self):
        if self.pop_stack:
            return self.pop_stack.pop()
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        if not self.pop_stack:
            raise Exception('Empty Queue')
        return self.pop_stack.pop()