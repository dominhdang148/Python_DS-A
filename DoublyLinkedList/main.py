from doubly_linked_list import DoublyLinkedList

a = DoublyLinkedList()
a.append(1)
a.append(5)
a.append(12)
a.append(2)
for item in a.iter(reverse=False):
    print(item)
a.delete(12)
print("result")
for item in a.iter(reverse=False):
    print(item)
