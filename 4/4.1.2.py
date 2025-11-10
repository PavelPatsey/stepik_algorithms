import sys
from typing import List


def get_input_data():
    data = (line for line in sys.stdin)
    n, weight = map(int, next(data).split())
    backpacks = [tuple(map(int, line.split())) for line in data]
    return n, weight, backpacks


def get_max_cost(max_weight: int, backpacks: List):
    sorted_packs = sorted(backpacks, key=lambda x: x[0] / x[1], reverse=True)
    cur_cost = 0
    cur_weight = 0
    i = 0
    while i < len(backpacks) and cur_weight <= max_weight:
        c, w = sorted_packs[i]
        delta = max_weight - cur_weight
        if delta > w:
            cur_cost += c
            cur_weight += w
        else:
            ro = c / w
            cur_cost += delta * ro
            cur_weight += delta
        i += 1
    return cur_cost


def main():
    n, max_weight, backpacks = get_input_data()
    max_cost = get_max_cost(max_weight, backpacks)
    print(f"{max_cost:.3f}")


if __name__ == "__main__":
    # main()

    from io import StringIO

    print("test 1")
    input_data = """\
3 50
60 20
100 50
120 30
"""
    sys.stdin = StringIO(input_data)
    main()
