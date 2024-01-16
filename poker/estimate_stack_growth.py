import random

# Define big blind levels
# last level is first day two level
big_blind_levels = [40, 60, 80, 100, 120, 160, 200, 250, 250, 300, 350, 400, 500, 600, 700, 800, 1000, 1200]

# Define stack change probabilities
bust_chance = 0.10
decrease_chance = 0.20
increase_chance = 0.60
double_chance = 0.10

def simulate_tournament():
    # Starting stack size
    stack = 4000

    # Simulate stack size changes for each big blind level (except the last)
    levels_except_last = big_blind_levels[:-1]
    for big_blind_level in levels_except_last:
        # Generate a random value to determine the stack change
        random_value = random.random()

        # Check the stack change based on probabilities
        if random_value < bust_chance:
            # Bust out (lose all chips)
            stack = 0
            # exit for loop because we cannot continue
            break
        elif random_value < bust_chance + decrease_chance:
            # Decrease stack by half
            stack *= 0.5
        elif random_value < bust_chance + decrease_chance + increase_chance:
            # Increase stack by 25%
            stack *= 1.25
        else:
            # Double stack
            stack *= 2

    return stack

# Simulate 1000 tournaments and calculate average final stack size
results = []
num_tournaments = 100000
for i in range(num_tournaments):
    results.append(simulate_tournament())

# Calculate average final stack size
average_final_stack_size = sum(results) / len(results)
print(f"Average Final Stack Size: {average_final_stack_size:.2f}")

# calculate chance of not busting
not_busted = [result for result in results if result > 0]
print(f"Chance of bagging: {len(not_busted) / len(results) * 100:.2f}%") 

average_final_stack_size = sum(not_busted) / len(not_busted)
print(f"Average stack when bagging: {average_final_stack_size}:.0f")
first_day_two_level = big_blind_levels[-1]
print(f"Average BB starting day 2 when bagging: {average_final_stack_size / first_day_two_level:.1f}"       )

average_bb_include_busts = sum(results) / len(results) / first_day_two_level
print(f"Average BB including busts: {average_bb_include_busts:.1f}")