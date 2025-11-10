def get_input_data():
    n, weight = map(int, input().split())
    backpacks = [list(map(int, input().split())) for _ in range(n)]
    return n, weight, backpacks


def main():
    n, max_weight, backpacks = get_input_data()
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
    print(f"{cur_cost:.3f}")


if __name__ == "__main__":
    # main()

    import sys
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
