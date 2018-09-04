# Drone Flight Planner
#
# create a function calc_drone_min_energy that computes and returns the
# mininimal amount of energy the drone would need to complete its route.
# Assume that the drone starts its flight at the first point in route.

# Constraints
# input -> array.array.integer (1 <= route.length <= 100)
# output -> integer

# input -> [[1,2,3],[4,5,6],[7,8,9]]
# calDroneMinEnergy(input) -> 6

# input -> [[1,2,6],[3,4,3],[2,4,1]]
# calDonreMinEnergy(input) -> 0

# known
#  - ascending -> 1kwh
#  - descending -> -1kwh
#  z point is the point that matters

# calc_drone_min_energy(example_input) = 6
# calc_drone_min_energy(input2) = 0

import sys

def calc_drone_min_energy(path):
    z_1 = path[0][2]

    max_height = get_max_height(path)

    min_energy_required = max_height - z_1

    return min_energy_required

def get_max_height(path):
    max_value = -sys.maxint - 1

    for point in path:
        if max_value < point[2]:
            max_value = point[2]

    return max_value


