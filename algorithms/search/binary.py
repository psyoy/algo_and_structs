from typing import List

def binary_search(sorted_list: List[int], target: int, left: int = 0, right: int = None) -> int:
    """
    Рекурсивная реализация бинарного поиска.

    :param sorted_list: Отсортированный список целых чисел.
    :param target: Искомое значение.
    :param left: Левая граница диапазона поиска (по умолчанию 0).
    :param right: Правая граница диапазона поиска (по умолчанию len(sorted_list) - 1).

    :return: Индекс элемента, если найден; иначе -1.
    """

    if right is None:
        right = len(sorted_list) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if sorted_list[mid] == target:
        return mid

    elif sorted_list[mid] < target:
        return binary_search(sorted_list, target, left=mid + 1, right=right)

    else:
        return binary_search(sorted_list, target, left=left, right=mid - 1)
