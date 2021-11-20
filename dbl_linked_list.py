class DBLLinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, element, next_node=None, prev_node=None):
            self.element = element
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return

        node = self.head
        while node.next_node:
            node = node.next_node

        new_node = self.Node(element)
        node.next_node = new_node
        new_node.prev_node = node

    def search(self, element):
        i = 0
        node = self.head

        while node.next_node:
            if node.element == element:
                print(f'Index of element {element}: is {i}')
                break
            node = node.next_node
            i += 1
        if node.element == element:
            print(f'Index of element {element}: is {i}')
            return

    def out(self):
        node = self.head

        if node != None:
            while node.next_node:
                print(node.element)
                node = node.next_node
            print(node.element)
        else:
            print('List is empty')

    def insert(self, element, index):
        node = self.head

        if index == 0:
            new_node = self.Node(element)
            new_node.next_node = node
            self.head = new_node
            node.prev_node = self.head
            return

        i = 0
        while i < index:
            if node.next_node is None and i == index - 1:
                new_node = self.Node(element=element)
                node.next_node = new_node
                new_node.prev_node = node
                return
            node = node.next_node
            i += 1

        new_node = self.Node(element=element)
        new_node.prev_node = node.prev_node
        new_node.next_node = node
        node.prev_node.next_node = new_node
        node.prev_node = new_node

    def delete(self, element):
        node = self.head

        index = 0
        while node.next_node:
            if node.element == element:
                break
            node = node.next_node
            index += 1

        if self.head.next_node is None and index == 0:
            self.head = None
            return
        elif index == 0:
            self.head.next_node.prev_node = None
            self.head = self.head.next_node
            return

        if node.next_node is None:
            node.prev_node.next_node = None
            node.prev_node = None
            return
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        del node