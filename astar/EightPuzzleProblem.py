class Puzzle8:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def h(self, arr):
        h = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] != self.goal[i][j] and arr[i][j] != 0:
                    h += 1

        return h

    def f(self, arr, g=0):
        return self.h(arr) + (g + 1)

    def findNext(self, ori_arr, g):
        i, j = self.empty(ori_arr)

        arr = [x[:] for x in ori_arr]
        print(arr)

        all_arr = []
        # print("ori arr", ori_arr)

        # TOP
        if (i - 1) >= 0:
            arr[i - 1][j], arr[i][j] = arr[i][j], arr[i - 1][j]
            th = self.h(arr)
            print(f"TOP : {arr} H : {th} G : {g+1}")
            all_arr.append(arr)

        arr = [x[:] for x in ori_arr]

        # DOWN
        if (i + 1) <= 2:
            arr[i + 1][j], arr[i][j] = arr[i][j], arr[i + 1][j]
            th = self.h(arr)

            print(f"DOWN : {arr} H : {th} G : {g+1}")

            all_arr.append(arr)

        arr = [x[:] for x in ori_arr]

        # LEFT
        if (j - 1) >= 0:
            arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
            th = self.h(arr)

            print(f"LEFT : {arr} H : {th} G : {g+1}")
            all_arr.append(arr)

        arr = [x[:] for x in ori_arr]

        # RIGHT
        if (j + 1) <= 2:
            arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1]
            th = self.h(arr)

            print(f"RIGHT : {arr} H : {th} G : {g+1}")
            all_arr.append(arr)

        i = len(all_arr) - 1
        while i > 0:
            j = 0
            while j < i:
                # print(i, j)
                if self.f(all_arr[j]) > self.f(all_arr[j + 1]):

                    all_arr[j], all_arr[j + 1] = all_arr[j + 1], all_arr[j]
                j += 1

            i -= 1

        return all_arr

    def empty(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    print(f"EMPTY AT {i} {j}")
                    return i, j

    def solve(self, start, stop):
        visited = []
        curr = start
        g = 0
        # print(goal)

        while curr != goal:
            print(f"G : {g}")
            print(f"VISITED : {visited}")

            for pa in self.findNext(curr, g):
                if pa not in visited:

                    visited.append(curr)
                    curr = pa
                    break
            g += 1

        else:
            visited.append(curr)

        return visited


if __name__ == "__main__":

    start = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MID_ZERO = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    EDGE_01 = [[1, 0, 3], [4, 2, 5], [6, 7, 8]]

    TEST_01 = [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
    TEST_02 = [[1, 3, 0], [5, 2, 6], [4, 7, 8]]

    p = Puzzle8(start, goal)
    g = 0
    # for a in p.findNext(start, g):
    #     print(a, p.f(a, g))

    # print(p.h(TEST_01))
    print("SOLUTION")

    for state in p.solve(EDGE_01, goal):
        print("-" * 10)
        for row in state:
            print(row)
