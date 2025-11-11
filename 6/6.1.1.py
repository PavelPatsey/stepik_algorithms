import sys


def input_data():
    data = [line for line in sys.stdin]
    array = [int(x) for x in data[0].split()]
    ks = [int(x) for x in data[1].split()]
    ks = [len(ks)] + ks
    return array, ks


def main():
    array, ks = input_data()
    print(array)
    print(ks)


if __name__ == "__main__":
    # main()

    from io import StringIO

    print("test 1")
    test_input_data = """\
5 1 5 8 12 13
5 8 1 23 1 11
"""
    sys.stdin = StringIO(test_input_data)
    main()
