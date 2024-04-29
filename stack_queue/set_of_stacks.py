class SetOfStacks:
    def __init__(self, size):
        self.size = size
        self.stacks = [[]]
        self.cur_stacks = 0

    def is_cur_full(self):
        if len(self.stacks[self.cur_stacks]) == size:
            return True
        return False

    def is_empty(self):
        if not self.stacks[self.cur_stacks]:
            return True
        return False

    def push(self, value):
        if self.is_cur_full():
            self.stacks.append([])
            self.cur_stacks += 1
        self.stacks[self.cur_stacks].append(value)

    def pop(self):
        if self.is_empty():
            if self.cur_stacks == 0:
                raise Exception('Empty Stacks')
            self.cur_stacks -= 1
        return self.stacks[self.cur_stacks].pop()

    def pop_at(self, index):
        if not self.stacks[index]:
            raise Exception('Empty Stacks')
        return self.stacks[index].pop()