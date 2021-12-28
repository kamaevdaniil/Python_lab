from basecache import BaseCache


class Cache(BaseCache):
    values = {}

    def clean(self, key):
        del self.values[key]

    def refresh(self, key, value):
        self.clean(key)
        self.keep(key, value)

    def keep(self, key, value):
        self.values[key] = value

    def check(self, key):
        if key in self.values.keys():
            return True
        else:
            return False

    def get(self, key):
        return self.values[key]

    def set(self, key, value):
        self.values[key] = value