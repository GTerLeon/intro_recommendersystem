import numpy as np
import matplotlib.pyplot as plt

# Define the true success probabilities for 10 treatments (hard-coded for consistency)
true_success_rates = np.array([0.1, 0.3, 0.5, 0.7, 0.2, 0.4, 0.6, 0.8, 0.25, 0.55])

# Number of treatments and days
num_treatments = len(true_success_rates)
total_days = 100
patience_threshold = 3  # Number of failures before eliminating a treatment

def simulate_patient(treatment_idx):
    """Simulates a patient's response to a given treatment."""
    return np.random.rand() < true_success_rates[treatment_idx]

# Track records for each treatment
success_counts = np.zeros(num_treatments)
failure_counts = np.zeros(num_treatments)
available_treatments = set(range(num_treatments))  # Start with all treatments available

daily_success = []

def weighted_choice(weights):
    """Select an index based on weighted probability."""
    total = sum(weights)
    probs = [w / total for w in weights]
    return np.random.choice(range(len(weights)), p=probs)

for day in range(total_days):
    if day < num_treatments:
        # Initial exploration: Try each treatment once
        chosen_treatment = day
    else:
        # Ensure at least one treatment remains available
        if not available_treatments:
            available_treatments = set(range(num_treatments))  # Reset if all eliminated
            success_counts = np.zeros(num_treatments)
            failure_counts = np.zeros(num_treatments)
        
        # Weighted selection: Favor treatments with higher success rates
        weights = [success_counts[i] + 1 for i in available_treatments]  # +1 to avoid zero-weight
        chosen_treatment = list(available_treatments)[weighted_choice(weights)]
    
    # Apply the treatment
    success = simulate_patient(chosen_treatment)
    
    # Update records
    if success:
        success_counts[chosen_treatment] += 1
    else:
        failure_counts[chosen_treatment] += 1
    
    # Check for elimination based on patience threshold
    if failure_counts[chosen_treatment] >= patience_threshold and len(available_treatments) > 1:
        available_treatments.discard(chosen_treatment)
    
    daily_success.append(sum(success_counts))
    
# Plot results
plt.plot(range(1, total_days + 1), daily_success, label="Improved Strategy")
plt.xlabel("Days")
plt.ylabel("Cumulative Successes")
plt.title("Treatment Success Over Time")
plt.legend()
plt.show()
