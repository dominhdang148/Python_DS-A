from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
            return False

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.tail == None and self.head == None

    def insert_start(self, data):
        if self.isEmpty():
            self.append(data)
            return
        new_node = Node(data)
        new_node.next = self.tail
        self.tail = new_node
        self.size += 1

    def insert_after(self, data, previous_data):
        # Case 1: Không có node nào  trong danh sách
        if self.isEmpty():
            self.append(data)
            return
        current = self.tail
        while current:
            if current.data == previous_data:
                node = Node(data)
                # Case 3: previous node là node cuối --> append như thông thường
                if current == self.head:
                    self.append(data)
                else:
                # Case 4: previous node là node đầu hoặc giữa --> thay đổi liên kết
                    node.next = current.next
                    current.next = node
                    self.size += 1
                return
            current = current.next
        # Case 2: Không tìm thấy previous node --> chèn ở đầu ds
        self.insert_start(data)
