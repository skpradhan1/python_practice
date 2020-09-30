class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.my_list = [0]*size
        self.top1 = -1
        self.top2 = size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.my_list[self.top1] = value
        else:
            print('stack full')
            exit(1)

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top1 < self.top2 -1:
            self.top2 -= 1
            self.my_list[self.top2] = value
        else:
            print('stack full')
            exit(1)

    # Return and remove top Value from First Stack
    def pop1(self):
        ele = self.my_list[self.top1]
#       self.my_list.remove(self.my_list[self.top1])
        self.top1 = self.top1 -1
        return ele

    # Return and remove top Value from Second Stack
    def pop2(self):
        ele = self.my_list[self.top2]
#       self.my_list.remove(self.my_list[self.top2])
        self.top2 = self.top2 + 1
        return ele

stack = TwoStacks(10)

stack.push1(10)
stack.push2(30)

print(stack.my_list)

stack.push1(43)
stack.push2(33)

print(stack.my_list)

print(stack.pop1())

print(stack.pop2())

print(stack.my_list)