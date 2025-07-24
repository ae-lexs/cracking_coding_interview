class HashTable(object):
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self.__hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self.__hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if key == key:
                return v

        return None

    def delete(self, key):
        index = self.__hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if key == k:
                del bucket[i]

                return True

        return False


ht = HashTable()

ht.set("apple", 10)
ht.set("banana", 20)
ht.set("orange", 30)

print("table", ht.table)
print(ht.get("banana"))  # Output: 20

ht.delete("banana")
print(ht.get("banana"))  # Output: None







