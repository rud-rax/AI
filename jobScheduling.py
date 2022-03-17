class AdjList:
    def __init__(self, deadline_range=10):

        self.g = {}
        for i in range(1, deadline_range):
            self.g[i] = []

        self.schedule = []

    def addJob(self, job, profit, deadline):
        self.g[deadline].append([job, profit])

    def sortJobs(self):

        for key in self.g.keys():

            if self.g[key] == []:
                continue

            max_pr = self.g[key][0][1]
            max_pr_job = self.g[key][0][0]
            for jo, pr in self.g[key][1:]:

                if pr > max_pr:
                    max_pr_job = jo
                    max_pr = pr
            self.schedule.append([max_pr_job, max_pr])

            # print(max_pro)

    def printAdjMat(self):
        # print(self.g)

        for k in self.g.keys():
            print(k, end=" > ")
            for jo, pr in self.g[k]:

                print(f"[ {jo} : {pr} ]", end=" -- ")
            print("* \n|")

        print("*")

    def calculateMaxProfit(self):

        self.sortJobs()
        max_profit = 0
        print("JOBS = ", end=" ")
        for jo, pr in self.schedule:
            max_profit += pr
            print(jo, end=" ")

        print(f"\nMAX PROFIT = {max_profit}")
        return max_profit


if __name__ == "__main__":
    g1 = AdjList()
    g1.addJob("J1", 28, 1)
    g1.addJob("J2", 100, 2)
    g1.addJob("J3", 15, 2)
    g1.addJob("J4", 30, 1)

    g1.printAdjMat()
    # g1.sortJobs()
    # print(g1.schedule)
    g1.calculateMaxProfit()
