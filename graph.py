from unicodedata import name


class Graph:
    def __init__(self, graph={}):
        self.graph = graph
        self.hc_list = {}
        self.nodes = 0

    def addNode(self, name, hc=1):
        # node = Node(name, hc)
        self.graph[name] = []
        self.hc_list[name] = hc

    def addEdge(self, n1, n2, cost):

        self.graph[n1].append([n2, cost])
        self.graph[n2].append([n1, cost])

    def displayAdjList(self):
        for node in self.graph:
            print(f"{node}", end=" -> ")
            for info, cost in self.graph[node]:
                print(f"[ {info}:{cost}:{self.hc_list[info]} ]", end=" -> ")

            print("#\n|")
        print("#")

    def displayHCList(self):
        print("-" * 5 + "+" + "-" * 5)
        for node in self.hc_list:
            print(f"  {node}  |  {self.hc_list[node]}  ")
        print("-" * 5 + "+" + "-" * 5)

    def getAdjNodes(self, node):
        return self.graph[node]

    def getHeuristicCost(self, node):
        return self.hc_list[node]


if __name__ == "__main__":

    g = Graph()

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

    g.displayAdjList()
    g.displayHCList()

    # print(g.getAdjNodes("C"))

    # print(g.getHeuristicCost("C"))
