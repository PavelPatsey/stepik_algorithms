def main():
    n = int(input())
    a = 1
    b = n - a
    res = []
    while a < b:
        res.append(a)
        a = a + 1
        b = b - a
    res.append(a + b)
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
