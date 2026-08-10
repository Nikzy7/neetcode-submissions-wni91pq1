class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        value_to_return = self.cache.get(key, -1)

        if value_to_return == -1:
            return value_to_return

        self.cache.move_to_end(key)

        return value_to_return

    def put(self, key: int, value: int) -> None:
        key_already_present = key in self.cache
        if len(self.cache) == self.size and not key_already_present:
            self.cache.popitem(last=False)
        if key_already_present:
            self.cache.move_to_end(key)
        self.cache[key] = value
