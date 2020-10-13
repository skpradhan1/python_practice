from graph.Graph import Graph
from stack.MyQueue import MyQueue

# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}

def bfs_helper(g: Graph, source):
    result = ""
    q = MyQueue()
    q.enqueue(source)
    visited = [False] * g.vertices
    visited[source] = True
    while q.is_empty() is False:
        current_node = q.dequeue()
        result += str(current_node)
        temp = g.array[current_node].get_head()
        while temp is not None:
            if visited[temp.data] is False:
                q.enqueue(temp.data)
                visited[temp.data] = True
            elif visited[temp.data] is True and source != current_node:
                return True
            temp = temp.next_element
    return False


def detect_cycle(g: Graph):
    num_vertices = g.vertices

    if num_vertices is 0:
        return True

    for i in range(num_vertices):
        outcome = bfs_helper(g, i)
        if outcome is True:
            print('cycle exists')
            return outcome
    return outcome

g = Graph(4)

g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(3,2)
g.add_edge(2,0)

print(detect_cycle(g))