class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printing(self):
        print(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('Dog')
    q.enqueue('cat')
    q.enqueue('3.4')
    q.dequeue()
    print(q.size())
    q.printing()
