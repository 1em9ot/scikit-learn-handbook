import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def simulate_ar1(alpha, sigma, T, n_simulations=1):
    """
    Simulates an AR(1) process: y_t = alpha * y_{t-1} + epsilon_t
    epsilon_t ~ N(0, sigma^2)
    """
    y = np.zeros((n_simulations, T))
    epsilon = np.random.normal(0, sigma, (n_simulations, T))

    # Assume y_0 comes from the stationary distribution N(0, sigma^2 / (1 - alpha^2))
    # or just start at 0 and burn-in. Let's use stationary distribution start.
    if abs(alpha) < 1:
        stationary_variance = sigma**2 / (1 - alpha**2)
        y[:, 0] = np.random.normal(0, np.sqrt(stationary_variance), n_simulations)
    else:
        y[:, 0] = epsilon[:, 0]

    for t in range(1, T):
        y[:, t] = alpha * y[:, t-1] + epsilon[:, t]

    return y

def theoretical_variance_of_sample_mean(alpha, sigma, T):
    """
    Calculates the theoretical variance of the sample mean for an AR(1) process.
    Formula: (sigma^2 / T^2) * [T * gamma_0 + 2 * sum_{h=1}^{T-1} (T-h) * gamma_h]
    where gamma_h = alpha^h * gamma_0
    and gamma_0 = sigma^2 / (1 - alpha^2)
    """
    if abs(alpha) >= 1:
        return np.inf # Not stationary

    gamma_0 = sigma**2 / (1 - alpha**2)

    # Summation term: sum_{h=1}^{T-1} (T-h) * alpha^h
    h = np.arange(1, T)
    sum_term = np.sum((T - h) * (alpha ** h))

    # Correct formula derivation integration
    # Var(y_bar) = (1/T^2) * [ T*gamma_0 + 2 * sum((T-h)*gamma_h) ]
    #            = (gamma_0 / T^2) * [ T + 2 * sum((T-h)*alpha^h) ]

    variance = (gamma_0 / T**2) * (T + 2 * sum_term)
    return variance

# Parameters
alpha = 0.5
sigma = 1.0
T = 100
n_simulations = 10000

# 1. Simulation for Variance Verification
print(f"Running {n_simulations} simulations of AR(1) with alpha={alpha}, sigma={sigma}, T={T}...")
simulated_data = simulate_ar1(alpha, sigma, T, n_simulations)
sample_means = np.mean(simulated_data, axis=1)
empirical_variance = np.var(sample_means, ddof=1) # Unbiased estimator

theoretical_var = theoretical_variance_of_sample_mean(alpha, sigma, T)
iid_variance = (sigma**2 / (1-alpha**2)) / T # If it were IID with the same process variance

print(f"Theoretical Variance of Sample Mean: {theoretical_var:.6f}")
print(f"Empirical Variance of Sample Mean:   {empirical_variance:.6f}")
print(f"IID Variance (for comparison):       {iid_variance:.6f}")
print(f"Ratio (AR(1) / IID):                 {theoretical_var / iid_variance:.4f}")

# 2. Generate Plot for a single realization
y_single = simulated_data[0, :]

plt.figure(figsize=(12, 6))

# Time Series Plot
plt.subplot(1, 2, 1)
plt.plot(y_single, label=f'AR(1) alpha={alpha}')
plt.title(f'AR(1) Process Simulation (T={T})')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Autocorrelation Plot
# Calculate ACF manually or use statsmodels (but avoiding extra dependency if possible)
def autocorrelation(x):
    n = len(x)
    variance = x.var()
    x = x - x.mean()
    r = np.correlate(x, x, mode = 'full')[-n:]
    result = r / (variance * (np.arange(n, 0, -1)))
    return result

acf = autocorrelation(y_single)
lags = 20
theoretical_acf = alpha ** np.arange(lags)

plt.subplot(1, 2, 2)
plt.stem(range(lags), acf[:lags], label='Sample ACF')
plt.plot(range(lags), theoretical_acf, 'r--', label='Theoretical ACF')
plt.title('Autocorrelation Function')
plt.xlabel('Lag')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('ar_plot.png')
print("Plot saved to ar_plot.png")
