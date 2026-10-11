
import numpy as np
import matplotlib.pyplot as plt

# Optimal solutions
x_star = 1
mu_star = 2

# Common saddle-point value
common_value = x_star**2 + mu_star * (1 - x_star)

# Graph 1: L(mu, x*) against mu
mu = np.linspace(0, 5, 300)
L1 = x_star**2 + mu * (1 - x_star)

# Graph 2: L(mu*, x) against x
x = np.linspace(-2, 4, 300)
L2 = x**2 + mu_star * (1 - x)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# First graph
axes[0].plot(mu, L1, label=r'$L(\mu, x^*)$')
axes[0].axhline(
    common_value, color='red', linestyle='--',
    label=r'$L(\mu^*,x^*)=1$'
)
axes[0].scatter(mu_star, common_value, color='black', zorder=3)
axes[0].set_xlabel(r'$\mu$')
axes[0].set_ylabel(r'$L(\mu,x^*)$')
axes[0].set_title(r'$L(\mu,x^*)$ against $\mu$')
axes[0].legend()
axes[0].grid(True)

# Second graph
axes[1].plot(
    x, L2, label=r'$L(\mu^*,x)=(x-1)^2+1$'
)
axes[1].axhline(
    common_value, color='red', linestyle='--',
    label=r'$L(\mu^*,x^*)=1$'
)
axes[1].scatter(x_star, common_value, color='black', zorder=3)
axes[1].annotate(
    '(1, 1)', (x_star, common_value),
    xytext=(10, 10), textcoords='offset points'
)
axes[1].set_xlabel(r'$x$')
axes[1].set_ylabel(r'$L(\mu^*,x)$')
axes[1].set_title(r'$L(\mu^*,x)$ against $x$')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
