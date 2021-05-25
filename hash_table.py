
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
            hash_value = (hash_value * ord(char)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:  # there is a collision
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
        return None

    def print_table(self):
        table_ = "{\n"
        for key, value in enumerate(self.hash_table):
            if value is not None:
                inner_node = ""
                node = value
                while node:
                    inner_node += f"({node.data.key} : {node.data.value}) --> "
                    node = node.next_node
                inner_node += 'None'
                table_ += f"    [{key}] {inner_node}\n"
            else:
                table_ += f"    [{key}] {value}\n"
        print(table_ + '}')


# table = HashTable(4)
# table.add_key_value('hi', 'there')
# table.add_key_value('hi', '@mr_baz')
# table.add_key_value('4', 'okay sir!')
# table.print_table()
# print(table.get_value('hi'))
