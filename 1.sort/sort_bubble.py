def bubble_sort(array):
    n = len(array) 
    for i in range(n):
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

if __name__ == '__main__':
    x1 = [4, 2, 1, 5, 7, 3, 9, 6, 8]
    x2 = [2, 1, 3, 1, 2, 3, 4]
    out1 = bubble_sort(x1)
    out2 = bubble_sort(x2)
    print(out1)
    print(out2)
