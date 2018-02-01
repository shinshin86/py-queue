class Queue:
    def __init__(self, max_size=100):
        self.max_buffer = max_size
        self.head = 0
        self.tail = 0
        self.index = 1
        self.array = [None] * max_size

    def is_full(self):
        if (not self.is_empty() and
           (self.head == ((self.tail) % (self.max_buffer)))):
            return True

    def is_empty(self):
        return self.head == self.tail

    def get_size(self):
        if self.is_empty():
            return 0
        else:
            return sum(x is not None for x in self.array)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return False

        data = self.array[self.head]
        self.array[self.head] = None

        if self.head + 1 >= self.max_buffer:
            self.head = 0
        else:
            self.head += 1

        return data

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!")
            return False

        self.array[self.tail] = data

        if self.tail >= self.max_buffer:
            self.tail = 0
        else:
            self.tail += 1

    def print_queue_all(self):
        print(self.array)
        print("head : ", self.head)
        print("tail : ", self.tail)

    def get_queue_all_list(self):
        return self.array[self.head:self.tail]
