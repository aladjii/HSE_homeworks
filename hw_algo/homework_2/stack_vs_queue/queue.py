from linked_list import Node, LinkedList

class Queue(LinkedList):
    def enqueue(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value
