import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
shape_description = [
( 1., 2., mpath.Path.MOVETO),
( 1., 1., mpath.Path.LINETO),
( 2., 1., mpath.Path.LINETO),
( 2., -1., mpath.Path.LINETO),
( 1., -1., mpath.Path.LINETO),
( 1., -2., mpath.Path.LINETO),
(-1., -2., mpath.Path.LINETO),
(-1., -1., mpath.Path.LINETO),
(-2., -1., mpath.Path.LINETO),
(-2., 1., mpath.Path.LINETO),
(-1., 1., mpath.Path.LINETO),
(-1., 2., mpath.Path.LINETO),
( 0., 0., mpath.Path.CLOSEPOLY),
]
u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asarray((u, v)).T, codes)
data = np.random.rand(10, 10)
plt.scatter(data[:,0], data[:, 1], c = 'b', marker = my_marker, s = 120)
plt.show()
print('#',50*"-")