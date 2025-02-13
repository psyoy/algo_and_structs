class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class LinkedList:
    """
    Класс, реализующий односвязный список
    """
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
        return "[" + " -> ".join(nodes) + "]"

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if index >= self._nodes_counter:
            raise IndexError('index out of range')

        temp = self._head

        for ind in range(index):
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

        self._nodes_counter += 1

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            temp = self._head
            self._head = node
            self._head.next = temp

    def append(self, value):
        node = Node(value)

        self._nodes_counter += 1

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            temp = self._tail
            temp.next = node
            self._tail = node

    def insert(self, index, value):
        if index < 0 or index > self._nodes_counter:
            raise IndexError("index out of range")

        if index == self._nodes_counter:
            self.append(value)

        node = Node(value)

        self._nodes_counter += 1

        temp = self._head

        if index == 0:
            node.next = temp
            self._head = node
            return

        for ind in range(index - 1):
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def pop(self):
        if self._nodes_counter == 0:
            raise IndexError

        self._nodes_counter -= 1

        if self._head == self._tail:
            value = self._tail.value
            self._head = self._tail = None
            return value

        temp = self._head

        while temp != self._tail:
            temp = temp.next

        value = self._tail.value
        self._tail = temp
        self._tail.next = None

        return value

    def pop_front(self):
        if self._nodes_counter == 0:
            raise IndexError
        else:
            self._nodes_counter -= 1
            result = self._head
            self._head = self._head.next

            return result.value


if __name__ == "__main__":
    l = LinkedList()

    l.append(74)
    l.append(30)
    l.append(111)
    l.append(112)
    l.prepend(0)
    l.insert(0, 1000000)

    a = l.pop()
    print("popped", a)

    b = l.pop_front()
    print("popped front", b)

    for n in l:
        print(n)

    print(f'last item = {l[-1]}')

    print(f'Length = {len(l)}')

    print(l)