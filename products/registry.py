class ProductRegistry:
    _registry = {}

    @classmethod
    def get(cls, key: str):
        return cls._registry.get(key)

    @classmethod
    def register(cls, key: str, product):
        if key in cls._registry:
            return cls._registry[key]
        cls._registry[key] = product
        return product