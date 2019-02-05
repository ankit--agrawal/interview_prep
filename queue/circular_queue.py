class Circular():
    def __init__(self, l):
        self.items = list()
        self.head = 0
        self.tail = 0
        self.MaxSize = l

    def enqueue(self,item):
        if self.size() == self.MaxSize - 1:
            return("Queue is full")
        self.items.append(item)
        self.tail = (self.tail + 1) % self.MaxSize
        return True

    def dequeue(self):
        if self.size() == 0:
            return("Queue is empty")
        data = self.items[self.head]
        self.head = (self.head + 1) % self.MaxSize
        return data

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.MaxSize - (self.head - self.tail)

    def printing(self):
        print(self.items)

if __name__ == '__main__':
    q = Circular(4)
    q.enqueue(1)
    print(q.enqueue('Dog'))
    print(q.enqueue('Cat'))
    print(q.enqueue('2'))
    print(q.dequeue())
    q.printing()
    q.enqueue('100')
    q.dequeue()
    q.enqueue(99)
    q.dequeue()
    print(q.enqueue(111))
    print(q.size())
    q.printing()
