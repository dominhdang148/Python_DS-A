from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.head
            self.head.next = new_node
            self.head = new_node
        self.count += 1

    def iter(self, reverse=False):
        if reverse == False:
            current = self.tail
            while current:
                val = current.data
                current = current.next
                yield val
        else:
            current = self.head
            while current:
                val = current.data
                current = current.previous
                yield val

    def delete(self, data):
        current = self.tail
        node_deleted = False
        if self.tail == None:
            node_deleted = False
        if self.tail.data == data:
            self.tail = current.next
            self.tail.previous = None
            node_deleted = True
        elif self.head.data == data:
            self.head = self.head.previous
            self.head.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1

    def contain(self, data):
        for item in self.iter():
            if item == data:
                return True
        return False