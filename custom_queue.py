
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(data)
            return
        self.tail.next_node = Node(data)
        self.tail = self.tail.next_node
        return

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed
