from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

path = "C:\\Users\\bubbl\\OneDrive\\Desktop\\for_3d_graph.csv"

x = np.arange(1.0, 5.0, 1.0)
y = np.arange(1.0, 5.0, 1.0)

data = np.loadtxt(path, 
skiprows=1,
usecols=(1,2,3),
encoding="utf-8",
dtype = None, 
delimiter = "\t"
)

#data = data.replace('"', '')
print(data)