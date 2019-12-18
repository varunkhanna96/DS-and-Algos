def find(arr, k):
    dict_obj = dict()

    for obj in arr:
        if obj in dict_obj:
            dict_obj[obj] += 1
        else:
            dict_obj[obj] = 1

    a = sorted(list(dict_obj.keys()), key=lambda x: dict_obj[x], reverse=True)
    print(a[0:k])


if __name__ == '__main__':
    """program to find n max repeated occurence of an array"""
    arr = [3, 1, 4, 4, 5, 2, 6, 1]
    find(arr, 2)