class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._nodes_counter = 0
        self._current = None

    def __len__(self):
        return self._nodes_counter

    def __str__(self):
        nodes = []
        node = self._head
        while node:
            nodes.append(str(node.value))
            node = node.next
        return "[" + " -> ".join(nodes) + "]" if nodes else "[]"

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if index < 0 or index >= self._nodes_counter:
            raise IndexError('index out of range')

        temp = self._head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next
        return value

    def prepend(self, value):
        node = Node(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._nodes_counter += 1

    def append(self, value):
        node = Node(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._nodes_counter += 1

    def insert(self, index, value):
        if index < 0 or index > self._nodes_counter:
            raise IndexError("index out of range")

        if index == 0:
            return self.prepend(value)
        if index == self._nodes_counter:
            return self.append(value)

        prev = self._head
        for _ in range(index - 1):
            prev = prev.next

        node = Node(value)
        node.next = prev.next
        prev.next = node
        self._nodes_counter += 1

    def pop(self):
        if self._nodes_counter == 0:
            raise IndexError("pop from empty list")

        if self._head == self._tail:
            value = self._head.value
            self._head = self._tail = None
        else:
            prev = self._head
            while prev.next != self._tail:
                prev = prev.next
            value = self._tail.value
            prev.next = None
            self._tail = prev

        self._nodes_counter -= 1
        return value

    def pop_front(self):
        if self._nodes_counter == 0:
            raise IndexError("pop from empty list")

        value = self._head.value
        self._head = self._head.next
        self._nodes_counter -= 1

        if self._nodes_counter == 0:
            self._tail = None

        return value