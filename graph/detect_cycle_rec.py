from graph.Graph import Graph


def detect_cycle(g:Graph):
    visited = [False] * g.vertices
    rec_node_stack = [False]*g.vertices

    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True

    return False

def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if (rec_node_stack[node]):
        return True

    # It has been visited before this recursion
    if (visited[node]):
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True

    head_node = g.array[node].head_node
    while(head_node is not None):
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if (detect_cycle_rec(g, adjacent, visited, rec_node_stack)):
            return True
        head_node = head_node.next_element

    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False


g1 = Graph(2)
g1.add_edge(0, 1)
g1.add_edge(1, 2)

print(detect_cycle(g1))