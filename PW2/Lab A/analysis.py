"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
print("mean acceleration:", np.mean(a))
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = y[0] + cumulative_trapezoid(v_rec, t, initial=0)
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axs = plt.subplots(3, 1, figsize=(10, 8))
axs[0].plot(t, y)
axs[0].set_ylabel("position (m)")
axs[0].set_xlabel("time (s)")
axs[1].plot(t, v)
axs[1].set_ylabel("velocity (m/s)")
axs[1].set_xlabel("time (s)")
axs[2].plot(t, a)
axs[2].set_ylabel("acceleration (m/s^2)")
axs[2].set_xlabel("time (s)")
axs[2].axhline(-9.81, color="red", linestyle="--")
plt.tight_layout()
plt.savefig("motion.png")
trajectory = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
t2 = trajectory[:, 0]
x2 = trajectory[:, 1]
y2 = trajectory[:, 2]
vx = np.gradient(x2, t2)
vy = np.gradient(y2, t2)
speed = np.sqrt(vx**2 + vy**2)
plt.figure()
plt.plot(x2, y2)
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("trajectory")
plt.savefig("trajectory.png")
plt.figure()
plt.plot(t2, speed)
plt.xlabel("time (s)")
plt.ylabel("speed (m/s)")
plt.title("speed vs timep")
plt.savefig("speed.png")

