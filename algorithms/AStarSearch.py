from heapq import heappush, heappop
import numpy as np


# Euclidean distance
def heuristic(node1, node2):
    return np.sqrt(((node1.position[0] - node2.position[0]) ** 2) +
                   ((node1.position[1] - node2.position[1]) ** 2))


class Node:

    def __init__(self, name, position, parent=None):
        self.name = name
        self.position = position
        self.parent = parent
        self.neighbors = []
        self.g = 0
        self.h = 0
        self.f = 0

    def add_neighbor(self, v):
        self.neighbors.append(v)

    # we compare the nodes based on the f(x) values
    # f = g + h
    def __lt__(self, other_node):
        return self.f < other_node.f

    def __repr__(self):
        return self.name


class Edge:

    def __init__(self, target, weight):
        self.target = target
        self.weight = weight


class SearchAlgorithm:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.explored = set()
        self.heap = [source]

    def run(self):
        # we keep iterating while the heap is not empty
        while self.heap:
            # we always get the node with the lowest f value possible
            current = heappop(self.heap)
            # we add the node to the visited set
            self.explored.add(current)
            # if we reach the destination - this is the end of the algorithm
            if current == self.destination:
                break

            # consider all the neighbors (adjacent nodes)
            for edge in current.neighbors:
                child = edge.target
                temp_g = current.g + edge.weight
                temp_f = temp_g + heuristic(current, self.destination)

                # if we have considered the child and the f(x) is higher
                if child in self.explored and temp_f >= child.f:
                    continue

                # else if we have not visited OR the f(x) score is lower
                if child not in self.heap or temp_f < child.f:
                    child.parent = current
                    child.g = temp_g
                    child.f = temp_f

                    # we should update the heap
                    if child in self.heap:
                        self.heap.remove(child)

                    heappush(self.heap, child)

    def show_solution(self):
        solution = []
        node = self.destination

        while node:
            solution.append(node)
            node = node.parent

        print(solution[::-1])


if __name__ == '__main__':
    n1 = Node("A", (0, 0))
    n2 = Node("B", (10, 20))
    n3 = Node("C", (20, 40))
    n4 = Node("D", (30, 10))
    n5 = Node("E", (40, 30))
    n6 = Node("F", (50, 10))
    n7 = Node("G", (50, 40))

    n1.add_neighbor(Edge(n2, 10))
    n1.add_neighbor(Edge(n4, 50))

    n2.add_neighbor(Edge(n3, 10))
    n2.add_neighbor(Edge(n4, 20))

    n3.add_neighbor(Edge(n5, 10))
    n3.add_neighbor(Edge(n7, 30))

    n4.add_neighbor(Edge(n6, 80))

    n5.add_neighbor(Edge(n6, 50))
    n5.add_neighbor(Edge(n7, 10))

    n7.add_neighbor(Edge(n6, 10))

    algorithm = SearchAlgorithm(n1, n5)
    algorithm.run()
    algorithm.show_solution()
