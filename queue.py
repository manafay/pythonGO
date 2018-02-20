class Queue():
    def __init__(self):
        self.__arr = []

    def enqueue(self, elem):
        return self.__arr.append(elem)

    def dequeue(self):
        first = self.__arr[0]
        self.__arr = self.__arr[1:]
        return first

    def is_empty(self):
        return len(self.__arr) == 0

    def top(self):
        return self.__arr[0]

    def count(self):
        return len(self.__arr)

s = Queue()

print(s.enqueue(5))
print(s.enqueue(3))
print(s.enqueue(5))
print(s.enqueue(7))
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.count())
print(s.is_empty())
print(s.top())