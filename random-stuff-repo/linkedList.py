class LinkedList:
    class Node:
        def __init__(self, value = None, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0
    
    def append(self, value):
        newNode = self.Node(value)
        if self.head:
            self.end.next = newNode
            self.end = self.end.next
        else:
            self.end = self.head = newNode
        self.size += 1
    
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current = 0
            temp = self.head
            while current != index - 1:
                temp = temp.next
                current += 1
            temp.next = temp.next.next
        self.size -= 1
        
    def insert(self, value, index):
        if index == 0:
            newNode = self.Node(value, self.head)
            self.head = newNode
        else:
            current = 0
            temp = self.head
            while current != index - 1:
                temp = temp.next
                current += 1
            newNode = self.Node(value, temp.next)
            temp.next = newNode
        self.size += 1

    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.delete(2)
list.insert(3, 2)
list.printList()