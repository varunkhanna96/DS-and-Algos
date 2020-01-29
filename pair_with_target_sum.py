"""
To find unique pairs with target sum
"""
from itertools import combinations


def find_pairs(numbers, target):
    """
    O(n) solution for finding unique pairs with target sum
    :param numbers:
    :param target:
    :return:
    """
    result, comp = set(), set()
    for number in numbers:
        temp_comp = target - number
        if temp_comp in comp:
            res = (number, temp_comp) if number > temp_comp else (temp_comp, number)
            result.add(res)
        comp.add(number)
    print(result)


def find_pairs_using_combinations(numbers, target):
    """
    solution using python class combination.
    :param numbers:
    :param target:
    :return:
    """
    comb = combinations(numbers, 2)
    result = set()
    for i, j in comb:
        if i+j == target:
            result.add((i, j))
    print(result)


if __name__ == "__main__":
    nums = [1, 1, 2, 45, 46, 46]
    target = 47

    find_pairs(nums, target)
    find_pairs_using_combinations(nums, target)