class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]

    def isEmpty(self):
        return self.data == []

    def sort(self):
        self.data = self.mergeSort(self.data)

    def mergeSort(self, data):
        #check for base case
        if len(data) == 1:
            return data
        #split in two
        mid = len(data)//2
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:])
        #merge two sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]
            elif len(left) > 0:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        return result

#test code
stack = Stack()
stack.push(3)
stack.push(2)
stack.push(7)
stack.push(4)
stack.sort()

while not stack.isEmpty():
    print(stack.pop())

