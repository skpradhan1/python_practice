from stack.MyQueue import MyQueue
from stack.Stack import MyStack


def reverse(queue: MyQueue, k):
    if queue.size() ==0 or queue.size() < k:
        return None
    s = MyStack()
    for i in range(k):
        s.push(queue.dequeue())
    q1 = MyQueue()
    for i in range(k):
        q1.enqueue(s.pop())
    while queue.is_empty() is False:
        q1.enqueue(queue.dequeue())

    return q1

q2 = MyQueue()
for i in range(10):
    q2.enqueue(i)
q3 = reverse(q2, 5)
print(q3.queue_list)