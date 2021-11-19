class LinkedList:
    head = None

    class Node:
        def __init__(self, element, next_node=None):
            self.element = element 
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element=element)
            return
        
        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element=element)

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
    
        print(node.element)

    def insert(self, element, index):
        i = 0
        node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        new_node = self.Node(element=element)
        new_node.next_node = node
        prev_node.next_node = new_node

    def search(self, element):
        i = 0
        c = 0
        node = self.head

        while node.next_node:
            node = node.next_node
            i += 1
        i += 1
        node = self.head

        while c < i:
            if node.element == element:
                print(node.element)
                return
            node = node.next_node
            c += 1
    
    def delete(self, element):
        node = self.head
        index = 0

        if self.head.element == element:
            self.head = node.next_node
            return

        while node.next_node:
            if node.element == element:
                break
            index += 1
            node = node.next_node
        print('index', index)
        node = self.head

        i = 0
        prev_node = None
        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        prev_node.next_node = node.next_node
        

link_list = LinkedList()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.insert(element=4, index=1)
link_list.insert(element=4, index=3)
link_list.out()
