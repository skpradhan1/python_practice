from graph.Graph import Graph
from stack.MyQueue import MyQueue
from linkedlist.Node import Node
from stack.Stack import MyStack


def dfs_traversal_helper(g:Graph, source, visited):
    result = ""
    q = MyStack()
    q.push(source)
    visited[source] = True
    while q.is_empty() is False:
        current_node = q.pop()
        result += str(current_node)
        temp: Node = g.array[current_node].head_node
        while temp is not None:
            if visited[temp.data] is False:
                q.push(temp.data)
                visited[temp.data] = True
                temp = temp.next_element
    return result, visited


def dfs_traversal(g:Graph, source):
    result = ""
    num_vertices = g.vertices
    if num_vertices is 0:
        return result

    visited = [False]*num_vertices

    result, visited = dfs_traversal_helper(g,source,visited)

    for i in range(num_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new

    return result

g = Graph(7)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(2,5)
g.add_edge(3,6)

print(dfs_traversal(g,1))