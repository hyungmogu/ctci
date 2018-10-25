# Bubble Sort
#  - Create Bubble sort. The sorting algorithm only accepts basic data types
#
#

def bubble_sort(e):
    size = len(e)

    if type(e) != list:
        raise TypeError

    print(','.join([str(x) for x in e]))
    for i in range(size - 1):
        for j in range(size -1 - i):
            if j+1 >= size:
                continue

            if type(e[j]) not in [str, int, bool, float] or type(e[j+1]) not in [str, int, bool, float]:
                raise ValueError

            if e[j] > e[j+1]:
                swap(e,j,j+1)

        print(','.join([str(x) for x in e]))

    return e

def swap(e, j, jp1):
    temp = e[j]
    e[j] = e[jp1]
    e[jp1] = temp


if __name__ == '__main__':
    bubble_sort([4,2,1])




