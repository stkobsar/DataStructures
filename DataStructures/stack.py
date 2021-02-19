class Stack:

    ### Constructor ###

    def __init__(self):
        self.items = []  # Names items properties of the object we're creating

    ##################

    def is_empty(self):
        return len(self.items) == 0
        # return not self.items [other way of doing it]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    print("Array with no items:", s)
    s.is_empty()

    s.push(5)
    s.push(7)
    s.push(3)
    print("Added items:", s)

    s.pop()
    print("Array after pop:", s)
    print("Last number added:", s.peek())
