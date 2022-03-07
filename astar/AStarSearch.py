from graph import HeuristicGraph


def AStarSearch(g, start, goal):
    open = [start]
    closed = []
    queue = []
    total_cost = 0

    while len(open) > 0:

        node = open.pop(0)
        open = []
        if node == goal:

            closed.append(node)
            print("PATH  = ", closed)
            return

        for no, _ in g.graph[node]:

            if no not in closed:
                open.append(no)

        closed.append(node)
        # total_cost += g.getDistanceCost(node, open[0]) + g.getHeuristicCost(open[0])


if __name__ == "__main__":

    g = HeuristicGraph()

    # ADDING NODES TO THE GRAPH
    g.addNode("A", 0)
    g.addNode("B", 1)
    g.addNode("C", 3)
    g.addNode("D", 2)
    g.addNode("E", 1)
    g.addNode("F", 2)
    g.addNode("G", 0)

    # ADDING EDGES TO THE GRAPH
    g.addEdge("A", "B", 3)
    g.addEdge("A", "C", 2)
    g.addEdge("B", "D", 4)
    g.addEdge("D", "E", 5)
    g.addEdge("E", "C", 6)
    g.addEdge("F", "C", 7)
    g.addEdge("E", "G", 1)
    g.addEdge("F", "G", 2)

    g.prioritiseAdjNodes()
    g.displayAdjList()
    g.displayHCList()

    AStarSearch(g, "A", "G")

    # print(g.getAdjNodes("C"))

    # print(g.getHeuristicCost("C"))
