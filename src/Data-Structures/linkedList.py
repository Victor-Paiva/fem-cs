class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        rep = ''
        current_node = self.head
        while current_node is not None:
            rep += '{} -> '.format(current_node.value)
            current_node = current_node.next
        rep += 'None'

        return rep

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def pop(self):
        if self.length == 1:
            res = self.head.value
            self.__init__()
        else:
            current_node = self.head
            while True:
                if current_node.next is self.tail:
                    current_node.next = None
                    res = self.tail.value
                    self.tail = current_node
                    break

                current_node = current_node.next

        return res

    def get(self, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        
        return current_node.value

    def delete(self, index):
        if index == 0:
            if self.length == 1:
                self.__init__()
            else:
                self.head = self.head.next
            return

        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next

        current_node.next = current_node.next.next