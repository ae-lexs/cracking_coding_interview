class ArrayList(object):
    def __init__(self):
        self.capacity = 4
        self.count = 0
        self.data = [None] * self.capacity

    def __str__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.count)) + "]"

    def __resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")

        new_data = [None] * (self.capacity * 2)

        for index in range(self.count):
            new_data[index] = self.data[index]

        self.data = new_data
        self.capacity *= 2

    def __check_valid_index(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")

    def append(self, value):
        if self.count == self.capacity:
            self.__resize()

        self.data[self.count] = value
        self.count += 1

    def get(self, index):
        self.__check_valid_index(index)

        return self.data[index]

    def set(self, index, value):
        self.__check_valid_index(index)

        self.data[index] = value

    def remove(self, index):
        self.__check_valid_index(index)

        for i in range(index, self.count - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.count - 1] = None
        self.count -= 1

    def size(self):
        return self.count



arr = ArrayList()
arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
arr.append(50)

print(arr)            # [10, 20, 30, 40, 50]
print(arr.get(2))     # 30

arr.set(2, 99)
print(arr)            # [10, 20, 99, 40, 50]

arr.remove(1)
print(arr)            # [10, 99, 40, 50]

print("Size:", arr.size())  # 4

