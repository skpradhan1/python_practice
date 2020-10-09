from stack.Stack import MyStack


class NewQueue:

    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    def enqueue(self, value):
        self.main_stack.push(value)
        return True

    def dequeue(self):
        if self.temp_stack.is_empty():
            if self.main_stack.is_empty():
                return None
            while self.main_stack.is_empty() is False:
                self.temp_stack.push(self.main_stack.pop())
        temp = self.temp_stack.pop()
        return temp





