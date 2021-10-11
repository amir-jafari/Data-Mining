import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
# Circle
shape = patches.Circle((0, 0), radius = 1., color = '.75')
plt.gca().add_patch(shape)
# Rectangle
shape = patches.Rectangle((2.5, -.5), 2., 1., color = '.75')
plt.gca().add_patch(shape)
# Ellipse
shape = patches.Ellipse((0, -2.), 2., 1., angle = 45., color =
'.75')
plt.gca().add_patch(shape)
# Fancy box
shape = patches.FancyBboxPatch((2.5, -2.5), 2., 1., boxstyle =
'sawtooth', color = '.75')
plt.gca().add_patch(shape)
# Display all
plt.grid(True)
plt.axis('scaled')
plt.show()
print('#',50*"-")