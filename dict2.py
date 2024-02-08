class Dict2:
    def __init__(self):
        self.keys = []
        self.values = []

    def __setitem__(self, key, value):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            idx = self.keys.index(key)
            self.values[idx] = value

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError(f"Key '{key}' not found")
        else:
            idx = self.keys.index(key)
            return self.values[idx]

    def __iter__(self):
        return iter(self.keys)
