class DBLLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, element, next_node=None, prev_node=None):
            self.element = element
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, element):
        if not self.head:
            self.head = self.tail = self.Node(element=element)
            self.head.next_node = self.tail
            self.head.prev_node = self.tail
            return

        node = self.head
        while node.next_node != self.head:
            node = node.next_node

        self.tail = self.Node(element=element)
        node.next_node = self.tail
        self.tail.prev_node = node
        self.tail.next_node = self.head
        self.head.prev_node = self.tail

    def insert_in_head(self, element):
        if self.head is None:
            self.append(element)
            return

        node = self.head
        self.head = self.Node(element=element)
        self.head.next_node = node
        node.prev_node = self.head
        self.tail.next_node = self.head
        self.head.prev_node = self.tail

    def insert(self, element, index):
        node = self.head
        if index == 0:
            self.insert_in_head(element)
            return

        i = 0
        while i < index:
            node = node.next_node
            i += 1

        if node is self.head:
            self.tail = self.Node(element)
            node.prev_node.next_node = self.tail
            self.tail.prev_node = node.prev_node
            self.tail.next_node = node
            node.prev_node = self.tail
            return

        new_node = self.Node(element=element)
        new_node.prev_node = node.prev_node
        new_node.next_node = node
        node.prev_node.next_node = new_node
        node.prev_node = new_node

    def search(self, element):
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

    def out(self):
        node = self.head
        if self.head != None:
            while node.next_node != self.head:
                print(f"Prev: {node.prev_node.element} | "
                      f"Current: {node.element} | "
                      f"Next: {node.next_node.element}")
                node = node.next_node
            print(f"Prev: {node.prev_node.element} | "
                  f"Current: {node.element} | "
                  f"Next: {node.next_node.element}")
        else:
            print('List is empty')

    def delete(self, element):
        if self.head.element == element:
            if self.head.next_node == self.head:
                self.head = None
                return
            self.head = self.head.next_node
            self.head.prev_node = self.tail
            self.tail.next_node = self.head
            return

        node = self.head
        while node.element != element:
            node = node.next_node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node
        del node