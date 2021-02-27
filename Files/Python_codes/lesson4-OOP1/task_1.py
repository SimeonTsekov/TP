class CustomStack:
    def __init__(self):
        self.__data = []

    def push(self, value):
        self.__data.append(value)
        print(self.__data[len(self.__data) - 1])

    def pop(self):
        return(self.__data.pop())
    
    def size(self):
        return(len(self.__data))

MyStack = CustomStack()

MyStack.push(1)
MyStack.push(2)
MyStack.push(3)
MyStack.push(4)

popped = MyStack.pop()
print(popped)

size = MyStack.size()
print(size)
