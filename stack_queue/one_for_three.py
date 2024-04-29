class ThreeStacks:
    def __init__(self, size):
        self.stack = [None] * (size * 3)
        self.first = -1
        self.second = size - 1
        self.third = size * 2 - 1
        this.size = size

    def is_full(self, which):
        if not self.stack[which*size]:
            return True
        return False

    def is_empty(self, which):
        if not self.stack[which*size]:
            return False
        return True

    def push(self, value, which):
        if self.is_full(which):
            raise Exception('Full Stack')
        if which == 1:
            self.first += 1
            self.stack[self.first] = value
        elif which == 2:
            self.second += 1
            self.stack[self.second] = value
        else:
            self.third += 1
            self.stack[self.third] = value

    def pop(self, which):
        if self.is_empty(which):
            raise Exception('Empty Stack.')
        if which == 1:
            temp = self.stack[self.first]
            self.stack[self.first] = None
            self.first -= 1
        elif which == 2:
            temp = self.stack[self.second]
            self.stack[self.second] = None
            self.second -= 1
        else:
            temp = self.stack[self.third]
            self.stack[self.thrid] = None
            self.third -= 1
        return temp
