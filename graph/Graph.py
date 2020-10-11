from linkedlist.LinkedList import LinkedList


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

