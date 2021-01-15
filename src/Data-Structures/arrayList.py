class ArrayList:
    def __init__(self):
        self.length = 0
        self.data = {}

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.data[index]

    def delete(self, index):
        self.collapse_to(index)
        self.length -= 1

    def collapse_to(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
