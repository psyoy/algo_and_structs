class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._nodes_counter = 0
        self._current = None

    def __len__(self):
        return self._nodes_counter

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
        return LinkedListIterator(self._head)

    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current.value

        self.__current = self._current.next

        return value

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

if __name__ == "__main__":
    l = LinkedList()

    l.append(74)
    l.append(30)
    l.append(111)
    l.append(112)

    for node in l:
        print(node)

    print(f'index 0 = {l[-2]}')

    print(f'Length = {len(l)}')
