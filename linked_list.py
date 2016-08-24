from node import Node

class LinkedList():
    def __init__(self):
        self.__root = None
        self.__length = 0

    def count(self):
        return self.__length

    def insert_first(self, elem):
        newNode = Node(elem, self.__root)
        self.__root = newNode
        self.__length += 1

    def delete_first(self):
        result = self.__root.value
        self.__root = self.__root.link
        self.__length -= 1
        return result

    def insert_after(self, node, e):
        newNode = Node(e, node.link)
        node.link = newNode
        self.__length += 1

    def delete_after(self, node):
        node.link = node.link.link
        self.__length -= 1    


    def print_linkedlist(self):
        current = self.__root
        while current:
            print(current.value)
            current = current.link

    def find(self, val):
        current = self.__root
        while current:
            if current.value == val:
                return current
            current = current.link
        return None
