class SinglyLinkedList():
    class Node():
        def __init__(self, value = 0, next = None):
            self.val = value
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        if not self.head:
            self.tail = self.head = self.Node(value)
        else:
            self.tail.next = self.Node(value)
            self.tail = self.tail.next
        self.size += 1

    def insert(self, value, index):
        if index < 0 or self.size < index:
            raise Exception("Index out of bounds.")
        else:
            if index == 0:
                self.head = self.Node(value, self.head)
            else:
                temp = 0
                curr = self.head
                while temp < index - 1:
                    curr = curr.next
                    temp += 1
                curr.next = self.Node(value, curr.next)
            self.size += 1        

    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    
    def status(self):
        print(f"Size:   {self.size}")
        print(f"Head:   {self.head.val}")
        print(f"Tail:   {self.tail.val}")


s = SinglyLinkedList()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)

s.insert(3, 0)
s.insert(1, 4)

s.print()
s.status()