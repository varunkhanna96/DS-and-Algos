from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # using ordered dict to preserve order of least recently used cache

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def display(self):
        print(list(self.cache.values()))


if __name__ == "__main__":
    a = LRUCache(4)
    a.set(1, 1)
    a.set(2, 2)
    a.set(3, 3)
    a.get(1)
    a.set(4, 4)  # this will remove 2
    a.set(5, 5)
    a.set(3, 3)
    a.set(6, 6)  # this will remove 1
    a.display()
