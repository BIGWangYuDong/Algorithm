def sort_insert(array):
    n = len(array)
    for i in range(1, n):
        cur = array[i]
        j = i
        while j > 0 and array[j-1] > cur:
            array[j] = array[j-1]
            j -= 1
        array[j] = cur
    return array

if __name__ == '__main__':
    x1 = [4, 2, 1, 5, 7, 3, 9, 6, 8]
    x2 = [2, 1, 3, 1, 2, 3, 4]
    out1 = sort_insert(x1)
    out2 = sort_insert(x2)
    print(out1)
    print(out2)