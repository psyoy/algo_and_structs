"""
    Модуль linked_list реализует односвязный список
"""
from typing import Any

class Node:
    """
    Класс для реализации узла односвязного списка
    """
    def __init__(self, value: Any) -> None:
        self._value = value
        self.next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Any):
        self._value = value



class LinkedList:
    """
    Класс, реализующий односвязный список
    """
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._nodes_counter = 0
        self._current = None

    def __len__(self) -> int:
        """
        Магический метод, который возвращает длину связного списка
        :return int: возвращает длину списка
        """
        return self._nodes_counter

    def __str__(self) -> str:
        """
        Магический метод для представления связного списка в строковом виде,
        например, для функции print()

        :return str: возвращает строковое представление
        """
        nodes = []
        node = self._head
        while node:
            nodes.append(str(node.value))
            node = node.next
        return "[" + " -> ".join(nodes) + "]" if nodes else "[]"

    def __getitem__(self, index: int) -> Any:
        """
        Магический метод
        :param index: индекс, по которому нужно найти элемент списка
        :return int: возвращает значение узла
        """
        return self.find_by_index(index)

    def __setitem__(self, key: int, value: Any) -> None:
        """
        Магический метод, который устанавливает значение узла по его индексу

        :param key: ключ
        :param value: значение

        :return None:
        """
        if key < 0:
            key += len(self)
        if key < 0 or key >= self._nodes_counter:
            raise IndexError('index out of range')

        temp = self._head
        for _ in range(key):
            temp = temp.next

        temp.value = value

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next
        return value

    def prepend(self, value: Any) -> None:
        """
        Метод, который принимает значение, создает узел с этим значение
        и добавляет узел в начало списка
        :param value: значение

        :return None:
        """
        node = Node(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._nodes_counter += 1

    def append(self, value: Any) -> None:
        """
        Метод, который создает узел по значению и
        добавляет узел в конец связного списка
        :param value: значение
        :return None:
        """
        node = Node(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._nodes_counter += 1

    def insert(self, index: int, value: Any) -> None:
        """
        Вставляет в связный список узел по индексу
        :param index: индекс
        :param value: значение

        :return None:
        """
        if index < 0 or index > self._nodes_counter:
            raise IndexError("index out of range")

        if index == 0:
            self.prepend(value)
            return
        if index == self._nodes_counter:
            self.append(value)
            return

        prev = self._head
        for _ in range(index - 1):
            prev = prev.next

        node = Node(value)
        node.next = prev.next
        prev.next = node
        self._nodes_counter += 1

    def pop(self) -> Any:
        """
        Метод, который извлекает(удаляет) последний узел связного списка
        и возвращает значение его атрибута value
        """
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

    def pop_front(self) -> Any:
        """
        Метод, который извлекает(удаляет) первый узел связного списка
        и возвращает значение его атрибута value
        """

        if self._nodes_counter == 0:
            raise IndexError("pop from empty list")

        value = self._head.value
        self._head = self._head.next
        self._nodes_counter -= 1

        if self._nodes_counter == 0:
            self._tail = None

        return value

    def find_by_index(self, index: int) -> Any:
        """
        Метод, который находит по индексу узел связного списка
        и возвращает значение его атрибута value

        :param index: индекс для поиска
        """

        if index < 0:
            index += len(self)
        if index < 0 or index >= self._nodes_counter:
            raise IndexError('index out of range')

        temp = self._head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def remove(self, index: int) -> None:
        """
        Удаляет узел по индексу
        :param index:
        :raise IndexError:
        :return None:
        """
        if index < 0 or index >= self._nodes_counter:
            raise IndexError('index out of range')

        if index == 0:
            self.pop_front()
            return

        temp = self._head
        for _ in range(index - 1):
            temp = temp.next

        temp.next = temp.next.next

        if temp.next is None:
            self._tail = temp

        self._nodes_counter -= 1

    def clear(self) -> None:
        """
        Метод очищает список от узлов

        :return None:
        """
        self._head = self._tail = None
        self._nodes_counter = 0

if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.prepend(0)
    l.insert(3, 3)
    l.insert(0, -1)
    l.insert(2, 0.5)

    l[0] = 1000

    print(l.find_by_index(0))


    print(l)
    print(l.pop())  # 3
    print(l.pop_front())
    print(l[-1])
    print(len(l))

    print(l)
    l.remove(1)
    print(l)

    l.clear()
    print(l)