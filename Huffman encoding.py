import timeit
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def print_codes(root, current_code):
    if root == None:
        return

    if root.left == None and root.right == None:
        print(f"{root.char} : {current_code}")
    else:
        print_codes(root.left, current_code + "0")
        print_codes(root.right, current_code + "1")


def huffman_encoding(data):
    root = None
    heap = []
    total_size = sum(data.values())

    for key in data:
        node = Node(key, data[key])
        heapq.heappush(heap, node)

    while len(heap) != 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    root = heapq.heappop(heap)
    print("Huffman Codes:")
    print_codes(root, "")


def main():
    data = {}
    n = int(input("Enter number of characters: "))

    for i in range(n):
        char = input(f"Enter character {i+1}: ")
        freq = int(input(f"Enter frequency of character {char}: "))
        data[char] = freq

    start_time = timeit.default_timer()
    huffman_encoding(data)
    end_time = timeit.default_timer()

    print(f"\nTotal execution time: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()