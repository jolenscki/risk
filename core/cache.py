from collections import defaultdict


class Cache:
    def __init__(self):
        self._store = defaultdict(dict)

    def get(self, namespace, key):
        return self._store[namespace].get(key)

    def set(self, namespace, key, value):
        self._store[namespace][key] = value

    def clear_namespace(self, namespace):
        self._store[namespace].clear()


GLOBAL_CACHE = Cache()