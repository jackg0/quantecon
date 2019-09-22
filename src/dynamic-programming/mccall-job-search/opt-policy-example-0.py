import numpy as np
from numba import jit
import matplotlib.pyplot as plt
import quantecon as qe
from quantecon.distributions import BetaBinomial

n, a, b = 50, 200, 100
w_min, w_max = 10, 60
w_vals = np.linspace(w_min, w_max, n+1)
dist = BetaBinomial(n, a, b)
psi_vals = dist.pdf()


def plot_w_distribution(w_vals, psi_vals):
    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.stem(w_vals, psi_vals, label='$\phi (w\')$')
    ax.set_xlabel('wages')
    ax.set_ylabel('probabilities')
    plt.show()


def optimal_policy_step(v, w_weights, w, beta=0.99, unemployment=25):
    v_next = np.maximum(w / (1 - beta),
                        unemployment + beta*np.dot(v, w_weights))

    return v_next


def compute_reservation_wage(w, w_weights, max_iter=500, epsilon=1e-6, beta=0.99, unemployment=25):
    v = w / (1 - beta)

    i = 0
    error = epsilon + 1

    while i < max_iter and error > epsilon:
        v_next = optimal_policy_step(
            v, w_weights, w, beta=beta, unemployment=unemployment)

        error = np.max(np.abs(v_next - v))
        v = v_next
        i += 1

    reservation_wage = (1 - beta) * (unemployment + beta*np.dot(v, w_weights))
    return reservation_wage


reservation_wage = compute_reservation_wage(w_vals, psi_vals)


print(reservation_wage)
