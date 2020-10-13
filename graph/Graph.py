from linkedlist.LinkedList import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, target):
        if source < self.vertices and target < self.vertices:
            self.array[source].insert_at_head(target)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while (temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


