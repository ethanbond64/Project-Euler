from enum import Enum
import math
import random
import time
from typing import List


# Integral of inverse water function from lower to upper
def probability_water_in_bounds(lower_bound: float, upper_bound: float):
    
    if upper_bound <= lower_bound:
        print(lower_bound, upper_bound)
        raise Exception("Invalid bounds")
    
    lower_result = math.exp(-lower_bound)
    upper_result = math.exp(-upper_bound)

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

        section_expected_time = section_time * probability_water
        total_expected_time += section_expected_time

        previous_time += drill_distance

    return total_expected_time

# NOTE UPPER BOUND OF 40 is sufficient
UPPER_BOUND = 40


class Operation(Enum):
    REMOVE = 0
    ADD = 1
    MOVE_UP = 2
    MOVE_DOWN = 3


def genetic_search(unchanged_iterations_to_stop = 100000):

    last_score = math.inf
    last_locations = [40]

    new_locations = None
    iterations_since_change = 0

    while iterations_since_change < unchanged_iterations_to_stop:
        operation = get_random_operation()

        if operation == Operation.REMOVE:
            # Cannot remove upper bound
            if len(last_locations) > 1:
                index = random.randint(0, len(last_locations) - 1)
                if last_locations[index] != UPPER_BOUND:
                    new_locations = list(last_locations)
                    new_locations.pop(index)

        elif operation == Operation.ADD:
            new_value = random.random() * UPPER_BOUND
            new_locations = list(last_locations)
            new_locations.append(new_value)

        elif operation in { Operation.MOVE_UP, Operation.MOVE_DOWN }:
            if len(last_locations) > 1:
                index = random.randint(0, len(last_locations) - 1)
                if last_locations[index] != UPPER_BOUND:
                    new_locations = list(last_locations)
                    delta = random.random() / 10 # TODO scale denominator as time passes
                    current_value = new_locations[index]
                    if operation == Operation.MOVE_UP:
                        new_value = current_value + delta
                        if new_value < UPPER_BOUND:
                            new_locations[index] = new_value
                    else:
                        new_value = current_value - delta
                        if new_value > 0:
                            new_locations[index] = new_value
        
        if new_locations is not None:

            new_score = simulate_strategy(new_locations)
            if new_score < last_score:
                print("new score", new_score)
                last_score = new_score
                last_locations = new_locations
                iterations_since_change = 0

            else:
                iterations_since_change += 1
    
    return last_locations, last_score


def get_random_operation():
    val = random.random()

    if val < 0.10:
        return Operation.REMOVE

    if val < 0.20:
        return Operation.ADD
    
    elif val <= 0.60:
        return Operation.MOVE_UP
    
    return Operation.MOVE_DOWN


if __name__ == "__main__":
    start = time.time()
    print(genetic_search())
    end = time.time()
    print("Time:", end-start)
