def longest_subsequence_length(string):
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


def longest_subsequence(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    prev = [0] * 6
    cur = [0] * 6
    for i in range(len(string)):
        char = string[i]
        for j in range(5):
            if char == vowels[j]:
                cur[j+1] = max(prev[j], prev[j+1]) + 1
            else:
                cur[j+1] = prev[j+1]
        prev = cur
    print(f"Longest Ordered Vowel Subsequnce is: {cur[-1]}")


if __name__ == "__main__":
    s = input().strip()
    longest_subsequence_length(s)
    longest_subsequence(s)