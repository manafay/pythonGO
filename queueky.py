from stack import Stack;

class Queueky():
    def __init__(self):
        self.__s = Stack()

    def enqueue(self, elem):
         self.__s.push(elem)

    def dequeue(self):
        temp = Stack()
        cache = Stack()
        while self.__s.count() > 1:
            temp.push(self.__s.pop())
        while temp.count() > 0:
            cache.push(temp.pop())
        result = self.__s.pop()
        self.__s = cache    
        return result

    def is_empty(self):
        return self.__s.is_empty()

    def top(self):
        return self.__s.top()

    def count(self):
        return self.__s.count()

s = Queueky()

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