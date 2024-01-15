import random

def assign_prisoner_numbers(num_prisoners: int) -> list:
    # Assign numbers corresponding to each prisoner
    return list(range(1, num_prisoners + 1))

def shuffle_drawers(num_prisoners: int) -> list:
    # Initialize drawers with numbers matching prisoner IDs.
    drawers = list(range(1, num_prisoners + 1))
    # Shuffle drawers list.
    random.shuffle(drawers)
    return drawers

def prisoner_find_own_number(prisoner_number: int, opened_drawers: list) -> bool:
    # Check if the prisoner's number is in the opened drawers
    return prisoner_number in opened_drawers

def is_in_loop(prisoner_number: int, opened_drawers: list) -> bool:
    loop_start = opened_drawers.index(prisoner_number)
    loop_numbers = set(opened_drawers[loop_start:])
    return all((i+1) in loop_numbers for i in range(len(opened_drawers) - loop_start))

def simulate_single_experiment(num_prisoners: int, num_drawers_to_open: int = 50) -> bool:
    prisoners = assign_prisoner_numbers(num_prisoners)
    opened_drawers = shuffle_drawers(num_prisoners)

    for prisoner_number in prisoners:
        opened_drawers_prisoner = opened_drawers[:num_drawers_to_open]

        if prisoner_find_own_number(prisoner_number, opened_drawers_prisoner):
            if is_in_loop(prisoner_number, opened_drawers_prisoner):
                return True
            else:
                return False
    return False

def repeat_experiments(num_experiments: int = 1000, num_prisoners : int = 100, num_drawers_to_open: int = 50) -> float:
    success_count = 0
    
    for _ in range(num_experiments):
        if simulate_single_experiment(num_prisoners, num_drawers_to_open):
            success_count += 1

    # Check how many experiments were successful.
    probability = success_count / num_experiments
        
    return probability

if __name__ == "__main__":
    # Get num_experiments input
    num_experiments_input = input("How many tries to simulate? (Default: 1000): ")

    # Check if the input is a valid positive integer
    try:
        num_experiments = int(num_experiments_input) if num_experiments_input else 1000
        if num_experiments <= 0:
            raise ValueError("Number of experiments should be a positive integer.")
    except ValueError:
        print("Invalid input. Using the default value of 1000 experiments.")
        num_experiments = 1000

    # Repeat the experiments and print the final result.
    final_result = repeat_experiments(num_experiments=num_experiments)
    print(f"Success Probability of '100 Prisoners Problem': {final_result: .3%}")

