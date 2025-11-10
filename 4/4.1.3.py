def main():
    n = int(input())
    remainder = n
    res = []
    while True:
        pretender = res[-1] + 1 if res else 1
        a, b = pretender, remainder - pretender
        if a < b:
            res.append(a)
            remainder = b
        else:
            res.append(remainder)
            break
    print(len(res))
    print(*res)


if __name__ == "__main__":
    # main()

    import sys
    from io import StringIO

    print("test 1")
    input_data = """\
4
"""
    sys.stdin = StringIO(input_data)
    main()

    print("test 2")
    input_data = """\
6
"""
    sys.stdin = StringIO(input_data)
    main()

    print("test 3")
    input_data = """\
8
"""
    sys.stdin = StringIO(input_data)
    main()
