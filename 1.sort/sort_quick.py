
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]                    # 左边为key
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def quick_sort_right(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[-1]                    # 右边为key
        less = [i for i in array[:-1] if i <= pivot]
        greater = [i for i in array[:-1] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    x1 = [4, 2, 1, 5, 7, 3, 9, 6, 8]
    x2 = [2, 1, 3, 1, 2, 3, 4]
    out = quick_sort(x1)
    out_right = quick_sort_right(x1)
    print(out)
    print(out_right)