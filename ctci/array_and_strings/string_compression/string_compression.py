def compress_string(letters):
    compressed_str = ''
    current_cnt = 1
    current_char = letters[0]
    letters_arr = [x for x in letters]
    letters_size = len(letters_arr)
    print("size of arr: " + str(letters_size))

    if (letters_size == 1):
        return letters

    for i in range(1, letters_size):
        if (current_char == letters_arr[i]):
            current_cnt += 1

        if (i == letters_size - 1 and current_cnt == 1):
            compressed_str += current_char
            break
        elif (i == letters_size - 1 and current_cnt > 1):
            compressed_str += current_char + str(current_cnt)
            break

        if (current_char != letters_arr[i] and current_cnt == 1):
            compressed_str += current_char

            current_char = letters_arr[i]
            current_cnt = 1

        elif (current_char != letters_arr[i] and current_cnt > 1):
            compressed_str += current_char + str(current_cnt)

            current_char = letters_arr[i]
            current_cnt = 1

    print('compressed_str' + compressed_str)
    if (len(compressed_str) == letters_size):
        return letters
    else:
        return compressed_str


