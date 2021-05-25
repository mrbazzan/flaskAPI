
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, data_, node):
        if data_["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data_)
            else:
                self._insert_recursive(data_, node.left)
        elif data_["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data_)
            else:
                self._insert_recursive(data_, node.right)
        else:
            return  # binary search tree already has value and it doesn't support duplicates.

    def insert(self, data_):
        if self.root is None:
            self.root = Node(data_)
        else:
            self._insert_recursive(data_, self.root)  # only be used by insert method(the `_` in front)

    def _search_recursive(self, id, node):
        if id == node.data['id']:
            return node.data

        if node.left is None and node.right is None:
            return False

        if id < node.data['id']:
            # check the left node
            return self._search_recursive(id, node.left)
        else:
            return self._search_recursive(id, node.right)

    def search(self, id):
        id = int(id)
        if self.root is None:
            return False

        return self._search_recursive(id, self.root)

    def _recursive_tree(self, node):
        the_list = (node.left, node.right)
        if the_list == (None, None):
            return
        else:
            print('Node: ', node.data)
            print(' Sub-node:', list(map(lambda x: x.data if x is not None else x, the_list)))
            for each_node in the_list:
                if each_node:
                    self._recursive_tree(each_node)

    def print_tree(self):
        if self.root is None:
            print(None)
        else:
            node = self.root
            self._recursive_tree(node)
