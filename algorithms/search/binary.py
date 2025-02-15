from typing import List

def binary_search(unsorted_list: List[int], target: int) -> List[int]:

    middle = unsorted_list[len(unsorted_list) // 2]
    print(middle)

if __name__ == "__main__":
    a = [3, 1, 4, 5, 23]
    binary_search(a, 5)
