from stack.Stack import MyStack

def next_greater_element(lst):
    s = MyStack()
    res = [-1] * len(lst)
    for i in range(len(lst)-1,-1,-1):

        while not s.is_empty() and s.top() < lst[i]:
            s.pop()

        if not s.is_empty():
            res[i] = s.top()

        s.push(lst[i])

    return res

print(next_greater_element([4, 6, 1,2,8,1]))


