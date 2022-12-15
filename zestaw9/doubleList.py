class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node  # stary head
            self.head = node  # nowy head
        else:  # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node  # stary tail
            self.tail = node  # nowy tail
        else:  # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):  # zwraca node
        if self.head is None:
            raise ValueError("pusta lista")
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None  # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):  # zwraca node
        if self.head is None:
            raise ValueError("pusta lista")
        elif self.head is self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None  # czyszczenie
            self.length -= 1
            return node

    """Zwraca łącze do węzła z największym kluczem."""
    def find_max(self):
        if self.is_empty():
            return None
        current = self.head
        max_node = current
        while current.next is not None:
            current = current.next
            if current.data > max_node.data:
                max_node = current
        return max_node

    """Zwraca łącze do węzła z najmniejszym kluczem."""
    def find_min(self):
        current = self.head
        min_node = current
        while current.next is not None:
            current = current.next
            if current.data < min_node.data:
                min_node = current
        return min_node

    """Usuwa wskazany węzeł z listy"""
    def remove(self, node):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.data == node.data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == node.data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == node.data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.length -= 1

    """czyszczenie listy"""
    def clear(self):
        current = self.tail
        self.tail = None
        while current.prev is not None:
            current = current.prev

            current.next.data = None
            current.next.prev = None
            current.next = None

        self.head.data = None
        self.head = None

    def show(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

