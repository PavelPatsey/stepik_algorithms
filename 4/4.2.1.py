import heapq
from collections import Counter, namedtuple
from typing import Dict


class Node(namedtuple("Node", ["left", "right"])):
    def traverse(self, code: Dict, acc: str):
        self.left.traverse(code, acc + "0")
        self.right.traverse(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def traverse(self, code: Dict, acc: str):
        code[self.char] = acc or "0"


def make_huffman_codes(s: str) -> Dict:
    h = []
    for char, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(char)))
    heapq.heapify(h)
    counter = len(h)
    while len(h) > 1:
        freq1, _c1, left = heapq.heappop(h)
        freq2, _c2, right = heapq.heappop(h)
        new_tuple = freq1 + freq2, counter, Node(left, right)
        heapq.heappush(h, new_tuple)
        counter += 1

    freq, _c, root = heapq.heappop(h)
    codes = {}
    root.traverse(codes, "")
    return codes


def main():
    s = input()
    codes = make_huffman_codes(s)
    encoded_string = "".join([codes[char] for char in s])
    print(len(codes), len(encoded_string))
    for char in sorted(codes):
        print(f"{char}: {codes[char]}")
    print(encoded_string)


if __name__ == "__main__":
    main()

    import sys
    from io import StringIO

    print("test 1")
    input_data = "abacabad"
    sys.stdin = StringIO(input_data)
    main()
