class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=32):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def _resize_table(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for item in self.table:
            current = item
            while current is not None:
                index = self._hash_function(current.key)
                while new_table[index] is not None:
                    index = (index + 1) % new_capacity

                new_table[index] = Node(current.key, current.value)
                current = current.next

        self.table = new_table
        self.capacity = new_capacity

    def insert(self, key, value):
        if self.size / self.capacity > 0.7:
            self._resize_table()

        index = self._hash_function(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                return False  # Key already exists
            index = (index + 1) % self.capacity

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1
        return True

    def modify(self, key, value):
        index = self._hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return True  # Modification successful
            current = current.next
        return False  # Key not found

    def remove(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True  # Removal successful
            prev = current
            current = current.next
        return False  # Key not found

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found

    def get_capacity(self):
        return self.capacity

    def print_table(self):
        for i, item in enumerate(self.table):
            if item is not None:
                print(f"{i}: ", end="")
                current = item
                while current is not None:
                    print(f"({current.key}: {current.value})", end=" -> ")
                    current = current.next
                print("None")
            else:
                print(f"{i}: None")

    def __len__(self):
        return self.size
    def print_table(self):
        for i, item in enumerate(self.table):
            if item is not None:
                print(f"{i}: ", end="")
                current = item
                while current is not None:
                    print(f"({current.key}: {current.value})", end=" -> ")
                    current = current.next
                print("None")
            else:
                print(f"{i}: None")

# Interactive script
hash_table = HashTable()

while True:
    print("\n1. Insert")
    print("2. Modify")
    print("3. Remove")
    print("4. Search")
    print("5. Print Table")
    print("6. Print Size")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        key = input("Enter key: ")
        value = input("Enter value: ")
        if hash_table.insert(key, value):
            print("Insertion successful!")
        else:
            print("Key already exists. Insertion failed.")

    elif choice == '2':
        key = input("Enter key to modify: ")
        value = input("Enter new value: ")
        if hash_table.modify(key, value):
            print("Modification successful!")
        else:
            print("Key not found. Modification failed.")

    elif choice == '3':
        key = input("Enter key to remove: ")
        if hash_table.remove(key):
            print("Removal successful!")
        else:
            print("Key not found. Removal failed.")

    elif choice == '4':
        key = input("Enter key to search: ")
        result = hash_table.search(key)
        if result is not None:
            print(f"Value: {result}")
        else:
            print("Key not found.")

    elif choice == '5':
        hash_table.print_table()

    elif choice == '6':
        print(f"Size of the hash table: {len(hash_table)}")

    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
