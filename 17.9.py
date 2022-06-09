list_input = input('Введите последовательность чисел через пробел').split()
a = list(map(int, list_input))


def sorting(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


list_num = sorting(a)
print(list_num)
num = int(input('Введите любое число'))


def binary_search(some_list, el, left, right):
    if left > right:
        return False

    mid = (right + left) // 2
    if some_list[mid] == el:
        return mid
    elif el < some_list[mid]:
        return binary_search(some_list, el, left, mid - 1)
    else:
        return binary_search(some_list, el, mid + 1, right)


list_num.append(num)
list_num_1 = sorting(list_num)
result = binary_search(list_num_1, num, 0, len(list_num_1))

if result >= 1:
    print('Позиция ближайшего меньшего числа: ', result - 1)
else:
    print('Введенное число является наименьшим')
