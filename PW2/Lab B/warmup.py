import numpy as np 
from scipy.optimize import newton, minimize

def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def ddf(x):
    return 2

x = 0.0
learning_rate = 0.1
for i in range(100):
    x = x - learning_rate * df(x)

print("gradient descent:", x)

x_newton = newton(df, x0=0, fprime=ddf)

print("newton:", x_newton)

result = minimize(f, x0=[0], method="SLSQP")

print("SLSQP:", result.x[0])

def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def ddg(x):
    return 12*x**2 - 6

x = 0.0
learning_rate = 0.01
for i in range(1000):
    x = x - learning_rate * dg(x)

print("gradient descent g(x), x0=0:", x)

x_newton_g = newton(dg, x0=0, fprime=ddg)

print("newton g(x), x0=0:", x_newton_g)
print("second derivative at newton point:", ddg(x_newton_g))

result_g = minimize(g, x0=[0], method="SLSQP")

print("SLSQP g(x), x0=0:", result_g.x[0])

result_g2 = minimize(g, x0=[2], method="SLSQP")

print("SLSQP g(x), x0=2:", result_g2.x[0])

result_g3 = minimize(g, x0=[1], method="SLSQP")

print("SLSQP g(x), x0=1:", result_g3.x[0])

print("g(-1.30):", g(-1.30))
print("g(1.13):", g(1.13))

print("g(newton):", g(x_newton_g))

import matplotlib.pyplot as plt
x_values = np.linspace(-3, 3, 400)
y_values = g(x_values)
plt.plot(x_values, y_values)
plt.scatter(-1.30, g(-1.30), color = "red")
plt.scatter(1.13, g(1.13), color="green")
plt.scatter(0.17, g(0.17), color="blue")
plt.savefig("PW2/Lab B/optimization.png")
plt.show()




