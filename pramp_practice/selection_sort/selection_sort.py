# Selection Sort
#  - create selection sort. The method only accepts basic data types.
#

def selection_sort(e):
    size = len(e)
    print(','.join([str(x) for x in e]))

    if type(e) != list:
        raise TypeError

    if size == 0:
        return []

    for i in range(size - 1):
        index = i
        for j in range(i, size - 1):
            if type(e[index]) not in [str, bool, float, int] or type(e[j]) not in [str, bool, float, int]:
                raise ValueError

            if e[index] > e[j]:
                index = j

        if index != i:
            swap(e,i,index)
        print(','.join([str(x) for x in e]))

    return e

def swap(e,j,k):
    temp = e[k]
    e[k] = e[j]
    e[j] = temp


if __name__ == '__main__':
    selection_sort([4,2,1,2,5])
