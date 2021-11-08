# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:41:47 2021

@author: gabriel
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y = np.linspace(0, 5, 6)
X, Y = np.meshgrid(x, y)
print(X)
print(Y)

fig, ax = plt.subplots(1)
ax.set_aspect('equal')

ax.plot(X.flatten(), Y.flatten(), '.', c='0', ms=2)
ax.set_xticks(x)
ax.set_yticks(y)
# ax.set_xticklabels([])
# ax.set_yticklabels([])

plt.savefig("regular_grid.png", dpi=300, bbox_inches='tight')