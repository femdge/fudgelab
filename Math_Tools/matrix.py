import numpy as np

class Matrix:

    dim = None

    def __init__(self, dim):

        self.dim = dim
        self.rows = np.eye(dim)
        self.cols = np.eye(dim)
        self.rowAssign()
        self.colAssign()


    def rowAssign(self):

        row = np.arange(self.dim)

        for j in range(self.dim):

            rraw = input("type vector numbers \n") #splits raw numbers to fit into vector
            rraw = rraw.split(" ")
            for i in range(self.dim):
                row[i] = float(rraw[i])

            self.rows[j] = row

    def colAssign(self):

        col = np.arange(self.dim)

        for j in range(self.dim):

            for i in range(self.dim):
                col[i] = self.rows[i][j]

            self.cols[j] = col

    def printRows(self):

        print("rows:")
        for i in range(self.dim):
            print(str(self.rows[i]))

    def printCols(self):

        print("collumns:")
        for i in range(self.dim):
            print(str(self.cols[i])) 