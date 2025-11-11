from collections import Counter
from typing import Dict


def make_huffman_codes(s: str) -> Dict:
    return {c: c for c in Counter(s).keys()}


def main():
    s = input()
    codes = make_huffman_codes(s)
    encoded_string = "".join([codes[char] for char in s])
    print(len(codes), len(encoded_string))
    for char in sorted(codes):
        print(f"{char}: {codes[char]}")


if __name__ == "__main__":
    main()
