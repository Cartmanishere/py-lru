class Node:
    def __init__(self, value, k=None):
        self.val = value
        self.left = None
        self.right = None
        self.key = k

    def __repr__(self):
        return f'({self.key + ":" if self.key else ""}{self.val})'



class DoublyLinkedList:
    def __init__(self):
        self.head = Node('HEAD')
        self.last = Node('LAST')
        self.head.right = self.last
        self.last.left = self.head
        self.count = 0

    def __iter__(self):
        node = self.head.right
        while node.right is not None:
            yield node.val
            node = node.right

    def __len__(self):
        return self.count

    def __repr__(self):
        s = ''
        n = self.head
        while n is not None:
            s += str(n) + '<-> '
            n = n.right
        return s

    def insert_left(self, value, k=None):
        n = Node(value, k=k)
        n.left = self.head
        t = self.head.right
        n.right = t
        self.head.right = n
        t.left = n
        self.count += 1

        return n

    def insert_right(self, value, k=None):
        n = Node(value, k=k)
        t = self.last.left
        t.right = n
        n.right = self.last
        n.left = t
        self.last.left = n
        self.count += 1
        return n

    def pop_left(self):
        t = self.head.right
        if t is not None and t.val != self.last.val:
            self.head.right = t.right
            t.right.left = self.head
            self.count -= 1
            return t

    def pop_right(self):
        t = self.last.left
        if t is not None and t.val != self.head.val:
            self.last.left = t.left
            t.left.right = self.last
            self.count -= 1
            return t

    def delete_node(self, node):
        r = node.right
        l = node.left
        if l is not None:
            l.right = r
        if r is not None:
            r.left = l
        self.count -= 1

    def delete(self, value):
        ptr = self.head
        while ptr.right is not None:
            if ptr.right.val == value:
                break
            ptr = ptr.right

        if ptr.right is not None:
            t = ptr.right
            ptr.right = t.right
            t.right.left = ptr
            self.count -= 1


class LRUCache:
    def __init__(self, max_slots):
        self.hash = {}
        self.dll = DoublyLinkedList()
        self.max_slots = max_slots

    def __repr__(self):
        return self.dll.__repr__()

    def __iter__(self):
        yield from self.dll.__iter__()

    def __setitem__(self, key, value):
        if self.dll.count >= self.max_slots:
            popped = self.dll.pop_left()
            del self.hash[popped.key]

        n = self.dll.insert_right(value, k=key)
        self.hash[key] = n
        return value

    def __getitem__(self, key):
        n = self.hash.get(key, None)
        if n is not None:
            self.dll.delete_node(n)
            new_n = self.dll.insert_right(n.val, k=key)
            self.hash[key] = new_n
            return n.val
        return None

    def __len__(self):
        return self.dll.__len__()
