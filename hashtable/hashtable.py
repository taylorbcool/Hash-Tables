class HashTableEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        hash_int = 5381
        byte_arr = key.encode()

        for byte in byte_arr:
            hash_int = ((hash_int * 33) ^ byte) % 0x100000000
        
        return hash_int

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
      
        key_hash = self.hash_index(key)
        entry = HashTableEntry(key, value)
        if self.storage[key_hash] is None:
            self.storage[key_hash] = entry
        else:
            node = self.storage[key_hash]
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev = node
                node = node.next
            prev.next = entry
            
    def delete(self, key):

        warning = 'Given key does not exist in table.'
        key_hash = self.hash_index(key)
        if not self.storage[key_hash]:
            print(warning)
            return None
        node = self.storage[key_hash]
        if node.key == key:
            self.storage[key_hash] = node.next
            return None
        else:
            prev = node
            cur = node.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    return None
                cur = cur.next
        print(warning)
        return None

    def get(self, key):

        key_hash = self.hash_index(key)
        if self.storage[key_hash] is not None:
            node = self.storage[key_hash]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
            return None
        else:
            return None

    def resize(self):
        
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for node in self.storage:
            while node:
                key_hash = self.hash_index(node.key)
                new_storage[key_hash] = node
                node = node.next
        self.storage = new_storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
