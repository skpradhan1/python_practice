from graph.Graph import Graph

def find_min_helper(g:Graph, node,dest):
    sum = 1
    head = g.array[node].head_node
    while head is not None:
        sum +=1
        if head.data is dest:
            return sum
        head = head.next_element
    return float("inf")


def find_min(g:Graph, source, dest):
    head = g.array[source].head_node
    min_step = float("inf")
    while head is not None:
        adjecant = head.data
        num_steps = find_min_helper(g,adjecant,dest)
        min_step = min(min_step,num_steps)
        head = head.next_element

    return min_step

g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)

print(find_min(g,1,5))