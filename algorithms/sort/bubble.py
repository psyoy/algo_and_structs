from typing import List

def bubble_sort(unsorted_list: List[int]) -> List[int]:

    unsorted_list = unsorted_list[:]
    n = len(unsorted_list)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        if not swapped:
            break

    return unsorted_list