from graph.Graph import Graph


def remove_edge(g:Graph, source, dest):
    head = g.array[source].head_node
    prev = None
    if head.data is dest:
        g.array[source].head_node = head.next_element
        head.next_element = None
    else:
        while head is not None:
            adjecant = head.data
            if adjecant is dest:
                prev.next_element = head.next_element
                head.next_element = None
                return g
            else:
                prev = head
                head = head.next_element



    return g

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 0)

g.print_graph()

remove_edge(g, 0,1)

g.print_graph()


