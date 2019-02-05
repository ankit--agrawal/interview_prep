class Dequeue():
    def __init__(self):
        self.items = []

    def front_enqueue(self,item):
        self.items.insert(0,item)

    def rear_enqueue(self,item):
        self.items.append(item)

    def front_dequeue(self):
        self.items.pop(0)

    def rear_dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printing(self):
        print(self.items)

if __name__ == '__main__':
    q = Dequeue()
    q.front_enqueue(4)
    q.front_enqueue('Dog')
    q.rear_enqueue('cat')
    q.printing()
    q.front_dequeue()
    q.printing()
    q.rear_dequeue()
    q.printing()
