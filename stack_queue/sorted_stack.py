class SortedStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if self.stack and self.stack[-1] < value:
            temp = self.stack.pop()
            self.stack.append(value)
            self.stack.append(temp)
        else:
            self.stack.append(value)

    def sort(self):
        if not self.stack:
            return
        temp = []
        max_one = 0
        while self.stack:
            if min_one < self.stack[-1]:
                temp.append(self.stack.pop())
            else:
                min_one = self.stack[-1]
                self.stack.pop()
        temp.append(min_one)


    def pop(self):
        if not self.stack:
            raise Exception('Empty stack')
        popped = self.stack.pop()
        sort()
        return popped