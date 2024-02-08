class Dict2:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        if key not in self.data:
            raise KeyError(f"Key '{key}' not found")
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        return iter(self.data)
        
