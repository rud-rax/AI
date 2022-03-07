from unicodedata import name


class Graph:
    def __init__(self, graph={}):
        self.graph = graph

        self.nodes = 0

    def addNode(self, name):
        # node = Node(name, hc)
        self.graph[name] = []

        self.nodes += 1

    def addEdge(self, n1, n2):

        self.graph[n1].append([n2])
        self.graph[n2].append([n1])

    def getAdjNodes(self, node):
        return self.graph[node]


class WeightedGraph(Graph):
    def __init__(self, graph={}):
        super().__init__()
        self.graph = graph

    def addEdge(self, n1, n2, cost):

        self.graph[n1].append([n2, cost])
        self.graph[n2].append([n1, cost])

    def getDistanceCost(self, node1, node2):

        for no, co in self.graph[node1]:
            if no == node2:
                return co

        return None


class HeuristicGraph(WeightedGraph):
    def __init__(self):
        super().__init__()
        self.hc_list = {}

    def addNode(self, name, hc=1):
        # node = Node(name, hc)
        self.graph[name] = []
        self.hc_list[name] = hc
        self.nodes += 1

    def displayAdjList(self):
        for node in self.graph:
            print(f"{node}", end=" -> ")
            for info, cost in self.graph[node]:
                print(f"[ {info}:{cost}:{self.hc_list[info]} ]", end=" -> ")

            print("#\n|")
        print("#")

    def getHeuristicCost(self, node):
        return self.hc_list[node]

    def prioritiseAdjNodes(self):

        for node in self.graph:
            i = 0
            for no1 in range(len(self.graph[node])):
                for no2 in range(len(self.graph[node]) - 1):
                    if (
                        self.graph[node][no1][1]
                        + self.getHeuristicCost(self.graph[node][no1][0])
                    ) < (
                        self.graph[node][no2][1]
                        + self.getHeuristicCost(self.graph[node][no2][0])
                    ):
                        self.graph[node][no1], self.graph[node][no2] = (
                            self.graph[node][no2],
                            self.graph[node][no1],
                        )

                i += 1

    def displayHCList(self):
        print("-" * 5 + "+" + "-" * 5)
        for node in self.hc_list:
            print(f"  {node}  |  {self.hc_list[node]}  ")
        print("-" * 5 + "+" + "-" * 5)


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

    g.displayAdjList()
    g.displayHCList()

    # print(g.getAdjNodes("C"))

    # print(g.getHeuristicCost("C"))

    print("DISTANCE COST = ", g.getDistanceCost("A", "C"))

    g.prioritiseAdjNodes()
    g.displayAdjList()
