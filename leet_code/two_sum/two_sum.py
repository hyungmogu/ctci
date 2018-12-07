# Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# input: nums = [2, 7, 11, 15], target = 9,
# output: [0,1] Because nums[0] + nums[1] = 2 + 7 = 9,
#
# =========================================================

def two_sum(arr,target):
    if len(arr) == 0 or len(arr) == 1:
        return []

    for idx_i, arr_i in enumerate(arr):
        temp_dict = get_temp_dict(arr)
        arr_j = target - arr_i

        if arr_j == arr_i:
            continue

        if arr_j in temp_dict:
            idx_j = temp_dict[arr_j]
            return [idx_i,idx_j]

    return []

def get_temp_dict(arr):
    output = {}
    for idx,value in enumerate(arr):
        output[value] = idx

    return output


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    target = 18
    print(two_sum(arr,target))

