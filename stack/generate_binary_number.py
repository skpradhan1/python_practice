from stack.MyQueue import MyQueue


def find_bin(n):
    q = MyQueue()
    q.enqueue('1')
    lst = []
    while len(lst) < n:
        element = q.dequeue()
        lst.append(element)
        new_1 = element + '0'
        new_2 = element + '1'
        q.enqueue(new_1)
        q.enqueue(new_2)
    return lst


print(find_bin(4))

