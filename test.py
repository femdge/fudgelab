import numpy as np
import pandas as pd


dim = int(input("input vector dimension \n"))
vector = np.empty(dim)

vraw = input("type vector numbers \n") #splits raw numbers to fit into vector
vraw = vraw.split(" ")
for i in range(dim):
    vector[i] = float(vraw[i])

