from graph.Graph import Graph



def find_mother_vortex_helper(g:Graph, node,visited):
    if visited[node]:
        return True

    visited[node] = True

    head = g.array[node].head_node
    while head is not None:
        adjecant = head.data
        if find_mother_vortex_helper(g,adjecant,visited):
            return True
        head = head.next_element

    if all(visited):
        return True
    else:
        return False



def find_mother_vortex(g:Graph):
    for i in range(g.vertices):
        visited = [False]*g.vertices
        if find_mother_vortex_helper(g,i,visited):
            return i
    return -1

g = Graph(4)
g.add_edge(3,0)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(3,1)
print(find_mother_vortex(g))

g1 = Graph(3)
g1.add_edge(0,1)
g1.add_edge(1,2)
g1.add_edge(2,0)

print(find_mother_vortex(g1))
g2 = Graph(4)
g2.add_edge(0,1)
g2.add_edge(2,3)

print(find_mother_vortex(g2))