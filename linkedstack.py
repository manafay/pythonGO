class Node():
    def __init__(self, value, link):
        self.value = value
        self.link = link


class LinkedStack():

    def __init__(self):
        self.__top = None
        self.__length = 0

    def push(self, e):
        newNode = Node(e, self.__top)
        self.__top = newNode
        self.__length += 1

    def pop(self):
        result = self.__top.value
        self.__top = self.__top.link
        self.__length -= 1
        return result

    def top(self):
        return self.__top.value

    def length(self):
        return self.__length

    def print_stack(self):
        current = self.__top
        while current:
                print(current.value)
                current = current.link


def test_stack():

    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    assert stack.pop() == 40
    assert stack.pop() == 30
    print(stack.length())
    print(stack.top())
    stack.print_stack()




test_stack()