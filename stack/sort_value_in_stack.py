from stack.Stack import MyStack


def sortStack(stack:MyStack):
    tempStack = MyStack()

    while stack.is_empty() is False:
        value = stack.pop()
        if tempStack.top() is not None and value >= int(tempStack.top()):
            tempStack.push(value)
        else:
            while tempStack.is_empty() is False:
                stack.push(tempStack.pop())
            tempStack.push(value)

    while tempStack.is_empty() is False:
        stack.push(tempStack.pop())

    return stack


def recursive_sort(stack:MyStack):
    if stack.is_empty() is False:
        value = stack.pop()
        recursive_sort(stack)
        insert(stack,value)


def insert(stack:MyStack, value):
    if(stack.is_empty() or value < stack.top()):
        stack.push(value)
    else:
        temp=stack.pop()
        insert(stack, value)
        stack.push(temp)





stack = MyStack()

stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

print(stack.stack_list)

recursive_sort(stack)

print(stack.stack_list)

