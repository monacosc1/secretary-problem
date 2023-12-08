import numpy as np
import matplotlib.pyplot as plt

def simulate_secretary_problem(num_candidates=100, num_simulations=1000):
    best_candidate_results = {i: 0 for i in range(num_candidates)}
    
    for _ in range(num_simulations):
        # Generate a random order of candidates
        candidates = np.random.permutation(num_candidates) + 1  # Adding 1 to have rankings from 1 to 100

        for stopping_point in range(num_candidates):
            best_seen = max(candidates[:stopping_point]) if stopping_point > 0 else 0
            for candidate in candidates[stopping_point:]:
                if candidate > best_seen:
                    # Candidate selected - check if it's the best
                    if candidate == num_candidates:  # Best candidate has rank 100
                        best_candidate_results[stopping_point] += 1
                    break

    # Normalize results to get probabilities
    for stopping_point in best_candidate_results:
        best_candidate_results[stopping_point] /= num_simulations

    return best_candidate_results

# Run the simulation
simulation_results = simulate_secretary_problem()
simulation_results

# Graph the results
# Extracting the stopping points and their corresponding probabilities
stopping_points = list(simulation_results.keys())
probabilities = list(simulation_results.values())

# File path for saving the graph
file_path = './images/secretary_problem_simulation_graph.png'

# Creating and saving the plot
plt.figure(figsize=(12, 6))
plt.plot(stopping_points, probabilities, marker='o', color='b')
plt.title('Probability of Selecting the Best Candidate vs. Stopping Point')
plt.xlabel('Stopping Point (Number of Candidates Interviewed and Rejected)')
plt.ylabel('Probability of Selecting the Best Candidate')
plt.grid(True)
plt.axvline(x=37, color='r', linestyle='--', label='Approx. Theoretical Optimal Point (n/e)')
plt.legend()

# Save the plot to the specified file path
plt.savefig(file_path)

plt.show()
