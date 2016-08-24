class Stack():

    def __init__(self):
        self.__arr = []

    def push(self, elem):
        self.__arr.append(elem)

    def pop(self):
        return self.__arr.pop()

    def is_empty(self):
        return len(self.__arr) == 0

    def top(self):
        return self.__arr[-1]

    def count(self):
        return len(self.__arr)


s = Stack()

print(s.push(5))
print(s.push(3))
print(s.push(5))
print(s.push(7))
print(s.pop())
print(s.count())
print(s.is_empty())
print(s.top())