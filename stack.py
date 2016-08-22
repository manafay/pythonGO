class Stack():

    def __init__(self):
        self.__arr = []
        self.__top = 0

    def push(self, elem):
        self.__arr[self.__top] = elem
        self.__top += 1
        return self.__arr

    def pop(self):
        return self.__arr.pop()

    def is_empty(self):
        return len(self.__arr) == 0

    def count(self):
        return len(self.__arr)


s = Stack()

print(s.push(7))
print(s.pop())
print(s.count())
print(s.is_empty())
