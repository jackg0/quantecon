'''
Shortest Path in a Weighted Directed Graph Using Dynamic Programming.

Solution uses vectorization compared to the solution given in the lecture notes.
'''

import numpy as np
from numpy import inf


node_weights = []
destination_node = 99
starting_node = 13
num_nodes = 100
Q = inf*np.ones((num_nodes, num_nodes))


def map_file_to_distance_matrix(file, destination_node):
    with open(file) as f:
        line = f.readline()
        while line:
            line = f.readline().rstrip()

            if not line:
                break

            nodes = line.split(',')
            conn_nodes = nodes[1:]
            current_node = int(nodes[0][4:])

            for conn_node in conn_nodes:
                if not conn_node:
                    break

                conn_node = conn_node.lstrip()

                node_loc = int(conn_node.split(' ')[0][4:])
                weight = float(conn_node.split(' ')[1])

                Q[current_node, node_loc] = weight

    Q[destination_node, destination_node] = 0.0

    return Q


def bellman_eqn(J, Q):
    min_cost = np.min(Q + J, axis=1)
    J_next = min_cost
    return J_next


def bellman_from_solution(J, Q):
    num_nodes = Q.shape[0]
    next_J = np.zeros_like(J)
    for v in range(num_nodes):
        next_J[v] = np.min(Q[v, :] + J)
    return next_J


def compute_cost_to_go(Q):
    J = np.zeros((num_nodes,))
    n = 0
    i, max_iter = 0, 500

    while i < max_iter:
        J_next = bellman_eqn(J, Q)
        if np.allclose(J_next, J):
            break
        J[:] = J_next
        i += 1

    return J


Q = map_file_to_distance_matrix("exercise-1.txt", destination_node)
J = compute_cost_to_go(Q)

best_path = [starting_node]
while best_path[-1] != destination_node:
    node = np.argmin(Q + J, axis=1)[best_path[-1]]
    best_path.append(node)

print(best_path)
print("Cost:", J[starting_node])
