from scipy.optimize import minimize  # for optimization
import scipy.integrate as integrate
import numpy as np  # for numerical operations

def f(t):
    return 1-(1-np.exp(-t)*(1+t))


def average_cost(tau):
    result, _ = integrate.quad(f, 0, tau)
    return (1 - np.exp(-tau)) / result

# Initial guess for tau
initial_guess = 1.0

# Find the minimum of the average_cost function
result = minimize(average_cost, initial_guess)

# Optimal tau value is stored in the solution attribute
optimal_tau = result.x[0]

print("Optimal value of tau to minimize average cost:", optimal_tau)