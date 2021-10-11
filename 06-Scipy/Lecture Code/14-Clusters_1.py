import numpy
import scipy
import matplotlib.pyplot as plt


from scipy.cluster.hierarchy import linkage, dendrogram

file=open("data.dat","r")
lines=file.readlines()
file.close()
mammals=[]
dataset=numpy.zeros((len(lines),8))
for index,line in enumerate(lines):
    mammals.append( line[0:27].rstrip(" ").capitalize() )
    for tooth in range(8):
        dataset[index,tooth]=int(line[27+tooth])

plt.rcParams['figure.figsize'] = (10.0, 20.0)

Z=linkage(dataset)
dendrogram(Z, labels=mammals, orientation="right")
plt.show()