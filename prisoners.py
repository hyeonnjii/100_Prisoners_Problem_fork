import random

def generate_prisoners(num_prisoners=100) -> list:
    # Create a list with numbers corresponding to each prisoner.
    return list(range(1, num_prisoners + 1))

def simulate_single_experiment(prisoners, max_attempts=50) -> bool:
    # Initialize drawers with numbers matching prisoner IDs.
    drawers = list(range(1, len(prisoners) + 1))  # Corrected drawer numbering

    # Shuffle drawers list.
    random.shuffle(drawers)

    # Initialize a variable to track experiment success.
    experiment_success = False

    # Check if each prisoner finds their own drawer within the maximum attempts.
    for _ in range(max_attempts):
        # Check if all prisoners find their own drawer within the given attempts.
        experiment_success = all(chosen == actual for chosen, actual in zip(drawers, prisoners))
        
        if experiment_success:
            break  # Exit the loop if successful

    return experiment_success

def repeat_experiments(num_experiments=1000) -> float:
    # List comprehension to record experiment results.
    results = [simulate_single_experiment(generate_prisoners()) for _ in range(num_experiments)]

    # Check how many experiments were successful.
    total_success = sum(results)
    
    probability = total_success / num_experiments
        
    return probability

if __name__ == "__main__":
    # Get num_experiments input
    num_experiments = int(input("How many tries to simulate?(Default: 1000): "))
    # Repeat the experiments and print the final result.
    final_result = repeat_experiments(num_experiments)
   
    print(f"Success Probability of '100 Prisoners Problem': {final_result}")

