class DBLLinkedList:
    head = None

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
                print(f'Index of element {element} is {i}')
                return
            node = node.next_node
            i += 1
        if node.element == element:
            print(f'Index of element {element} is {i}')
            return

        # while node.next_node:
        #     i += 1
        #     node = node.next_node
        # i += 1
        # node = self.head
        #
        # index = 0
        # while index < i:
        #     if node.element == element:
        #         print(f'Index of element {element} is {index}')
        #         return
        #     node = node.next_node
        #     index += 1

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
            node = node.next_node
            i += 1

        new_node = self.Node(element=element)
        new_node.prev_node = node.prev_node
        new_node.next_node = node
        node.prev_node.next_node = new_node
        node.prev_node = new_node

        # prev_node = node.prev_node

        # new_node = self.Node(element=element)
        # new_node.prev_node = node.prev_node
        # new_node.next_node = node
        # node.prev_node = new_node
        # prev_node.next_node = new_node

    def delete(self, element):
        node = self.head

        index = 0
        while node.next_node:
            if node.element == element:
                break
            node = node.next_node
            index += 1
        print('Index', index)

        if self.head.next_node is None and index == 0:
            self.head = None
            return
        elif index == 0:
            self.head.next_node.prev_node = None
            self.head = self.head.next_node

        i = 0
        while i < index:
            if node.next_node is None:
                node.prev_node.next_node = None
                node.prev_node = None
                break
            node.prev_node.next_node = node.next_node
            node.next_node.prev_node = node.prev_node
            i += 1


l = DBLLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(4)
l.insert(element=5, index=2)
l.insert(element=6, index=0)
# l.insert(element=6, index=3)
# l.insert(element=7, index=4)
# l.insert(element=8, index=5)
print('===========')
# l.search(element=4)
# print('===========')
l.out()
print('===========')
# l.delete(element=2)
# l.delete(element=5)
# l.delete(element=4)
# l.delete(element=4)
l.delete(element=6)
l.delete(element=1)
l.delete(element=2)
l.delete(element=4)
l.delete(element=4)
l.delete(element=5)
l.delete(element=3)
print('===========')
l.out()
