import numpy as np
a = np.arange(12)**2
i = np.array( [ 1,1,3,8,5 ] )
print(a[i])
j = np.array( [ [ 3, 4], [ 9, 7 ] ] )
print(a[j])
palette = np.array( [ [0, 0, 0 ],# black
                     [255,0, 0 ],# red
                     [0,255, 0 ], # green
                     [0,0, 255 ], # blue
                    [255,255,255]])# white
image = np.array( [ [ 0, 1, 2, 0 ],
                    [ 0, 3, 4, 0 ] ] )
# each value corresponds to a color in the palette
print(palette[image])
print('#',50*"-")