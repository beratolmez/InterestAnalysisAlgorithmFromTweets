class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=256000):
        self.size = size
        self.hashmap = [None] * self.size

    def _hash_func(self, key):
        return hash(key) % self.size

    def __iter__(self):
        for item in self.hashmap:
            node = item
            while node:
                yield node.key
                node = node.next


    def set(self, key, value):
        index = self._hash_func(key)
        if self.hashmap[index] is None:
            self.hashmap[index] = Node(key, value)
        else:
            node = self.hashmap[index]
            while node.next:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)

    def get(self, key):
        index = self._hash_func(key)
        node = self.hashmap[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError('Key does not exist.')

    def delete(self, key):
        index = self._hash_func(key)
        node = self.hashmap[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.hashmap[index] = node.next
                return
            prev = node
            node = node.next
        raise KeyError('Key does not exist.')

    def __getitem__(self, key):
        try:
            return self.get(key)
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def items(self):
        items_list = []
        for item in self.hashmap:
            node = item
            while node:
                items_list.append((node.key, node.value))
                node = node.next
        return items_list

    def __len__(self):
        count = 0
        for item in self.hashmap:
            node = item
            while node:
                count += 1
                node = node.next
        return count