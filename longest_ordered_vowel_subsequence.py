def longest_subsequence(string):
    a, e, i, o, u = [0] * 5
    for char in string:
        if char == 'a':
            a += 1
        if char == 'e' and a > 0:
            e = max(a, e) + 1
        if char == 'i' and e > 0:
            i = max(e, i) + 1
        if char == 'o' and i > 0:
            o = max(i, o) + 1
        if char == 'u' and o > 0:
            u = max(o, u) + 1
    print(f"Longest Ordered Vowel Subsequnce is: {u}")


if __name__ == "__main__":
    s = input().strip()
    longest_subsequence(s)