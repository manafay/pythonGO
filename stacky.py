from queue import Queue;

class Stacky():
    def __init__(self):
        self.__q = Queue()
    
    def push(self, elem):
        self.__q.enqueue(elem)
    
    def pop(self): 
        temp = Queue()
        while self.__q.count() > 1:
            temp.enqueue(self.__q.dequeue())
        result = self.__q.dequeue()
        self.__q = temp    
        return result

    def is_empty(self):
        return self.__q.is_empty()
    
    def count(self):
        return self.__q.count()
    
    def top(self):
        return self.__q.top()
    

s = Stacky()

print(s.push(5))
print(s.push(3))
print(s.push(6))
print(s.push(7))
print(s.pop())
print(s.count())
print(s.is_empty())
print(s.top())