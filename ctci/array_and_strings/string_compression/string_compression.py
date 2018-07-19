def compress_string(letters):
    compressed_str = ''
    current_cnt = 1
    letters_arr = [x for x in letters]
    current_char = letters_arr[0]
    letters_size = len(letters_arr)

    # Edge case where letter size is 1
    if (letters_size == 1):
        return letters

    if (letters_size == 2):
        if (current_char == letters_arr[letters_size-1]):
            current_cnt += 1
            compressed_str += current_char + str(current_cnt)
        else:
            compressed_str += current_char + letters_arr[letters_size-1]

    if (letters_size > 2):
        # Edge case where letter size is not 1
        for i in range(1, letters_size):
            # case where i is greater than 0
            # case where the ith letter is equal to current char
            if (current_char == letters_arr[i]):
                current_cnt += 1
                continue

            # case where the ith letter is not equal to current char
            if (current_char != letters_arr[i] and current_cnt == 1):
                compressed_str += current_char

            elif (current_char != letters_arr[i] and current_cnt > 1):
                compressed_str += current_char + str(current_cnt)

            current_char = letters_arr[i]
            current_cnt = 1

        # address the last letter in string
        if (current_cnt > 1):
            compressed_str += current_char + str(current_cnt)
        else:
            compressed_str += current_char

    if (len(compressed_str) == letters_size):
        return letters
    else:
        return compressed_str


