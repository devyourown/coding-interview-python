class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value):
        if not self.min or self.min[-1] >= value:
            self.min.append(value)
        self.stack.append(value)

    def min(self):
        if not self.min:
            raise Exception('Empty Stack')
        return self.min[-1]

    def pop(self):
        if not self.min:
            raise Exception('Empty Stack')
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        return self.stack.pop()