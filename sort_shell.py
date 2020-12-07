def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap >= 1:
        for i in range(gap,n):
            if array[i] < array[i-gap]:
                array[i], array[i-gap] = array[i-gap], array[i]
        gap = gap // 2
    return array


if __name__ == '__main__':
    x1 = [4, 2, 1, 5, 7, 3, 9, 6, 8]
    x2 = [2, 1, 3, 1, 2, 3, 4]
    out1 = shell_sort(x1)
    out2 = shell_sort(x2)
    print(out1)
    print(out2)