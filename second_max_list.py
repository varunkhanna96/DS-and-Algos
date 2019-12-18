import sys


def sec_max(arr):
    first = second = -sys.maxsize - 1
    for obj in arr:
        if obj > first:
            second = first
            first = obj
    print(second)


if __name__ == '__main__':
    """program to find n max repeated occurence of an array"""
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    sec_max(arr)