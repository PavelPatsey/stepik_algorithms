import sys
from typing import List


def input_data():
    data = (line for line in sys.stdin)
    array = [int(x) for x in next(data).split()]
    ks = [int(x) for x in next(data).split()]
    return array, ks


def binary_search(k: int, array: List[int]) -> int:
    l = 1
    r = len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] == k:
            return m
        if k < array[m]:
            r = m - 1
        elif k > array[m]:
            l = l + 1
    return -1


def main():
    array, ks = input_data()
    res = [binary_search(ks[i], array) for i in range(1, len(ks))]
    print(*res)


if __name__ == "__main__":
    main()

    assert binary_search(8, [5, 1, 5, 8, 12, 13]) == 3

    from io import StringIO

    print("test 1")
    test_input_data = """\
5 1 5 8 12 13
5 8 1 23 1 11
"""
    sys.stdin = StringIO(test_input_data)
    main()
