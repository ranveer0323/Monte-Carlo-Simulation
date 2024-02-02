import numpy as np
import matplotlib.pyplot as plt

# Function to simulate Fermi estimate with n steps using Monte Carlo
def monte_carlo_simulation(n_simulations, n_steps):
    overall_growth_estimates = []
    individual_step_errors = []

    for _ in range(n_simulations):
        # Simulate each step with random errors using normal distribution
        user_acquisition = np.random.normal(1.2, 0.2)  # Example: mean=1.2, std=0.2
        market_trends = np.random.normal(1.1, 0.15)
        user_engagement = np.random.normal(1.15, 0.25)
        monetization_strategy = np.random.normal(1.05, 0.1)
        external_factors = np.random.normal(1.1, 0.2)

        # Calculate the overall growth estimate
        overall_growth = user_acquisition * market_trends * user_engagement * monetization_strategy * external_factors

        # Store the overall growth estimate
        overall_growth_estimates.append(overall_growth)

        # Store the errors of individual steps
        individual_step_errors.append([user_acquisition, market_trends, user_engagement, monetization_strategy, external_factors])

    return overall_growth_estimates, np.array(individual_step_errors)

# Number of simulations and steps
n_simulations = 1000
n_steps = 5

# Perform the Monte Carlo simulation
growth_estimates, individual_step_errors = monte_carlo_simulation(n_simulations, n_steps)

# Calculate the overall error for each simulation
overall_errors = growth_estimates - np.mean(growth_estimates)

# Visualization 1: Plot the distribution of overall growth estimates
plt.hist(growth_estimates, bins=30, density=True, alpha=0.7)
plt.xlabel('Overall User Growth Estimate')
plt.ylabel('Probability Density')
plt.title(f'Monte Carlo Simulation for User Growth (n = {n_steps})')
plt.show()

# Visualization 2: Probability Density Function (Kernel Density Estimate)
plt.figure(figsize=(10, 6))
sns.kdeplot(growth_estimates, shade=True, color='skyblue')
plt.xlabel('Overall User Growth Estimate')
plt.ylabel('Probability Density')
plt.title('Kernel Density Estimate of Overall User Growth')
plt.grid(True)
plt.show()

# Calculate the correlation between individual step errors and overall error
correlations = np.corrcoef(individual_step_errors.T, overall_errors)

# Visualization 3: Correlation Matrix of Individual Step Errors vs. Overall Error
sns.set(rc={'figure.figsize':(8, 6)})  # Set figure size
sns.heatmap(correlations, cmap='coolwarm', vmin=-1, vmax=1, annot=True, fmt='.2f')
plt.xlabel('Individual Step Errors')
plt.ylabel('Overall Error')
plt.title('Correlation Matrix: Individual Step Errors vs. Overall Error')

plt.show()

# Display mean and standard deviation
mean_growth = np.mean(growth_estimates)
std_dev_growth = np.std(growth_estimates)
print(f'Mean Growth: {mean_growth:.2f}, Std Dev: {std_dev_growth:.2f}')
