class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

    def update(self):
        if not self.right and not self.left:
            self.height = 1
        elif not self.right or (self.left and self.right.height < self.left.height):
            self.height = self.left.height + 1
        else:
            self.height = self.right.height + 1

    def rotateRR(self):
        value_before = self.value
        left_before = self.left
        self.value = self.right.value
        self.left = self.right
        self.right = self.right.right
        self.left.right = self.left.left
        self.left.left = left_before
        self.left.value = value_before
        self.left.update()
        self.update()

    def rotateLL(self):
        value_before = self.value
        right_before = self.right
        self.value = self.left.value
        self.right = self.left
        self.left = self.left.left
        self.right.left = self.right.right
        self.right.right = right_before
        self.right.value = value_before
        self.right.update()
        self.update()

    def balance(self):
        right_height = self.right.height if self.right is not None else 0
        left_height = self.left.height if self.left is not None else 0

        if left_height > right_height + 1:
            left_right_height = self.left.right.height if self.left.right is not None else 0
            left_left_height = self.left.left.height if self.left.left is not None else 0

            if left_right_height > left_left_height:
                self.left.rotateRR()
            self.rotateLL()

        elif right_height > left_height + 1:
            right_right_height = self.right.right.height if self.right.right is not None else 0
            right_left_height = self.right.left.height if self.right.left is not None else 0

            if right_left_height > right_right_height:
                self.right.rotateLL()
            self.rotateRR()

    def add(self, value):
        if value <= self.value:
            # Add the node
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.add(value)

            # Update the height
            if self.right is None or self.right.height < self.left.height:
                self.height = self.left.height + 1
        else:
            # Add the node
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.add(value)

            # Update the height
            if self.left is None or self.left.height < self.right.height:
                self.height = self.right.height + 1

        self.balance()

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)