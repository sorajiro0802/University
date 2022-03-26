#!/Users/sorakojima/miniforge3/envs/python39/bin/python3
#%%
import numpy as np
import matplotlib.pyplot as plt

X = np.array([ 0.  ,  0.16,  0.22,  0.34,  0.44,  0.5 ,  0.67,  0.73,  0.9 ,  1.  ])
Y = np.array([-0.06,  0.94,  0.97,  0.85,  0.25,  0.09, -0.9 , -0.93, -0.53,  0.08])
fig, ax = plt.subplots(dpi=100)
ax.scatter(X, Y, marker='o', color='b')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid()
# %%
W3 = np.polyfit(X, Y, 3)
W3
# %%
x = np.linspace(0, 1, 1000)
fig, ax = plt.subplots(dpi=100)
ax.scatter(X, Y, marker='o', color='b')
ax.plot(x, np.polyval(W3, x), 'r')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid()
# %%
np.mean((Y - np.polyval(W3, X)) ** 2)
# %%
W9 = np.polyfit(X, Y, 9)
W9
# %%
x = np.linspace(0, 1, 1000)
fig, ax = plt.subplots(dpi=100)
ax.scatter(X, Y, marker='o', color='b')
ax.plot(x, np.polyval(W9, x), 'r')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_ylim(-1.2, 1.2)
ax.grid()
# %%
x = np.linspace(0, 1, 1000)
fig, ax = plt.subplots(dpi=100)
ax.scatter(X, Y, marker='o', color='b')
ax.plot(x, np.polyval(W9, x), 'r')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid()
# %%
np.mean((Y - np.polyval(W9, X)) ** 2)
# %%
W3 = np.polyfit(X, Y, 3)
W9 = np.polyfit(X, Y, 9)

x = np.linspace(0, 1, 1000)
fig, ax = plt.subplots(dpi=100)
ax.scatter(X, Y, marker='o', color='b')
ax.plot(x, np.sin(2 * np.pi * x), 'black', label=r'$\sin(2\pi x)$', linestyle="solid")
ax.plot(x, np.polyval(W3, x), label=r'Polymominal ($d=3$)', linestyle="dotted")
ax.plot(x, np.polyval(W9, x), label=r'Polymominal ($d=9$)', linestyle="dashed")
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_ylim(-1.2, 1.2)
plt.legend(loc='upper right')
fig.savefig('overfitting.png')
ax.grid()

# %%
X_valid = np.array([ 0.05,  0.08,  0.16,  0.28,  0.44,  0.47,  0.55,  0.63,  0.84,   0.99])
Y_valid = np.array([ 0.35,  0.58,  0.87,  0.98,  0.45,  0.01, -0.36, -0.73, -0.85,  -0.06])
# %%
fig, ax = plt.subplots(dpi=100)
ax.scatter(X_valid, Y_valid, marker='x', color='r')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_ylim(-1.2, 1.2)
ax.grid()
# %%
for d in range(1, 10):
    W = np.polyfit(X, Y, d)
    Y_hat = np.polyval(W, X)
    Y_valid_hat = np.polyval(W, X_valid)
    e_train = np.mean((Y_hat - Y)**2)
    e_valid = np.mean((Y_valid_hat - Y_valid) ** 2)
    print(f'd = {d}: MSR = {e_train:.10f} (training), {e_valid:.10f} (validation)')
# %%

# %%
