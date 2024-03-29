class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        """
        Добавляем элемент в конец списка, аналогично встроенному методу append
        :param element: новый элемент который будет вставлен
        """
        if not self.head:
            self.head = self.tail = self.Node(element=element)
            self.tail.next_node = self.head
            return

        node = self.head
        while node.next_node != self.head:
            node = node.next_node

        self.tail = self.Node(element=element)
        node.next_node = self.tail
        self.tail.next_node = self.head

    def out(self):  # Выводим весь список
        node = self.head

        if self.head != None:
            while node.next_node != self.head:
                print(f"{node.element} | {node.next_node.element}")
                node = node.next_node
            print(f"{node.element} | {node.next_node.element}")
        else:
            print('List is empty')

    def insert_in_head(self, element):
        """
        Добавляем элемент в начало списка
        :param element: новый элемент который будет вставлен
        """
        node = self.head
        if not node:
            self.append(element=element)
            return

        new_node = self.Node(element=element)
        self.head = new_node
        self.head.next_node = node
        self.tail.next_node = self.head
        return

    def insert(self, element, index):
        """
        Изменяем элемент по конкретному индексу
        :param element: новый элемент который будет вставлен
        :param index: индекс нового элемента
        ПРИМЕЧАНИЕ:
        Связанный список не предоставляет доступ к элементу по индексу,
        данная реализация характерна только для массива.
        Поэтому данный метод было бы неправильно использовать в связанном списке
        """
        if index == 0:
            self.insert_in_head(element=element)
            return

        node = self.head
        i = 0
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        new_node = self.Node(element=element)
        prev_node.next_node = new_node
        new_node.next_node = node

    def search(self, element):
        """
        Находим элемент по значению и выводим вместе с соотвествующим индексом
        :param element: элемент для поиска
        """
        i = 0
        node = self.head
        try:
            while node.next_node != self.head:
                if node.element == element:
                    print(f'Index of element {element}: is {i}')
                    return
                node = node.next_node
                i += 1
            if node.element == element:
                print(f'Index of element {element}: is {i}')
                return
            raise
        except:
            print(f'Element {element} not in list')

    def delete(self, element):
        """
        удаляем элемент из списка и из памяти
        :param element: элемент для удаления
        """
        node = self.head
        if node.element == element:
            if node is self.tail:
                self.head = None
                return
            self.head = node.next_node
            self.tail.next_node = self.head
            del node
            return

        while node != self.tail:
            if node.element == element:
                break
            prev_node = node
            node = node.next_node
        prev_node.next_node = node.next_node
        del node