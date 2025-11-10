from operator import itemgetter
from typing import List


def get_input_data():
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    return n, segments


def segment_contains_point(point: int, segment: List[int]) -> bool:
    a, b = segment
    return a <= point <= b


def main():
    n, segments = get_input_data()
    segments = sorted(segments, key=itemgetter(1))
    res = []
    s = 0
    while s < len(segments):
        point = segments[s][1]
        res.append(point)
        while s < len(segments) and segment_contains_point(point, segments[s]):
            s += 1
    print(len(res))
    print(*res)


if __name__ == "__main__":
    main()

    import sys
    from io import StringIO

    print("test 1")
    input_data = """\
3
1 3
2 5
3 6
"""
    sys.stdin = StringIO(input_data)
    main()

    print("test 2")
    input_data = """\
4
4 7
1 3
2 5
5 6
    """
    sys.stdin = StringIO(input_data)
    main()
