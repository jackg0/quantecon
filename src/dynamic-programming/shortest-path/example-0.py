'''
Shortest Path in a Weighted Directed Graph Using Dynamic Programming.

Solution uses vectorization compared to the solution given in the lecture notes.
'''

import numpy as np
from numpy import inf

Q = np.array([[inf, 1,   5,   3,   inf, inf, inf],
              [inf, inf, inf, 9,   6,   inf, inf],
              [inf, inf, inf, inf, inf, 2,   inf],
              [inf, inf, inf, inf, inf, 4,   8],
              [inf, inf, inf, inf, inf, inf, 4],
              [inf, inf, inf, inf, inf, inf, 1],
              [inf, inf, inf, inf, inf, inf, 0]])

num_nodes = 7
J_n = [0 for _ in range(num_nodes)]
J_next = [0 for _ in range(num_nodes)]
n = 0
i, max_iter = 0, 500

while i < max_iter:
    min_cost = np.min(Q + J_n, axis=1)
    J_next = min_cost

    if np.all(J_next == J_n):
        break

    J_n = J_next
    i += 1

print(J_n)
print(J_n[0])
