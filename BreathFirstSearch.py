from graph import Graph


def DFS(g, start, stop):

    queue = [start]
    visited = []

    while len(queue) > 0:
        node = queue[0]
        queue.pop(0)

        if node == stop:
            visited.append(node)
            print("PATH = ", visited)
            return

        visited.append(node)

        for no in g.graph[node]:
            if no not in visited and no not in queue:
                queue.append(no)

    print("NO PATH FOUND")


if __name__ == "__main__":

    g = Graph()
    g.addNode("A")
    g.addNode("B")
    g.addNode("C")
    g.addNode("D")
    g.addNode("E")
    g.addNode("F")
    g.addNode("G")

    g.addEdge("A", "C")
    g.addEdge("C", "B")
    g.addEdge("A", "F")
    g.addEdge("A", "B")
    g.addEdge("C", "D")
    g.addEdge("C", "E")
    g.addEdge("D", "G")
    g.addEdge("E", "F")
    g.addEdge("F", "G")

    g.getAdjNodes("A")
    g.displayAdjList()

    DFS(g, "A", "G")
