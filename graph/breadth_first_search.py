from graph.Graph import Graph
from stack.MyQueue import MyQueue
from linkedlist.Node import Node


def bfs_traversal_helper(g:Graph, source, visited):
    result = ""
    q = MyQueue()
    q.enqueue(source)
    visited[source] = True
    while q.is_empty() is False:
        current_node = q.dequeue()
        result += str(current_node)
        temp: Node = g.array[current_node].head_node
        while temp is not None:
            if visited[temp.data] is False:
                q.enqueue(temp.data)
                visited[temp.data] = True
                temp = temp.next_element
    return result, visited


def bfs_traversal(g:Graph, source):
    result = ""
    num_vertices = g.vertices
    if num_vertices is 0:
        return result

    visited = [False]*num_vertices

    result, visited = bfs_traversal_helper(g,source,visited)

    for i in range(num_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new

    return result


g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)

print(bfs_traversal(g,0))

