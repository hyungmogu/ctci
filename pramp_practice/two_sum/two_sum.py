# Two Sum (brute force)
#
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# input
#   - array of integer
#   - integer
#
# constraint
#   - input would have exactly one solution
#   - same element cannot be used twice
#
# example
#   two_sum([2,1],3) --> [0,1]
#   two_sum([1,2,3,4,5],9) --> [3,4]
#   two_sum([1], 10) --> ValueError
#   two_sum([], 4) --> ValueError
#   two_sum("", 10) --> TypeError

def two_sum(arr, target):
    if (type(arr) != list) or (type(target) != int):
        raise TypeError

    if len(arr) <= 1:
        raise ValueError

    for idx in range(len(arr)):
        result = find_two_sum(arr, target, idx)
        if (result != None):
            return result

    return None

def find_two_sum(arr, target, idx_i):
    output = None

    # perform search algorithm to find the index of the matching coord
    # in near future, i will be replacing this with binary search method to bring the complexity down to O(nlogn)
    for idx_j in range(idx_i, len(arr)):
        # check to see if the sum of two is target
        if arr[idx_i] + arr[idx_j] == target:
        # if its target, then set output, and break
            output = [idx_i, idx_j]
            break
        # if index doesn't exist, then continue

    # if matching array does exist, then return output
    return output

# def sort_arr(arr):
    # for now, i will be using sorting algorithm of O(N^2) complexity.
    # but, in the future, i will be replacing this with quick sort / something of
    # better time complexity
    # list.sort(arr)