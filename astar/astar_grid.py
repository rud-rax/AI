mat = [[1, 3], [0, 2]]

goal = [[1, 2], [3, 0]]


class Matrix:
    def __init__(self, m, goal):
        self.m = m
        self.goal = goal
        self.rows = len(m)
        self.cols = len(m[0])
        self.closed = []
        self.open = []

    def getEmptyNode(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[0])):
                if self.m[i][j] == 0:
                    return i, j
        return

    def getNeighborsValues(self, n):
        i, j = n[0], n[1]

        neighbors = []
        print("NEIGHBORS = ", end=" ")
        if i - 1 >= 0:
            print(self.m[i - 1][j], end=" ")
            neighbors.append([i - 1, j])
        if i + 1 < len(self.m):
            print(self.m[i + 1][j], end=" ")
            neighbors.append([i + 1, j])
        if j - 1 >= 0:
            print(self.m[i][j - 1], end=" ")
            neighbors.append([i, j - 1])
        if j + 1 < len(self.m[0]):
            print(self.m[i][j + 1])
            neighbors.append([i, j + 1])

        return neighbors

    def getNextMatrix(self):

        ei, ej = self.getEmptyNode()
        neighbors = self.getNeighborsValues([ei, ej])

        # print(f"MIN I AND J = {min_i} {min_j}")

        for i, j in neighbors:
            temp_mat = self.m

            temp_mat[i][j], temp_mat[ei][ej] == temp_mat[ei][ej], temp_mat[i][j]

            hc = 0

            for i in range(len(temp_mat)):
                for j in range(len(temp_mat[0])):
                    if temp_mat[i][j] == goal[i][j] and temp_mat not in self.closed:
                        hc += 1

            self.open.append(hc)

        print(self.open.index(min(self.open)))
        w = self.open.index(min(self.open))
        wi, wj = neighbors[w]
        self.closed.append(self.m)

        self.m[ei][ej], self.m[wi][wj] = self.m[wi][wj], self.m[ei][ej]

    def aStar(self):

        pass


if __name__ == "__main__":
    m1 = Matrix(mat, goal)
    print("EMPTY NODE AT = ", m1.getNeighborsValues(m1.getEmptyNode()))

    print(f"BEFORE = ", m1.m)
    m1.getNextMatrix()
    print(f"AFTER = ", m1.m)
