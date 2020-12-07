def sort_select(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

if __name__ == '__main__':
    x1 = [4, 2, 1, 5, 7, 3, 9, 6, 8]
    x2 = [2, 1, 3, 1, 2, 3, 4]
    out1 = sort_select(x1)
    out2 = sort_select(x2)
    print(out1)
    print(out2)