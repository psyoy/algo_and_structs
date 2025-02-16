from typing import List

def binary_search(unsorted_list: List[int], target: int, left: int = 0, right: int = 0) -> int:
    middle = unsorted_list[len(unsorted_list) // 2]

    if middle == target:
        return 0

    return 1


if __name__ == "__main__":
    a = [3, 1, 5, 4, 23]
    a.sort()
    binary_search(a, 5)
