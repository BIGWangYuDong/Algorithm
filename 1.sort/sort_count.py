def sort_count(array):
    n = len(array)
    num = max(array)
    count = [0] * (num+1)
    for i in range(n):
        count[array[i]] += 1
    arr = []
    for i in range(num+1):
        for j in range(count[i]):
            arr.append(i)
    return arr


if __name__ == '__main__':
    x1 = [4, 2, 1, 5, 7, 3, 9, 6, 8]
    x2 = [2, 1, 3, 1, 2, 3, 4]
    out1 = sort_count(x1)
    out2 = sort_count(x2)
    print(out1)
    print(out2)