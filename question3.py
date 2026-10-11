
import numpy as np
import matplotlib.pyplot as plt

# Lagrangian lines for x = 0, 1, 2
mu = np.linspace(0, 5, 500)

L_x0 = mu           
L_x1 = np.ones_like(mu)  
L_x2 = 4 - mu       

# Lower envelope of the three lines
lower_envelope = np.minimum.reduce([L_x0, L_x1, L_x2])

# Plot the three lines
plt.figure(figsize=(9, 5))

plt.plot(mu, L_x0, label=r'$L(\mu,0)=\mu$')
plt.plot(mu, L_x1, label=r'$L(\mu,1)=1$')
plt.plot(mu, L_x2, label=r'$L(\mu,2)=4-\mu$')

# Plot the lower envelope
plt.plot(
    mu, lower_envelope,
    color='black', linewidth=3, linestyle='--',
    label='Lower envelope'
)

plt.xlabel(r'$\mu$')
plt.ylabel(r'$L(\mu,x)$')
plt.title('Lagrangian Lines and Their Lower Envelope')
plt.xlim(0, 5)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
