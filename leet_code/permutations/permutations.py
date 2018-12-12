
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    def permute(self, nums):

        output = []
        temp_arr = ['.' for x in range(len(nums))]

        if len(nums) == 0 or len(nums) == 1:
            return [nums]

        self.backtrack(0, nums, temp_arr, output)

        return output


    def backtrack(self, idx, nums, temp_arr, output):
        # 1. if terminating case is reached, then append temp_arr to output and return false
        if idx == len(nums):
            output.append(temp_arr[:])
            return False

        # 2. recursive case
        # 2.1 for each num in nums, check to see if placement is valid
        # 2.2 if not valid, then continue
        # 2.3 if valid, temp_arr[idx] = num
        # 2.4 backtrack(idx+1, nums, temp_arr, output)
        # 2.5 temp_arr[idx] = '.'
        for num in nums:
            if not self.placement_is_valid(num, temp_arr):
                continue

            temp_arr[idx] = num
            self.backtrack(idx+1, nums, temp_arr, output)
            temp_arr[idx] = '.'

        return False

    def placement_is_valid(self, num, temp_arr):
        if num in set(temp_arr):
            return False
        return True