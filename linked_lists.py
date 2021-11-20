class LinkedList:
    def __init__(self):
        self.head = None

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
            self.head = self.Node(element=element)
            return
        
        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element=element)

    def out(self): # Выводим весь список
        node = self.head

        if self.head != None:
            while node.next_node:
                print(node.element)
                node = node.next_node
            print(node.element)
        else:
            print('List is empty')

    def insert(self, element, index):
        """
        Изменяем элемент по конкретному индексу
        :param element: новый элемент который будет вставлен
        :param index: индекс нового элемента
        """
        i = 0
        node = self.head

        # если индекс элемента = 0 делаем его первым в списке
        if index == 0:
            new_node = self.Node(element)
            new_node.next_node = node
            self.head = new_node
            return

        while i < index:
            prev_node = node # запоминаем прошлый узел
            node = node.next_node
            i += 1

        new_node = self.Node(element=element)
        new_node.next_node = node
        prev_node.next_node = new_node

    def search(self, element):
        """
        Находим элемент по значению и выводим вместе с соотвествующим индексом
        :param element: элемент для поиска
        """
        i = 0
        node = self.head

        try:
            while node.next_node:
                if node.element == element:
                    print(f'Index of element {element}: is {i}')
                    return
                node = node.next_node
                i += 1
            if node.element == element:
                print(f'Index of element {element}: is {i}')
                return
        except:
            print(f'Element {element} not in list')
    
    def delete(self, element):
        """
        удаляем элемент из списка и из памяти
        :param element: элемент для удаления
        """
        node = self.head

        if self.head.element == element:
            self.head = node.next_node
            return

        while node.next_node:
            if node.element != element:
                prev_node = node
            node = node.next_node
        prev_node.next_node = node.next_node
        del node