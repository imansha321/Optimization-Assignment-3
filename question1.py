
import numpy as np
import matplotlib.pyplot as plt

# Problem:
# Minimize x^2 subject to x >= 1
# L(mu, x) = x^2 + mu(1 - x), mu >= 0


# ==================================================
# PART (a): Plot the Lagrangian
# ==================================================

x = np.linspace(-1, 3, 500)
mu_values = [0, 1, 2, 3]

plt.figure(figsize=(9, 6))

for mu in mu_values:
    L = x**2 + mu * (1 - x)

    # Minimizer of L with respect to x
    # ∂L/∂x = 2x - mu = 0
    # x = mu/2  

    x_min = mu / 2
    L_min = x_min**2 + mu * (1 - x_min)

    plt.plot(x, L, label=f"mu = {mu}")
    plt.scatter(x_min, L_min, s=60)

    plt.annotate(
        f"x = {x_min:.1f}",
        (x_min, L_min),
        xytext=(5, 8),
        textcoords="offset points"
    )

plt.xlabel("x")
plt.ylabel("L(mu, x)")
plt.title("Part (a): Lagrangian for Different Values of mu")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ==================================================
# PART (b): Plot the dual function
# ==================================================

# d(mu) = mu - mu^2 / 4, for mu >= 0

mu = np.linspace(0, 4, 500)
d = mu - mu**2 / 4

# Dual optimum
mu_star = 2
d_star = mu_star - mu_star**2 / 4

plt.figure(figsize=(8, 5))

plt.plot(mu, d, label="d(mu) = mu - mu^2/4")
plt.scatter(
    mu_star, d_star,
    color="red",
    s=70,
    label=f"Optimum ({mu_star}, {d_star:.0f})",
    zorder=3
)

plt.axvline(mu_star, linestyle="--", alpha=0.7)
plt.axhline(d_star, linestyle="--", alpha=0.7)

plt.xlabel("mu")
plt.ylabel("d(mu)")
plt.title("Part (b): Dual Function")
plt.xlim(0, 4)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ==================================================
# PART (c): Plot the primal function
# ==================================================

# g(x) = +infinity for x < 1
# g(x) = x^2 for x >= 1


x_feasible = np.linspace(1, 3, 300)
g_feasible = x_feasible**2

plt.figure(figsize=(9, 5.5))

# Plot the finite part of g(x)
plt.plot(
    x_feasible,
    g_feasible,
    linewidth=2,
    label="g(x) = x^2, x >= 1"
)

# Minimum
plt.scatter(
    [1], [1],
    color="red",
    s=70,
    label="Minimum at (1, 1)",
    zorder=3
)

# Infeasible region
plt.axvspan(
    -1, 1,
    color="gray",
    alpha=0.15,
    label="Infeasible: g(x) = +infinity"
)

plt.axvline(1, linestyle="--", color="black", alpha=0.7)


plt.xlim(-1, 3)
plt.ylim(0, 10)
plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("Part (c): Primal Function")
plt.legend(loc="upper left")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()