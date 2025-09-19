# Create three illustrative regression figures arranged in a row.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

# Parameters
a = 0.8     # slope
b = 0.0     # intercept
mu_x = 2.0  # mean of x
sigma_x = 1.0  # std dev of x
n = 80

# Data
x = np.random.normal(mu_x, sigma_x, size=n)
eps = np.random.normal(0, 0.7, size=n)
y = b + a * x + eps


fig, axs = plt.subplots(1, 3, figsize=(12, 4), constrained_layout=True)

# --------- Left panel: scatter, line, mu_x line, example residual, sigma_x bar ---------
ax = axs[0]
ax.scatter(x, y, s=14, alpha=0.7)
xx = np.linspace(0, mu_x + 3*sigma_x, 100)
ax.plot(xx, b + a*xx, linewidth=2)

# vertical line at mu_x
ax.axvline(mu_x, linestyle='--', linewidth=1)
ax.text(mu_x, ax.get_ylim()[0] + 0.1*(ax.get_ylim()[1]-ax.get_ylim()[0]), r'$\mu_x$', ha='center', va='bottom')

# pick a representative point near mu_x to show residual
ix = np.argmin(np.abs(x - mu_x))
x0, y0 = x[ix], y[ix]
yhat0 = b + a*x0
ax.plot([x0, x0], [y0, yhat0], linewidth=2)  # residual "bar"
ax.text(x0 + 0.05*(ax.get_xlim()[1]-ax.get_xlim()[0]), (y0 + yhat0)/2, r'$\varepsilon$', va='center')

# sigma_x bracket (one std dev) along x-axis
x_left, x_right = mu_x - sigma_x, mu_x + sigma_x
y_base = ax.get_ylim()[0] + 0.06*(ax.get_ylim()[1]-ax.get_ylim()[0])
ax.plot([x_left, x_right], [y_base, y_base], linewidth=3)
ax.plot([x_left, x_left], [y_base-0.12, y_base+0.12], linewidth=2)
ax.plot([x_right, x_right], [y_base-0.12, y_base+0.12], linewidth=2)
ax.text((x_left + x_right)/2, y_base + 0.18, r'$\sigma_x$', ha='center', va='bottom')

# tiny right-angle near origin to suggest slope "a"
# draw a small triangle and label "a"
ra_x = 0.6
ax.plot([0, ra_x], [0, 0], linewidth=2)
ax.plot([ra_x, ra_x], [0, a*ra_x], linewidth=2)
ax.plot([0, ra_x], [0, a*ra_x], linewidth=2)
ax.text(0.05 + ra_x/2, a*ra_x/2, r'$\beta_1$', ha='left', va='bottom')

ax.set_xlim(0, mu_x + 3*sigma_x)
ax.set_ylim(0, max(y.max(), (b+a*(mu_x+3*sigma_x))) + 1)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
#ax.set_title('Data, fit, and annotations')

# --------- Top-right panel: effect of a unit change in x on mean (label "+ a") ---------
ax = axs[1]
ax.scatter(x, y, s=12, alpha=0.4)
ax.plot(xx, b + a*xx, linewidth=2)

# bracket indicating unit change in x and corresponding change in mean a
x1 = mu_x
x2 = mu_x + 1.0
y1 = b + a*x1
y2 = b + a*x2
# unit step on x
ax.plot([x1, x2], [y1, y1], linewidth=3)
ax.plot([x1, x1], [y1-0.15, y1+0.15], linewidth=2)
ax.plot([x2, x2], [y1-0.15, y1+0.15], linewidth=2)
ax.text((x1+x2)/2, y1-0.35, '1', ha='center')

# response step "a"
ax.plot([x2, x2], [y1, y2], linewidth=3)
ax.text(x2 + 0.1, (y1+y2)/2, r'$+\,\beta_1$', va='center')


ax.set_xlim(0, mu_x + 3*sigma_x)
ax.set_ylim(0, max(y.max(), (b+a*(mu_x+3*sigma_x))) + 1)
ax.set_xlabel(r'$x$')
#ax.set_title('Unit step in $x$ implies +a in mean $y$')

# --------- Bottom-right panel: variability due to x-spread (label "+ σ_x^2") ---------
ax = axs[2]
ax.scatter(x, y, s=12, alpha=0.4)
ax.plot(xx, b + a*xx, linewidth=2)

# show +/- sigma band on x
ax.axvline(mu_x, linestyle='--', linewidth=1)
ax.plot([x_left, x_right], [y_base, y_base], linewidth=3)
ax.plot([x_left, x_left], [y_base-0.12, y_base+0.12], linewidth=2)
ax.plot([x_right, x_right], [y_base-0.12, y_base+0.12], linewidth=2)
ax.text((x_left + x_right)/2, y_base + 0.18, r'$\sigma_x$', ha='center', va='bottom')

# label for variance contribution
ax.text(mu_x + 1.2*sigma_x, b + a*(mu_x + 1.2*sigma_x), r'$+\ \sigma_x^2$', ha='left', va='bottom')


ax.set_xlim(0, mu_x + 3*sigma_x)
ax.set_ylim(0, max(y.max(), (b+a*(mu_x+3*sigma_x))) + 1)
ax.set_xlabel(r'$x$')
#ax.set_title('Spread in $x$ highlighted')
plt.savefig("./figures/cov_effect.pdf", bbox_inches="tight")
