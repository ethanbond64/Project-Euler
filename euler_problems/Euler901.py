



# Start with fixed bounds d in 0 - 100


import math
from typing import List


# Integral of inverse water function from lower to upper
def probability_water_in_bounds(lower_bound: float, upper_bound: float):
    print(lower_bound, upper_bound)
    
    if upper_bound <= lower_bound:
        raise Exception("Invalid bounds")
    
    lower_result = math.exp(-lower_bound) - 1
    print("lr", lower_result)
    upper_result = math.exp(-upper_bound) - 1
    print("ur", upper_result)

    return lower_result - upper_result


def simulate_strategy(drill_list: List[float]):

    if len(set(drill_list)) != len(drill_list):
        raise Exception("Duplicates in drill list")

    sorted_drill_list = list(sorted(drill_list))

    previous_time = 0
    total_expected_time = 0

    for i, drill_distance in enumerate(sorted_drill_list):

        lower_bound = 0 if i == 0 else sorted_drill_list[i-1]
        upper_bound = drill_distance

        section_time = previous_time + drill_distance

        probability_water = probability_water_in_bounds(lower_bound, upper_bound)
        print(probability_water)

        section_expected_time = section_time * probability_water
        total_expected_time += section_expected_time

        previous_time += drill_distance

    return total_expected_time


# NOTE UPPER BOUND OF 40 is sufficient


if __name__ == "__main__":
    print("TOTAL", simulate_strategy([1, 1.1, 1.3, 2, 3.5, 9, 16, 25, 17, 0.2, 0.3, 0.4, 40]))
    print("TOTAL", simulate_strategy([0.1, 0.7, 1, 2, 3, 10, 20, 40]))