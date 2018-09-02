#
# array_chunking
#
#  given an array and chunk size, divide the array into many subarrays
#  where each subarray is of length size
#
# array_chunking([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
# array_chunking([1,2,3,4,5], 1) -> [[1],[2],[3],[4],[5]]
# array_chuncking("hello world", 2) -> Type Error
# array_chunking([1,2,3,4,5], 0.1) -> Type Error
# array_chunking([], 2) -> Value Error
# array_chunking([1,2,3,4,5], -1) -> Value Error

def array_chunking(arr, sub_arr_size):
    output = []

    if type(arr) != list:
        raise TypeError

    if type(sub_arr_size) != int:
        raise TypeError

    if len(arr) == 0:
        raise ValueError

    if sub_arr_size < 1:
        raise ValueError

    # enumerate([1,2,3,4,5]) -> [(0, 1), (1,2), (2,3)...]
    for idx, value in enumerate(arr):
        sub_arr = []
        if (idx + 1) % sub_arr_size > 0:
            sub_arr.append(value)

            if idx != len(arr) -1:
                continue

        output.append(sub_arr)

    return output