# Binary Search Tree

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, verbose=False):
        self.root = None
        self.verbose = verbose

    def add(self, value, current=0):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root if current == 0 else current

        if self.verbose:
            print(current.value)

        if value <= current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.add(value, current=current.left)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.add(value, current=current.right)