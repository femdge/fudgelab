import numpy as np

class Matrix:

    dim = 1
    rows = np.empty(dim)
    cols = np.empty(dim)

    def __init__(self, dim):

        dim = self.dim
        rows = np.empty(dim)
        cols = np.empty(dim)

    def rowAssign(dim, rows):

        row = np.empty(dim)

        for j in range(dim):

            rraw = input("type vector numbers \n") #splits raw numbers to fit into vector
            rraw = rraw.split(" ")
            for i in range(dim):
                row[i] = float(rraw[i])

        rows[j] = row

    def colAssign(dim, rows, cols):

        col = np.empty(dim)

        for j in range(dim):

            for i in range(dim):
                col[i] = rows[i][j]

            cols[j] = col

    
