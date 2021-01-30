class Hash:
    def __init__(self):
        self.table = [None] * 255

    def hash_function(self, value, size):
        res = 0
        for i, letter in enumerate(value):
            res += ord(letter) * i
        return res % size

    def add(self, value):
        self.table[self.hash_function(value, 255)] = value

    def check(self, value):
        return bool(self.table[self.hash_function(value, 255)])