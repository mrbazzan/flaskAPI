class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        the_list = []
        node = self.head
        while node is not None:
            the_list.append(node.data)
            node = node.next_node
        return the_list

    def get_user_by_id(self, id):
        node = self.head
        while node is not None:
            if node.data['id'] == id:
                return node.data
            node = node.next_node
        return None

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            node = Node(data, self.head)
            self.head = node

    def insert_at_end(self, data):

        if self.head is None:
            return self.insert_beginning(data)

        self.last_node.next_node = Node(data)
        self.last_node = self.last_node.next_node

    def __str__(self):
        ll_string = ''
        node = self.head
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node

        ll_string += "None"
        return ll_string
